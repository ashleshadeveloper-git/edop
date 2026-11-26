from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.business_record import (
    BusinessRecordCreate,
    BusinessRecordResponse
)
from app.services.record_service import RecordService

router = APIRouter(
    prefix="/api/v1/records",
    tags=["Business Records"]
)


@router.post(
    "/",
    response_model=BusinessRecordResponse,
    status_code=201
)
def create_record(
    record: BusinessRecordCreate,
    db: Session = Depends(get_db)
):
    return RecordService.create_record(db, record)


@router.get(
    "/",
    response_model=list[BusinessRecordResponse]
)
def get_records(
    department: str | None = None,
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    db: Session = Depends(get_db)
):
    return RecordService.get_all_records(
        db,
        department,
        skip,
        limit
    )


@router.get(
    "/{record_id}",
    response_model=BusinessRecordResponse
)
def get_record(
    record_id: int,
    db: Session = Depends(get_db)
):

    record = RecordService.get_record(db, record_id)

    if not record:
        raise HTTPException(
            status_code=404,
            detail="Business record not found"
        )

    return record


@router.put(
    "/{record_id}",
    response_model=BusinessRecordResponse
)
def update_record(
    record_id: int,
    record: BusinessRecordCreate,
    db: Session = Depends(get_db)
):

    updated = RecordService.update_record(
        db,
        record_id,
        record
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Business record not found"
        )

    return updated


@router.delete("/{record_id}")
def delete_record(
    record_id: int,
    db: Session = Depends(get_db)
):

    deleted = RecordService.delete_record(db, record_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Business record not found"
        )

    return {"message": "Record deleted successfully"}