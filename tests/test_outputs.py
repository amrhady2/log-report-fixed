import json
from pathlib import Path


REPORT = Path("/app/report.json")


def load_report():
    assert REPORT.exists(), "report.json was not created at /app/report.json"
    return json.loads(REPORT.read_text())


def test_report_exists_and_is_valid_json():
    """Success criterion 1: /app/report.json exists and contains valid JSON."""
    report = load_report()
    assert isinstance(report, dict), "report.json must contain a JSON object"


def test_report_has_exact_required_keys():
    """Success criterion 2: report contains exactly the required keys."""
    report = load_report()
    assert set(report) == {"total_requests", "unique_ips", "top_path"}


def test_total_requests():
    """Success criterion 3: total_requests is 6."""
    report = load_report()
    assert report["total_requests"] == 6


def test_unique_ips():
    """Success criterion 4: unique_ips is 3."""
    report = load_report()
    assert report["unique_ips"] == 3


def test_top_path():
    """Success criterion 5: top_path is /index.html."""
    report = load_report()
    assert report["top_path"] == "/index.html"