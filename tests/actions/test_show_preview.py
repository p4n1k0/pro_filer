from pro_filer.actions.main_actions import show_preview  # NOQA


def test_show_preview_success(capsys):
    # GIVEN
    context = {
        
        "all_files": ["src/__init__.py", "src/app.py", "src/utils/__init__.py"],
        "all_dirs": ["src", "src/utils"],
    }
    expected_out =  f"Found 3 files and 2 directories\nFirst 5 files: ['src/__init__.py', 'src/app.py', 'src/utils/__init__.py']\nFirst 5 directories: ['src', 'src/utils']\n"
    show_preview(context)
    captured = capsys.readouterr()
    assert captured.out == expected_out

def test_show_preview_with_context(capsys):
    context = {        
        "all_files": [],
        "all_dirs": [],
    }
    expected_out =  f"Found 0 files and 0 directories\n"
    show_preview(context)
    captured = capsys.readouterr()
    assert captured.out == expected_out

def test_show_preview_with_five_files(capsys):
    context = {
        "all_files": [
            "src/__init__.py", "src/app.py","src/utils/__init__.py",
            "src/utils/alpha.py", "src/utils/beta.py", "src/utils/gama.py"
        ],
        "all_dirs": ["src", "src/utils"],
        
    }
    expected_out =  f"Found 6 files and 2 directories\nFirst 5 files: ['src/__init__.py', 'src/app.py', 'src/utils/__init__.py', 'src/utils/alpha.py', 'src/utils/beta.py']\nFirst 5 directories: ['src', 'src/utils']\n"
    show_preview(context)
    captured = capsys.readouterr()
    assert captured.out == expected_out


def test_show_preview_with_five_directories(capsys):
    context = {
        "all_files": [
            "src/__init__.py", "src/utils/__init__.py",
            "src/libs/alpha.py", "src/tests/beta.py",
            "src/entities/gama.py", "src/assets/template.py"
        ],
        "all_dirs": ["src", "src/utils", "src/libs", "src/tests", "src/entities", "src/assets"],        
    }
    expected_out =  f"Found 6 files and 6 directories\nFirst 5 files: ['src/__init__.py', 'src/utils/__init__.py', 'src/libs/alpha.py', 'src/tests/beta.py', 'src/entities/gama.py']\nFirst 5 directories: ['src', 'src/utils', 'src/libs', 'src/tests', 'src/entities']\n"
    show_preview(context)
    captured = capsys.readouterr()
    assert captured.out == expected_out
