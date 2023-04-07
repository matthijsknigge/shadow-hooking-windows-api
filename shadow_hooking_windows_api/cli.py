"""Console script for shadow_hooking_windows_api."""
import argparse
import sys


def main():
    """Console script for shadow_hooking_windows_api."""
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()

    print("Arguments: " + str(args._))
    print("Replace this message by putting your code into "
          "shadow_hooking_windows_api.cli.main")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
