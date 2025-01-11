from pro_filer.actions.main_actions import show_preview  # NOQA

def test_show_preview(capsys):
    context = {
      "all_files": [],
      "all_dirs": []
    }
    show_preview(context)
    captured = capsys.readouterr()
    assert captured.out == "Found 0 files and 0 directories\n"


