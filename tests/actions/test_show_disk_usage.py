from pro_filer.actions.main_actions import show_disk_usage  # NOQA
from unittest.mock import Mock, patch

def test_show_disk_usage_with_files(capsys, tmp_path):
    file = tmp_path / "__init__.py"
    file2 = tmp_path / "app.py"    
    path_mock = Mock()
    path_mock.getsize.side_effect = [0, 4000, 0, 4000, 4000, 0]
    with patch("os.path", path_mock):
        context = { "all_files": [str(file), str(file2)] }
        show_disk_usage(context)
    captured = capsys.readouterr().out.splitlines()
    assert captured[0].__contains__("app.py")
    assert captured[0].__contains__("4000 (100%)")
