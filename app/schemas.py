from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional


" schemas are the structure of a data base / http operation"

class IssueStatus(str, Enum):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    CLOSED = "closed"


class IssuePriority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class IssueCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: Optional[str] = Field(default=None, max_length=500)
    priority:IssuePriority = IssuePriority.MEDIUM


class IssueUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=100)
    description: Optional[str] = Field(default=None, max_length=500)
    status: Optional[IssueStatus] = None
    priority: Optional[IssuePriority] = None
 

class IssueOut(BaseModel):
    id:str
    title: str
    description: Optional[str]=None
    status: IssueStatus
    priority: IssuePriority

# batch operations

class Batch_Issue_Create(BaseModel):
    issues: list[IssueCreate]

class Design_of_Batch_Issue_Update(BaseModel):
    id:str = Field(min_length=1,max_length=340)
    title: Optional[str] = Field(default=None, min_length=1, max_length=100)
    description: Optional[str] = Field(default=None, max_length=500)
    status: Optional[IssueStatus] = IssueStatus.OPEN
    priority: Optional[IssuePriority] = IssuePriority.MEDIUM

class Batch_Issue_Update(BaseModel):
    issues: list[Design_of_Batch_Issue_Update]