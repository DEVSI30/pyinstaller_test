import os

from file_generator import simple_file_generator
from file_generator import excel_file_generator

if __name__ == '__main__':
    # simple_file_generator.make_txt_file()
    TEST = False
    print(f"[output$file_path]:{excel_file_generator.excel_img(TEST)}")

    os.system("pause")
