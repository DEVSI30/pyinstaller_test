from .file_path_util import get_absolute_project_path, get_now_str
import matplotlib.pyplot as plt
import pandas as pd
import io

def create_excel_file(test_option):
    file_name = get_now_str()
    file_path = "./output/" if test_option else get_absolute_project_path() + "output\\"
    file_ext = "xlsx"
    #
    # # 엑셀파일 쓰기
    # write_wb = Workbook()
    #
    # # 이름이 있는 시트를 생성
    # write_ws = write_wb.create_sheet('생성시트')
    #
    # # Sheet1에다 입력
    # write_ws = write_wb.active
    # write_ws['A1'] = '숫자'
    #
    # # 행 단위로 추가
    # write_ws.append([1, 2, 3])
    #
    # # 셀 단위로 추가
    # write_ws.cell(5, 5, '5행5열')
    # write_wb.save(f"{file_path}{file_name}.{file_ext}")


def excel_img(test_option):
    file_name = get_now_str()
    file_path = "./output/" if test_option else get_absolute_project_path() + "output\\"
    file_ext = "xlsx"
    save_path = f"{file_path}{file_name}.{file_ext}"

    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    fig = plt.figure()
    plt.plot(x, y)
    plt.title(' in memory')
    writer = pd.ExcelWriter(f"{file_path}{file_name}.{file_ext}", engine='xlsxwriter')

    pd.DataFrame({'a': [1, 2, 3, 4]}).to_excel(writer, sheet_name="Sheet1")  # write some random data

    # 그냥 이미지 저장할까..

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    worksheet = writer.sheets['Sheet1']
    worksheet.insert_image('C2', 'a', options={'image_data': buf})  # 'a' is the name of the image which doesn't matter

    buf2 = io.BytesIO()
    plt.clf()
    plt.title('In memory2')
    plt.plot(y, x)
    plt.savefig(buf2, format='png')
    worksheet.insert_image('C27', 'b', options={'image_data': buf2})

    buf3 = io.BytesIO()
    plt.clf()
    plt.title('hangul no')
    plt.plot(y, x)
    plt.savefig(buf3, format='png')
    worksheet.insert_image('C52', 'b',
                           options={'image_data': buf3})
    writer.save()

    buf.close()
    buf2.close()
    buf3.close()

    return save_path




