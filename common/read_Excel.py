
"""读取表格的值"""
import xlrd
from xlrd import xldate_as_tuple
import datetime
# from configs.user_config import *
'''
xlrd中单元格的数据类型
数字一律按浮点型输出，日期输出成一串小数，布尔型输出0或1，所以我们必须在程序中做判断处理转换
成我们想要的数据类型
0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
'''

# 打开文件
# workbook=xlrd.open_workbook(r"E:\qitanrequest\data\qitan_data.xls")
# 读取文件内所有的表格
# sheet1=workbook.sheet_names()[0]#读取第一个表格

# sheet1_name=workbook.sheet_by_index(1)

# sheet1=workbook.sheet_by_name("user")#通过名字查找  /.sheet_by_index(3)通过索引,读取表格

# row1=sheet1.cell_value(0,0)
# row=sheet1.row_values(1)#第二行全部列
# col=sheet1.col_values(0)#第一列全部行/（0，6，10）取第1行，第6~10列（不含第10表）
# print(row1)
# print(row)
# # print(sheet1.row_types(1))
# print(sheet1.cell(1,1).ctype)#获取单元表格的类型
# print(sheet1.cell(1,2).ctype)

# print(sheet1)
class ExcelData():

    def __init__(self, data_path,sheet_name):
        # 文件的路径
        self.data_path = data_path
        # 工作表的名称
        self.sheet_name = sheet_name
        # 打开文件
        self.data=xlrd.open_workbook(self.data_path)
        # 获取表格
        self.table=self.data.sheet_by_name(self.sheet_name)
        # 字典的key就是excel表中每列第一行的字段
        self.keys=self.table.row_values(0)
        # 获取行总数
        self.rownum=self.table.nrows
        # 获取列总数
        self.colnum=self.table.ncols
    def ReadExcel(self):#遍历表格的所有单元格
        #定义一个空列表
        datas=[]
        for i in range(1,self.rownum):
            sheet_data={}
            for j in range(self.colnum):
                # 获取单元格的数据类型
                c_type=self.table.cell(i,j).ctype
                # 获取单元格的值
                c_value=self.table.cell_value(i,j)
                if c_type == 2 and c_value % 1 == 0:
                    c_value = int(c_value)
                elif c_type == 3:
                    # 转成datetime对象
                    date = datetime.datetime(*xldate_as_tuple(c_value,0))

                    c_value = date.strftime("%Y-%m-%d")
                elif c_type == 4:
                   if c_value == 1:
                       c_value = True
                   else:
                       False
                sheet_data[self.keys[j]]=c_value
            datas.append(sheet_data)# 再将字典追加到列表中
            return datas
            # 循环每一个有效的单元格，将字段与值对应存储到字典中
            # 字典的key就是excel表中每列第一行的字段
            # 再将字典追加到列表中

        #获取单元格的值，再判断类型
    def readExcel(self,i,j):

        # 获取单元格的数据类型
        c_type=self.table.cell(i,j).ctype
        # 获取单元格的值
        c_value =self.table.cell_value(i,j)
        if c_type==2 and c_value % 1 == 0:
            c_value=int(c_value)
        elif c_type == 3:
            # 转成datetime对象
            # 1. xlrd.xldate_as_tuple(xldate,datemode)1. xlrd.xldate_as_tuple(xldate,datemode)参数
            # datemode:时间基准（0代表1900-01-01为基准，1代表1904-01-01为基准）；常使用1900为基准
            # 返回值：返回一个元组，类似于（year, month, day, hour, minute, nearest_second）
            # 但是，仅适用于date类型的excel单元格，不适用于time类型的单元格
            # 对于time类型的单元格值，报错：XLDateAmbiguous
            date = datetime.datetime(*xldate_as_tuple(c_value,0))
            c_value = date.strftime("%Y-%m-%d")
        elif c_type==4:
            c_cell = True if c_value == 1 else False
        # sheet_data[self.keys[j]]=c_value
    # datas.append(sheet_data)# 再将字典追加到列表中
    # return datas
    # 循环每一个有效的单元格，将字段与值对应存储到字典中
    # 字典的key就是excel表中每列第一行的字段
    # 再将字典追加到列表中
        return c_value



if __name__=="__main__":
    data_path=r"E:\qitan1.3API\data\test_api.xlsx"
    sheet_name="test_case"
    get_data=ExcelData(data_path,sheet_name)
    datas=get_data.ReadExcel()
    unit_data=get_data.readExcel(1,0)
    print(datas)
    print(unit_data)
