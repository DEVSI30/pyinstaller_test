import sys
from datetime import datetime


# 단일 EXE 생성 옵션으로 빌드 한다. --OneFile -F
# 프로젝트 폴더 위치를 반환한다.
def get_absolute_project_path() -> str:
    return "\\".join(sys.argv[0].split("\\")[:-2]) + "\\"


def get_now_str() -> str:
    now: datetime = datetime.now()
    return f"{now.year}_{now.month}_{now.day}_{now.hour}_{now.minute}_{now.second}"
