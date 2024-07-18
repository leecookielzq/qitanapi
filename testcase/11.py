from datetime import datetime,date
from  random import randint
print(randint(0,1))
# def web_endDate():
#     current_date = datetime.now()
#     # 提取当前的年份和月份
#     current_year = current_date.year
#     current_month = current_date.month
#     # 计算输出的年份
#     if current_month > 5:
#         return date(current_year - 1, 12, 31)
#     else:
#         return date(current_year-2, 12, 31)
# print(web_endDate())
#
# from datetime import datetime, timedelta
#111
# def get_custom_date():
#     current_date = datetime.now()
#     current_year = current_date.year
#     current_month = current_date.month
#
#     if current_month > 5:
#         # 如果当前月份大于 5 月份，则返回当前年份 - 1 年的 12 月 31 日
#         return str(datetime(current_year - 1, 12, 31))
#     else:
#         # 否则返回当前年份 - 2 年的 12 月 31 日
#         return str(datetime(current_year - 2, 12, 31))
#
# custom_date = get_custom_date()
# print(custom_date.current_year)
# def web_year():
    # current_date = datetime.now()
    # 提取当前的年份和月份
    # current_year = current_date.year
    # current_month = current_date.month
    # 计算输出的年份
    # if current_month >= 5:
        # web_year_value = current_year -1
    # else:
    #     web_year_value = current_year - 2

    # return web_year_value,current_year,curre    nt_month
# print(web_year())
def shu(input_dict):
    dist_1={"数字":"num","中文":"chinese","英文":"english"}
    tuple_1=()
    # for key,value in dist_1.items():
    #     print(f"{key}:{value}")
    for value in dist_1.values():
            tuple_1+=(value,)
            # print(tuple_1)
    tuple_2=()
    for value_2 in input_dict.value:

            tuple_2+=(value_2,)
            # print(tuple_2)
    output_dict=dict(zip(tuple_1,tuple_2))
    print(output_dict)
    # return output_dict

shu({"数字":1,"中文":2,"英文":3})