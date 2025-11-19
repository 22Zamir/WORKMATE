import argparse
import sys
from pathlib import Path
from tabulate import tabulate
from .app import run_report
from .reports.performance import PerformanceReportRow

def main() -> None:
    parser = argparse.ArgumentParser(description="Анализ эффективности разработчиков")
    parser.add_argument("--files", nargs="+", required=True, type=Path)
    parser.add_argument("--report", choices=["performance"], default="performance")

    args = parser.parse_args()

    try:
        report_data = run_report(args.files, args.report)

        # Вывод
        if not report_data:
            print("⚠️  Нет данных для отчёта.")
            return

        if isinstance(report_data[0], PerformanceReportRow):
            table = [
                [row.position, row.average_performance] for row in report_data
            ]
            print(tabulate(table, headers=["Позиция", "Средняя эффективность"], tablefmt="grid"))
        else:
            # Расширяемость: можно добавить другие форматы вывода
            raise NotImplementedError(f"Вывод для отчёта {args.report} не реализован")

    except Exception as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()