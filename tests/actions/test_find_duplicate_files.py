from pro_filer.actions.main_actions import find_duplicate_files  # NOQA
from unittest.mock import patch
import os
import pytest


@patch("pro_filer.actions.main_actions.filecmp")
def test_find_duplicates_files(mock_filecmp, tmp_path):
    tmp_path1 = tmp_path / "file1.txt"
    tmp_path1.write_text("Hello Gabriel")
    tmp_path2 = tmp_path / "file2.txt"
    tmp_path2.write_text("Hello Gabriel")
    tmp_path3 = tmp_path / "file3.txt"
    tmp_path3.write_text("Bye!")
    mock_filecmp.cmp.side_effect = [True, False, False]
    context = {"all_files": [tmp_path1, tmp_path2, tmp_path3]}
    assert find_duplicate_files(context) == [(tmp_path1, tmp_path2)]
    assert os.path.isfile(tmp_path1)
    
def test_find_duplicate_error():
    context = {"all_files": ["tmp_path1", "tmp_path2", "tmp_path3"]}
    with pytest.raises(ValueError):
        find_duplicate_files(context)
