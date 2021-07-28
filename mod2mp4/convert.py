import os
import pathlib
import subprocess

def main():
    files = os.listdir(".")

    for f in files:
        if not f.endswith(".MOD"):
            continue
        out_name = f.replace(".MOD", "") + ".mp4"

        subprocess.run(["ffmpeg", "-i", f, "-c:v", "libx264", out_name])

        ff = pathlib.Path(f)
        os.utime(out_name, (ff.stat().st_atime, ff.stat().st_mtime))

if __name__ == "__main__":
    main()

