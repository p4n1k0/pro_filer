from pro_filer.actions.main_actions import show_details  # NOQA
from io import StringIO
from pathlib import Path
from unittest.mock import patch

def test_msg_correct(tmp_path):
    tmp_path = tmp_path / "Trybe_logo.png"
    tmp_path.touch()
    file_path = Path(tmp_path)
    context = { "base_path": str(file_path) }
    expected_output = (
        "File name: Trybe_logo.png\n"
        "File size in bytes: 0\n"
        "File type: file\n"
        "File extension: .png\n"
        "Last modified date: 2025-01-11\n"
    )
    with patch("pro_filer.actions.main_actions.os.path.isfile",
               return_value=True), \
         patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        show_details(context)
        captured = mock_stdout.getvalue()
    assert captured == expected_output

def test_msg_wrong(capsys):
    context = { "base_path": "/home/trybe/Trybe.png" }
    show_details(context)
    captured = capsys.readouterr()
    expected_output = ("File 'Trybe.png' does not exist\n")
    assert captured.out == expected_output

def test_correct_extension(tmp_path):
    tmp_path = tmp_path / "Trybe_logo"
    tmp_path.touch()
    file_path = Path(tmp_path)
    context = { "base_path": str(file_path) }
    expected_output = (
        "File name: Trybe_logo\n"
        "File size in bytes: 0\n"
        "File type: file\n"
        "File extension: [no extension]\n"
        "Last modified date: 2025-01-11\n"
    )
    with patch("pro_filer.actions.main_actions.os.path.isfile",
               return_value=True), \
         patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        show_details(context)
        captured = mock_stdout.getvalue()
        assert captured == expected_output
