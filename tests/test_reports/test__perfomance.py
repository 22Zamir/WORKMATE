import pytest
from devperf.models import Employee
from devperf.reports.performance import PerformanceReportGenerator

@pytest.fixture
def generator():
    return PerformanceReportGenerator()

@pytest.mark.parametrize("employees,expected", [
    (
        [
            Employee("A", "Dev", 10, 4.5, "", "T", 2),
            Employee("B", "Dev", 10, 5.5, "", "T", 2),
        ],
        [{"position": "Dev", "avg": 5.0}]
    ),
    (
        [
            Employee("A", "Frontend", 10, 4.0, "", "T", 1),
            Employee("B", "Backend", 10, 5.0, "", "T", 3),
        ],
        [
            {"position": "Backend", "avg": 5.0},
            {"position": "Frontend", "avg": 4.0},
        ]
    ),
    ([], []),
])
def test_performance_report(generator, employees, expected):
    result = generator.generate(employees)
    assert len(result) == len(expected)
    for r, e in zip(result, expected):
        assert r.position == e["position"]
        assert r.average_performance == e["avg"]


