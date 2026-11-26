from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict


class BusinessRecordCreate(BaseModel):

    record_name: str = Field(min_length=2, max_length=150)

    department: str = Field(min_length=2, max_length=100)

    amount: float = Field(ge=0)

    status: str = "PENDING"

    description: str | None = None


class BusinessRecordResponse(BusinessRecordCreate):

    id: int

    created_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)