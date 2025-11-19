import csv
from pathlib import Path
from typing import List
from .models import Employee

def read_employees_from_csv(filepath: Path) -> List[Employee]:
    """Читает CSV и возвращает список сотрудников."""
    employees = []
    try:
        with open(filepath, encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    emp = Employee(
                        name=row["name"],
                        position=row["position"],
                        completed_tasks=int(row["completed_tasks"]),
                        performance=float(row["performance"]),
                        skills=row["skills"],
                        team=row["team"],
                        experience_years=int(row["experience_years"]),
                    )
                    employees.append(emp)
                except (KeyError, ValueError, TypeError) as e:
                    raise ValueError(f"Некорректные данные в файле {filepath}, строка {reader.line_num}: {e}")
        return employees
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Файл не найден: {filepath}") from e