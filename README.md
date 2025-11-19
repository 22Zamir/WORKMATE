# Dev Performance Analyzer  
Скрипт для анализа эффективности разработчиков на основе CSV-данных.

> ✅ Чистая архитектура • ✅ Расширяемость • ✅ Тестируемость  
> Реализован строго по ТЗ: только стандартная библиотека (`argparse`, `csv`), `tabulate` для вывода. Без `pandas`, `click`.

---

## Возможности

- Чтение **нескольких CSV-файлов** с данными о сотрудниках.
- Агрегация данных **по всем файлам** (не по отдельности).
- Формирование отчётов через расширяемый реестр генераторов.
- Поддерживаемый отчёт:  
  **`performance`** — средняя эффективность по позициям (сортировка по убыванию).

Формат CSV:
```csv
name,position,completed_tasks,performance,skills,team,experience_years
Alex Ivanov,Backend Developer,45,4.8,"Python, Django",API Team,5

python -m venv venv
venv\Scripts\activate          # Windows (PowerShell/cmd)
# source venv/bin/activate     # Linux/macOS

pip install -r requirements.txt




$env:PYTHONPATH="src"; python -m devperf.cli --files example_data/employees1.csv example_data/employees2.csv --report performance
