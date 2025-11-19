from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Employee:
    name: str
    position: str
    completed_tasks: int
    performance: float
    skills: str
    team: str
    experience_years: int

@dataclass(frozen=True)
class PerformanceReportRow:
    position: str
    average_performance: float