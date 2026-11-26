from sqlalchemy.orm import Session

from app.models.business_record import BusinessRecord
from app.schemas.business_record import BusinessRecordCreate


class RecordService:

    @staticmethod
    def create_record(
        db: Session,
        record_data: BusinessRecordCreate
    ):

        record = BusinessRecord(
            **record_data.model_dump()
        )

        db.add(record)
        db.commit()
        db.refresh(record)

        return record

    @staticmethod
    def get_record(db: Session, record_id: int):

        return db.query(BusinessRecord).filter(
            BusinessRecord.id == record_id
        ).first()

    @staticmethod
    def get_all_records(
        db: Session,
        department: str | None = None,
        skip: int = 0,
        limit: int = 100
    ):

        query = db.query(BusinessRecord)

        if department:
            query = query.filter(
                BusinessRecord.department == department
            )

        return query.order_by(
            BusinessRecord.id.desc()
        ).offset(skip).limit(limit).all()

    @staticmethod
    def update_record(
        db: Session,
        record_id: int,
        record_data: BusinessRecordCreate
    ):

        record = RecordService.get_record(db, record_id)

        if not record:
            return None

        for key, value in record_data.model_dump().items():
            setattr(record, key, value)

        db.commit()
        db.refresh(record)

        return record

    @staticmethod
    def delete_record(db: Session, record_id: int):

        record = RecordService.get_record(db, record_id)

        if not record:
            return False

        db.delete(record)
        db.commit()

        return True