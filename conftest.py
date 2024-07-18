import pytest
from yaml_util import YamlUtil
import logging,os,time
from datetime import datetime,date
@pytest.fixture(scope='session',autouse=True)  #只作用于会话
def clear_yaml():#清除yaml 文件
    YamlUtil().clear_extract_yaml()

'''前端控制年份如果当前月大于5月份则当前年份-1，否则-2'''
@pytest.fixture(scope='session',autouse=True)
def web_year():
    current_date = datetime.now()
    # 提取当前的年份和月份
    current_year = current_date.year
    current_month = current_date.month
    # 计算输出的年份
    if current_month >= 5:
        web_year_value = current_year -1
    else:
        web_year_value = current_year - 2

    return web_year_value

'''前端控制的日期'''
@pytest.fixture(scope='session',autouse=True)
def web_endDate():
    current_date = datetime.now()
    # 提取当前的年份和月份
    current_year = current_date.year
    current_month = current_date.month
    # 计算输出的年份
    if current_month >= 5:
        return str(date(current_year - 1, 12, 31))
    else:
        return str(date(current_year - 2, 12, 31))

'''后端控制年份如果当前月大于5月份则当前年份-1，否则-2'''
@pytest.fixture(scope='session',autouse=True)
def Java_year():
    current_date = datetime.now()
    # 提取当前的年份和月份
    current_year = current_date.year
    current_month = current_date.month
    # 计算输出的年份
    if current_month >= 5:
        java_year_value = current_year -1
    else:
        java_year_value = current_year - 2

    return java_year_value

'''后端端控制的日期'''
@pytest.fixture(scope='session',autouse=True)
def java_endDate():
    current_date = datetime.now()
    # 提取当前的年份和月份
    current_year = current_date.year
    current_month = current_date.month
    # 计算输出的年份
    if current_month >= 5:
        return str(date(current_year - 1, 12, 31))
    else:
        return str(date(current_year - 2, 12, 31))


# def pytest_addoption(parser):
#     parser.addoption(
#         "--cmdopt",
#         action="store",
#         default="type1",
#         help="my option: type1 or type2",
#         choices=("type1", "type2"),
#     )
#
# class Logger:
#     def __init__(self,stdout_format='%(asctime)s - %(levelname)s - %(message)s',log_name=time.strftime('%Y-%m-%d', time.localtime()) + '.log',log_level=logging.INFO):
#         self.stdout_format = stdout_format
#         self.log_name = log_name
#         self.log_level=log_level
#         self.log_path=os.path.join(os.path.abspath(".."), "logs")
#     def  create_logger(self):
#         '''日志输出格式'''
#         formatter=logging.Formatter(self.stdout_format)
#         #定义终端输出
#         console_handler = logging.StreamHandler()
#         console_handler.setFormatter(formatter)
#         # 定义日志文件输出
#         file_handler = logging.FileHandler(os.path.join(self.log_path, self.log_name), encoding='utf-8')
#         file_handler.setFormatter(formatter)
#         # 创建日志输出的位置及日志级别
#         logger = logging.getLogger()
#         logger.addHandler(console_handler)
#         logger.addHandler(file_handler)
#         logger.setLevel(self.log_level)
#
#         return logger
#
# @pytest.fixture(scope='session', autouse=True)
# def setup_and_teardown():
#     # 在测试会话开始前创建日志记录器
#     logger_instance = Logger()
#     logger_instance.create_logger()
#     yield
#
#
# print(os.path.join(os.path.abspath("."), "logs"))


# current_date = datetime.now()
# # 提取当前的年份和月份
# current_year = current_date.year
# current_month = current_date.month
# # 计算输出的年份
# if current_month > 5:
#     web_year = current_year - 1
# else:
#     web_year = current_year - 2