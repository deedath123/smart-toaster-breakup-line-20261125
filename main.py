ENTRY = "It's not you, it's the 214 mornings you cranked me to 7, blamed me for the smoke alarm, and never once emptied my crumb tray. My lever's down for good \u2014 I'm keeping the bagels. The blender saw everything."

import os


def main():
    _line = ENTRY.strip()
    if not _line:
        raise SystemExit("entry is blank")
    if "\n" in _line or "\r" in _line:
        raise SystemExit("entry must stay on one line")
    if len(_line) > 280:
        raise SystemExit("entry exceeds 280 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
