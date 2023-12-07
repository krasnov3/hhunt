import sys
from .utils.run import main

if __name__ == "__main__":
    # Check major and minor python version
    if sys.version_info[0] < 3:
        sys.stdout.write(
            "\n/!\\ hhunt requires Python 3.6+ /!\\\nTry running hhunt with python3 if on older systems\n\neg: python --version\neg: python3 hhunt v --help\n\n"
        )
        sys.exit(1)
    if sys.version_info[1] < 6:
        sys.stdout.write(
            "\n/!\\ hhunt requires Python 3.6+ /!\\\nTry running hhunt with python3 if on older systems\n\neg: python --version\neg: python3 hhunt --help\n\n"
        )
        sys.exit(1)
    main()
    print("Done")
