from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class TaskBase(BaseModel):
    title: str = Field(..., min_length=10, max_length=100)
    description: Optional[str] = None
    is_completed: bool = False
    is_in_progress: bool = False
    priority: int = Field(
        1,
        ge=1,
        le=5,
        description='Priority must be between 1 (lowest) and 5 (highest)',
    )

    model_config = ConfigDict(extra='forbid')
    # Forbid extra fields not defined in the model


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=10, max_length=100)
    description: Optional[str] = None
    is_completed: Optional[bool] = None
    is_in_progress: Optional[bool] = None
    priority: Optional[int] = Field(
        None,
        ge=1,
        le=5,
        description='Priority must be between 1 (lowest) and 5 (highest)',
    )

    model_config = ConfigDict(extra='forbid')


class TaskRead(TaskBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
