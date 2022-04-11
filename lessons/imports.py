"""Examples of importing Python."""

# Alias a module / imported name as another name

from lessons import helpers as hp

# Import names defined gobally in a module
from lessons.helpers import powerful


def main() -> None:
    """Entrypoint of program."""
    print(hp.powerful(2, 4))
    print(powerful(2, 3))


if __name__ == "__main__":
    main()