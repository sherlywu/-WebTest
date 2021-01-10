"""
文件处理类，实现文件的读写操作
"""

from openpyxl import Workbook, load_workbook
import os

class FileHandler:
    def __init__(self):
        self.data_path = os.path.join(os.path.dirname(__file__), '../test_data')

    def read_excel_by_sheet(self, excel_path, sheet_name):
        """
        读取excel文件
        :param excel_path: excel文件名
        :param sheet_name: worksheet 工作表名
        :return:
        """
        excel_file = os.path.join(self.data_path, excel_path)
        wb = load_workbook(filename=excel_file)
        ws = wb[sheet_name]
        test_data = []
        values = ws.values
        next(values)  # 去掉第一行
        for row in values:
            test_data.append(row)
        return test_data

    def read_csv_file(self, csv_path):
        pass

if __name__ == '__main__':
    fl = FileHandler()
    data = fl.read_excel_by_sheet('datadriven.xlsx', '登录')
    print(data)