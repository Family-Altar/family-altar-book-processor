from pathlib import Path

import chardet


def read_book(file_path: Path) -> str:
    """Read the book text into a string, auto-detecting encoding"""
    raw_data = file_path.read_bytes()
    result = chardet.detect(raw_data)
    encoding = result["encoding"]
    confidence = result["confidence"]
    print(f"Detected encoding: {encoding} (confidence: {confidence:.2f})")
    text = raw_data.decode(encoding).strip()
    # Remove extra blank lines
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return "\n".join(lines)
