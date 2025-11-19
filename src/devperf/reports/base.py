from abc import ABC, abstractmethod
from typing import List, Protocol
from ..models import Employee

class ReportData(Protocol):
    """Протокол ожидаемого результата отчёта."""
    pass

class ReportGenerator(ABC):
    """Абстрактный класс для генераторов отчётов."""

    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @abstractmethod
    def generate(self, employees: List[Employee]) -> List[ReportData]:
        ...