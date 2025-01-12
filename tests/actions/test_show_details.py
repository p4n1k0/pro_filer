from pro_filer.actions.main_actions import show_details  # NOQA
import datetime
import pytest
from unittest.mock import patch

@pytest.fixture
def temporary_file(tmp_path):
    tmp_path = tmp_path / "file1.txt"    
    return tmp_path

def test_show_details_exists(capsys, temporary_file):
    with patch(
        "pro_filer.actions.main_actions.os.path.exists", return_value=True
    ), patch(
        "pro_filer.actions.main_actions.os.path.getsize", return_value=100
    ), patch(
        "pro_filer.actions.main_actions.os.path.isdir", return_value=False
    ), patch(
        "pro_filer.actions.main_actions.os.path.getmtime",
        return_value=1623542400,
    ), patch(
        "pro_filer.actions.main_actions.date", spec=datetime.date
    ) as mock_date:        
        mock_date.fromtimestamp.return_value = datetime.date(2025, 1, 11)
        show_details({"base_path": str(temporary_file)})
    expected_output = (
        "File name: file1.txt\n"
        "File size in bytes: 100\n"
        "File type: file\n"
        "File extension: .txt\n"
        "Last modified date: 2025-01-11\n"
    )
    captured = capsys.readouterr()
    assert captured.out == expected_output
