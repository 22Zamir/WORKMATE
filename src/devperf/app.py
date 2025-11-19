from typing import List
from pathlib import Path
from .models import Employee
from .reports.base import ReportGenerator, ReportData
from .reports.performance import PerformanceReportGenerator
from .readers import read_employees_from_csv

AVAILABLE_REPORTS = {
    "performance": PerformanceReportGenerator(),
}

def run_report(
    filepaths: List[Path],
    report_name: str,
    report_registry: dict[str, ReportGenerator] = AVAILABLE_REPORTS
) -> List[ReportData]:
    if report_name not in report_registry:
        raise ValueError(f"Неизвестный отчёт: {report_name}. Доступны: {list(report_registry.keys())}")

    all_employees: List[Employee] = []
    for fp in filepaths:
        all_employees.extend(read_employees_from_csv(fp))

    generator = report_registry[report_name]
    return generator.generate(all_employees)