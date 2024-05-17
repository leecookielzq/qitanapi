import os, yaml
# print(os.getcwd())#获取当前文件的路径
#os.path.abspath("..")获取上一级目录
# print(os.path.abspath('..') + "\\testcase\\" + 'login.yml')
class YamlUtil:
    def read_extract_yaml(self, key):#读取yaml 文件
        with open(os.path.abspath("..") + "\extract.yml", mode='r', encoding='utf-8') as f:
            value=yaml.load(stream=f,Loader=yaml.FullLoader)
            return value[key]
    def write_extract_yaml(self,data):#写入yaml文件
        with open(os.path.abspath("..") + "\extract.yml", mode='a', encoding='utf-8') as f:
            yaml.dump(data=data,stream=f,allow_unicode=True)#将python字典转成 json，序列化写进extract
        # print(os.path.abspath("..") + "\extract.yml")

    # 清空文件的内容
    def clear_extract_yaml(self):
        with open(os.path.abspath("..") + "\extract.yml", mode='w', encoding='utf-8') as f:
            f.truncate()

    #读取用例的yaml文件
    def read_testcase_yaml(self,yaml_name):
        # work = os.path.abspath('..') + "\\testcase\\" + yaml_name
        # print(os.path.abspath("..") + "\extract.yml")
        # print(work)
        with open(os.path.abspath('..') + "\\testcase\\" + yaml_name, mode='r', encoding='utf-8') as f:
            value=yaml.load(stream=f, Loader=yaml.FullLoader)# 转成字典格式， #加上Loader=yaml.FullLoader 避免警告
            # print(value)
            return value

     #读取数据库配置信息yaml
    def read_data_yaml(self,key):
        with open(os.path.abspath("..")+"\configs\database_configs.yml", mode='r', encoding="utf-8") as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value[key]

if __name__=='__main__':
    YamlUtil().read_testcase_yaml('login.yml')
    print(YamlUtil().read_extract_yaml('org_code'))
    # print(YamlUtil().read_testcase_yaml('decoding_updateCsfHtml.yml'))
    # YamlUtil().read_testcase_yaml('ex.yml')

    # YamlUtil().clear_extract_yaml()
    # print(YamlUtil().read_data_yaml('host'))

