from dataclasses import dataclass
from datetime import datetime

from enumerations.main import *


@dataclass
class Exercise:
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
