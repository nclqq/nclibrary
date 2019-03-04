import xlrd
from framework.logger import Logger

logger=Logger(logger="Utils").getlog()

class Utils:

    @classmethod
    def read_excel(self,excel_path,sheet_name="sheet1"):
        workbook=xlrd.open_workbook(excel_path)
        sheet=workbook.sheet_by_name(sheet_name)

        #将第一行的作为key值
        keys=sheet.row_values(0)
        #获取总行数
        rowNum=sheet.nrows
        #获取总列数
        cloNum=sheet.ncols

        #循环获取值
        if rowNum<=1:
            logger.error("表格中数据小于1")
        else:
            r=[]
            for i in range(1,rowNum): #先循环行，从第二行开始
                sheet_data={}
                values=sheet.row_values(i)
                for j in range(cloNum): #只有一列
                    sheet_data[keys[j]]=values[j]  #第一行的第一列=第二行的第一列，第三行的第一列，第四行的第一列
                r.append(sheet_data)
            return r


if __name__=="__main__":
    print(Utils.read_excel("E:/Discuz/data/data_excel.xlsx","Sheet1"))