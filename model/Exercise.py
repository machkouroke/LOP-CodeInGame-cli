from datetime import datetime
from pydantic import BaseModel, Field

from enumerations.main import *


class Exercise(BaseModel):
    id: str
    name: str
    language: ProgramingLanguage
    kind: ExerciseKind
    owner: str
    subscribers: list[str]
    created_at: datetime
    start: datetime = None
    end: datetime = None
    owner_name: str = None
    status: str = None
