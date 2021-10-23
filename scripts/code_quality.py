import os


def check_import_order():
    os.system("isort --check ./brsus/ --skip __init__.py --gitignore --dont-follow-links --verbose")


def check_code_formatting():
    os.system("black --check ./brsus/ --exclude __init__.py --verbose")


def sort_import_order():
    os.system("isort ./brsus/ ./tests/ --skip __init__.py --gitignore --dont-follow-links --verbose")


def do_code_formatting():
    os.system("black ./brsus/ ./tests/ --exclude __init__.py --verbose")


def linter():
    os.system("pylama ./brsus/ ./tests/")


def run_tests():
    os.system("pytest ./tests/ --verbose --color=yes --code-highlight=yes")
