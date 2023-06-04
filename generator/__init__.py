from typing import Type

from generator.base import AbstractGenerator
from generator.python import PythonGenerator

generator: dict[str,  Type[AbstractGenerator]] = {
    "Python": PythonGenerator,
}