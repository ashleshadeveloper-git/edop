from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.core.database import get_db
from app.models.business_record import BusinessRecord

router = APIRouter(
    prefix="/api/v1/reports",
    tags=["Reports"]
)


@router.get("/summary")
def get_report_summary(db: Session = Depends(get_db)):

    total_records = db.query(
        func.count(BusinessRecord.id)
    ).scalar()

    total_amount = db.query(
        func.coalesce(func.sum(BusinessRecord.amount), 0)
    ).scalar()

    department_summary = db.query(
        BusinessRecord.department,
        func.count(BusinessRecord.id).label("record_count"),
        func.sum(BusinessRecord.amount).label("total_amount")
    ).group_by(
        BusinessRecord.department
    ).all()

    return {
        "total_records": total_records,
        "total_amount": float(total_amount),
        "department_summary": [
            {
                "department": row.department,
                "record_count": row.record_count,
                "total_amount": float(row.total_amount or 0)
            }
            for row in department_summary
        ]
    }