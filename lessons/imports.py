"""ex of imp"""

from lessons import helpers


def main() -> None:
    """stop it."""
    print(helpers.powerful(2, 4))
    print(f"imports.py: {__name__}")


if __name__ == "__main__":
    main()