from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func

from app.core.database import Base


class BusinessRecord(Base):

    __tablename__ = "business_records"

    id = Column(Integer, primary_key=True, index=True)

    record_name = Column(String(150), nullable=False)

    department = Column(String(100), nullable=False)

    amount = Column(Float, nullable=False, default=0)

    status = Column(
        String(50),
        nullable=False,
        default="PENDING"
    )

    description = Column(String(500), nullable=True)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )