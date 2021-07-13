import os
from smart_open import open


def run_me(options):
    with open(options["unc_path"]) as f:
        for line in f:
            print(line)


if __name__ == "__main__":
    opts = {"unc_path": os.getenv("UNC_PATH")}
    run_me(opts)
