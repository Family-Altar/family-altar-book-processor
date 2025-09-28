# main.py

from pathlib import Path

from book_processor.text_utils import clean_text, find_family_altar_lines, read_book


def main():
    book_file = Path(r"put file path here for testing")

    if not book_file.exists():
        print(f"Book file not found: {book_file}")
        return

    text = read_book(book_file)
    text = clean_text(text)
    print(text[:1000])
    altar_lines = find_family_altar_lines(text)

    print(f"Number of 'Day' lines found: {len(altar_lines)}")


if __name__ == "__main__":
    main()
