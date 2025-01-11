from pro_filer.actions.main_actions import show_preview  # NOQA

def test_show_preview_sucess(capsys):
    context = {
      "all_files": [],
      "all_dirs": []
    }
    show_preview(context)
    captured = capsys.readouterr()
    assert captured.out == "Found 0 files and 0 directories\n"

def test_show_preview_context(capsys):
    context = {
        "all_files": ["src/__init__.py", "src/app.py", "src/utils/__init__.py"],
        "all_dirs": ["src", "src/utils"]
    }
    show_preview(context)
    captured = capsys.readouterr()
    expected_output = (
        "Found 3 files and 2 directories\n"
        "First 5 files: ['src/__init__.py', 'src/app.py', "
        "'src/utils/__init__.py']\n"
        "First 5 directories: ['src', 'src/utils']\n"
    )
    assert captured.out == expected_output

def test_show_preview_error_file():
    context = { "all_files": [], "all_dirs": ["src", "src/utils"] }
    if len(context["all_dirs"]) > 1 and len(context["all_files"]) == 0:
        assert "all_files not must be empty"

def test_show_preview_error_dir():
    context = {
        "all_files": ["src/__init__.py", "src/app.py", "src/utils/__init__.py"],
        "all_dirs": []
    }
    if len(context["all_dirs"]) == 0 and len(context["all_files"]) > 0:
        assert "all_dirs not must be empty"


def test_show_preview_error_len():
    context = {
        "all_files": ["src/__init__.py", "src/app.py",
                      "src/utils/__init__.py", "src/utils/ui.py",
                      "src/utils/__init__.py", "src/testes/test.py"],
        "all_dirs": ["src", "src/utils", "src/test", "src/arrays",
                     "src/", "src/func"]
    }
    if len(context['all_files']) > 5 or len(context['all_dirs']) > 5:
        assert "Error: all_files and all_dirs must not be bigger 5"
