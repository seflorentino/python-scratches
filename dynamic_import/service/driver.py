import os
import time
import importlib
import subprocess
import sys


def main():
    while True:
        result = subprocess.run([sys.executable, "-m", "dynamic_import.imported"])
        print(result)
        time.sleep(5)


if __name__ == "__main__":
    main()
