import xlrd
class A:
    def __init__(self):
        self.COLS = {
            'distance': 3,
            'last_name': 4,
            'name': 5,
            'birth_date': 7,
            'gender': 8,
            'country': 11,
            'mobile_phone': 18,
            'email': 20,
            'register_date': 36,
            'pay_status': 37
        }


    def parse_xls(self, file_name):
        data = []
        wb = xlrd.open_workbook(file_name)
        sheet = wb.sheet_by_index(0)

        for row in range(2, sheet.nrows):
            recipient_data = {}
            for key, col_num in self.COLS.items():
                value = sheet.cell_value(row, col_num - 1)
                recipient_data[key] = value if value else ''

            data.append(recipient_data)
        print(data[0])
        return data

