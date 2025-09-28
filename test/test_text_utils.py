from book_processor.text_utils import read_book


def test_read_book(tmp_path):
    # Create a temporary text file
    sample_text = "Line 1\n\nLine 2\n\n\nLine 3"
    file_path = tmp_path / "sample.txt"
    file_path.write_text(sample_text, encoding="utf-8")

    # Read using the function
    result = read_book(file_path)

    # Expected: blank lines removed
    expected = "Line 1\nLine 2\nLine 3"

    assert result == expected
