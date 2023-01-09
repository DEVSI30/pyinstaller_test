from datetime import datetime
import os, sys


def make_txt_file():
    now = datetime.now()

    file_name = f"{now.year}_{now.month}_{now.day}_{now.hour}_{now.minute}_{now.second}"
    file_path = "\\".join(sys.argv[0].split("\\")[:-2]) + "\\output\\"
    file_ext = "txt"

    if os.path.exists(file_path):
        with open(f"{file_path}{file_name}.{file_ext}", "w", encoding="UTF-8") as f:
            f.write("Hello")

        f.close()