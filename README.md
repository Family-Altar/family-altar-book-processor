family-altar-book-processor

Python project for processing and structuring Family Altar books into chapters/sections.

## Folder Structure

```text
family-altar-book-processor/
├── book_processor/           # Python package for processing scripts
│   ├── __init__.py           # Makes this folder a package
│   ├── chapter_extractor.py  # Scripts to split books into chapters
│   └── text_utils.py         # Helper functions for text processing
├── test-notebooks/           # Test notebooks for experimenting
├── processed_books/          # Output folder for processed text files
├── main.py                   # Main entry point for processing
├── requirements.txt          # Python dependencies
├── setup.cfg                 # Linting and formatting config (flake8, isort, pytest)
├── pyproject.toml            # Black code formatter and build system config
└── .gitignore                # Files/folders to ignore in Git
```


Setup

Windows

python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py

macOS

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py

> Running main.py will execute the processing workflow, reading input text files and producing structured output in processed_books/.

---

GitHub Repository Guidelines

- Branch Naming Pattern: Feature branches should follow feature/<name>; bugfix branches bugfix/<name>.
- Status Checks: Linting and unit tests must pass before merging to main.
- Required Reviews: At least one code review approval required.
- CI/CD: GitHub Actions runs linting, formatting, and unit tests automatically on pull requests.

---

Linting & Formatting

setup.cfg

- Flake8 checks Python code style:
  - max-line-length = 88
  - Ignores E203, W503
  - Excludes .git, __pycache__, build, dist, .venv, venv, processed_books, test-notebooks

- Isort sorts imports and is Black-compatible:
  - profile = black
  - line_length = 88
  - known_first_party = book_processor
  - Skips .venv, venv, processed_books, test-notebooks

- Pytest ignores test-notebooks if desired:
  - norecursedirs = processed_books test-notebooks

pyproject.toml

[tool.black]
line-length = 88
target-version = ["py39"]
skip-string-normalization = false

[tool.isort]
profile = "black"
line_length = 88
known_first_party = ["book_processor"]
multi_line_output = 3
include_trailing_comma = true

[build-system]
requires = ["setuptools>=42", "wheel"]
build-backend = "setuptools.build_meta"

> This ensures consistent code formatting, import ordering, and makes the project installable.

---

Usage

1. Put txt location in main.py.
2. Run main.py.
3. Structured output will appear in processed_books/. (not setup yet , setup in test-notebook)
4. Test and experiment using test-notebooks/.

---

Notes

- processed_books/ folder exists in Git but all files inside are ignored in Git (.gitignore).
- test-notebooks/ can be used for quick tests and experiments; they are committed to the repo.
- test-notebooks/processed_books/ folder exists in Git but all files inside are ignored in Git (.gitignore).
- The project is designed for separation of concerns: book_processor/ wilol contain all reusable processing functions.
