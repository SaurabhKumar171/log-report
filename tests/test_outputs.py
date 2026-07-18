import json


def test_report_is_valid_json():
    """Success criterion 1: Create /app/report.json as valid JSON."""
    with open("/app/report.json") as f:
        json.load(f)


def test_request_and_ip_counts():
    """Success criterion 2: Set total_requests to 6 and unique_ips to 3."""
    with open("/app/report.json") as f:
        report = json.load(f)

    assert report["total_requests"] == 6
    assert report["unique_ips"] == 3


def test_top_path():
    """Success criterion 3: Set top_path to /index.html."""
    with open("/app/report.json") as f:
        report = json.load(f)

    assert report["top_path"] == "/index.html"