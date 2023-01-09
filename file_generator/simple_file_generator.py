from .file_path_util import get_absolute_project_path, get_now_str
import os


def make_txt_file():
    file_name = get_now_str()
    file_path = get_absolute_project_path() + "output\\"
    file_ext = "txt"

    if os.path.exists(file_path):
        with open(f"{file_path}{file_name}.{file_ext}", "w", encoding="UTF-8") as f:
            f.write("Hello")

        f.close()

