from collections import defaultdict
from typing import List
from ..models import Employee, PerformanceReportRow
from .base import ReportGenerator, ReportData

class PerformanceReportGenerator(ReportGenerator):
    @property
    def name(self) -> str:
        return "performance"

    def generate(self, employees: List[Employee]) -> List[PerformanceReportRow]:
        if not employees:
            return []

        # Группировка по позициям
        perf_by_position = defaultdict(list)
        for emp in employees:
            perf_by_position[emp.position].append(emp.performance)

        # Подсчёт среднего
        result = [
            PerformanceReportRow(
                position=pos,
                average_performance=round(sum(vals) / len(vals), 2)
            )
            for pos, vals in perf_by_position.items()
        ]

        # Сортировка по убыванию средней эффективности
        result.sort(key=lambda x: x.average_performance, reverse=True)
        return result