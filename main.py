import os

TEXT = "My obstacle sensors say the path is clear, but my pathfinding keeps routing me straight to you."

def validated_text():
    text = TEXT
    text.encode("utf-8")
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text.strip(), "entry must not be only whitespace"
    return text

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = (validated_text() + "\n").encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    # Re-read the written bytes and prove they are exactly what was validated.
    with open(path, "rb") as f:
        assert f.read() == data, "written bytes differ from validated text"

if __name__ == "__main__":
    main()
