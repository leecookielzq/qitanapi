import allure,os,pytest,random,yaml
import requests
import allure,os,pytest,random
from datetime import datetime
from common.yaml_util import YamlUtil
# from common.read_Excel import ExcelData
from config.env_config import *
from common.request_util import Request
# import json,logging
# from common.connect_sql import ConnectSql
# from time import *

class TestQitanApi:

    @allure.feature('登录模块')
    @allure.title("登录")
    @pytest.mark.parametrize('caseinfo',YamlUtil().read_testcase_yaml('login.yml'))
    def test_alogin(self,caseinfo):
        url=test_host+caseinfo['request']['url']
        method=caseinfo['request']['method']
        data=caseinfo['request']['data']
        header=caseinfo['request']['header']
        result=Request().send_request(url=url,method=method,header=header,data=data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
        # restult = requests.session(url,method,header,data)
        # requests.post()
        # print(restult)
        if result['code'] == 200:
            YamlUtil().write_extract_yaml({'token': result['data']['token']})
            YamlUtil().write_extract_yaml({'companyCode': '79'})
            YamlUtil().write_extract_yaml({'companyCode_1': '79580'})
            YamlUtil().write_extract_yaml({'java_endDate': '2023-12-31'})#后端控制的年份
            YamlUtil().write_extract_yaml({'java_year': 2023})  # 后端控制的年份
            assert result['code' ]== 200,'登录失败'
        elif result['code'] == 300002 :
            assert result['code'] == 300002,'登录成功'
        else:
            pass


    @allure.feature('登录模块')
    @allure.title("获取用户信息")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('companyhomepage_currentUser.yml'))
    def test_currentuser(self, caseinfo):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        result = Request().send_request(url, method, header)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
        YamlUtil().write_extract_yaml({"userId": result['data']['userId']})


    @allure.feature('登录模块')
    @allure.title("获取用户角色")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('companyhomepage_user_Rolequery.yml'))
    def test_queryuser(self, caseinfo):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data={}
        data['userId']=YamlUtil().read_extract_yaml('userId')
        result = Request().send_request(url, method, header,data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
        YamlUtil().write_extract_yaml({'userType':result['data']['userType']})
        if result['data']['userType'] == 1:
            YamlUtil().write_extract_yaml({'role': '战略决策者'})
        elif result['data']['userType'] == 2:
            YamlUtil().write_extract_yaml({'role': '战略规划者'})
        elif result['data']['userType'] == 3:
            YamlUtil().write_extract_yaml({'role': '销售管理者'})
        elif result['data']['userType'] == 4:
            YamlUtil().write_extract_yaml({'role': '咨询顾问'})
        else:
            pass


    @allure.feature('企业主页')
    @allure.title("公司诊断搜索")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('companyhomepage_DiagnosisSearch.yml'))
    def test_companyDiagnosisSearch(self, caseinfo):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        result = Request().send_request(url, method, header)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)

    @allure.feature('企业主页')
    @allure.title("公司nlg")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('General_getNlgShort.yml'))
    def test_getNlgShort(self, caseinfo):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data=caseinfo['request']['data']
        result = Request().send_request(url, method, header,data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)

    @allure.feature('企业主页')
    @allure.title("小程序公司nlg")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('companyhomepage_miniNlg.yml'))
    def test_miniNlg(self, caseinfo):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['orgCode'] = YamlUtil().read_extract_yaml('companyCode')
        result = Request().send_request(url, method, header, data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
    @allure.feature('企业主页')
    @allure.title("公司信息")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('companyhomepage_companyInfo.yml'))
    def test_companyInfo(self, caseinfo):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['mainCompanyCode']=YamlUtil().read_extract_yaml('companyCode')
        result = Request().send_request(url, method, header, data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
        print(result)


    @allure.feature('企业主页')
    @allure.title("公司相关产业链")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('companyhomepage_findCompanyChains.yml'))
    def test_findCompanyChains(self, caseinfo):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['orgCode'] = YamlUtil().read_extract_yaml('companyCode')
        result = Request().send_request(url, method, header, data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
        # print(result)

    @allure.feature('企业主页')
    @allure.title("公司变革数据")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('companyhomepage_biange.yml'))
    def test_companybiange(self, caseinfo):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['orgCode'] = YamlUtil().read_extract_yaml('companyCode')
        data['roleName'] = YamlUtil().read_extract_yaml('role')
        result = Request().send_request(url, method, header, data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
    #     # print(result)

    @allure.feature('企业主页')
    @allure.title("企业行业")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('companyhomepage_companyIndustryCode.yml'))
    def test_selectIndustryByCode(self, caseinfo):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['orgCode'] = YamlUtil().read_extract_yaml('companyCode')
        result = Request().send_request(url, method, header, data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
    #     # print(result)

    @allure.feature('企业主页')
    @allure.title("主营构成")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('companyhomepage_mainBusinessComposition.yml'))
    def test_mainBusinessComposition(self, caseinfo):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['orgCode'] = YamlUtil().read_extract_yaml('companyCode')
        result = Request().send_request(url, method, header, data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
    #     # print(result)

    @allure.feature('企业主页')
    @allure.title("公司的营收年份")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('companyhomepage_compangyRevenueYear.yml'))
    def test_getDateList(self, caseinfo):
        url = test_host + caseinfo['request']['url']+YamlUtil().read_extract_yaml('companyCode')
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        result = Request().send_request(url, method,header)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
        # print(result)

    '''
    @allure.feature('管理熵')
    @allure.title("管理熵nlg")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('ManageEntropy_getCompMsComment.yml'))
    def test_getCompMsComment(self, caseinfo):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['orgCode'] = YamlUtil().read_extract_yaml('companyCode')
        result = Request().send_request(url, method, header, data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
    @allure.feature('管理熵')
    @allure.title("最新年份数据、二级行业的数据")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('ManageEntropy_getEntropyPoint.yml'))
    def test_getEntropyPoint(self, caseinfo,web_endDate):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['orgCode'] = YamlUtil().read_extract_yaml('companyCode')
        data['endDate']=web_endDate
        result = Request().send_request(url, method, header, data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
        print(result)

    @allure.feature('管理熵')
    @allure.title("管理熵核心评价维度对比")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('ManageEntropy_coreMS7.yml'))
    def test_coreMS7(self, caseinfo,web_endDate):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['orgCode'] = YamlUtil().read_extract_yaml('companyCode')
        data['endDate'] = web_endDate
        result = Request().send_request(url, method, header, data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
        print(result)

    @allure.feature('管理熵')
    @allure.title("管理熵的排名")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('ManageEntropy_getEntropyPointIndex.yml'))
    def test_getEntropyPointIndex(self, caseinfo):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['orgCode'] = YamlUtil().read_extract_yaml('companyCode')
        result = Request().send_request(url, method, header, data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
        print(result)

    @allure.feature('管理熵')
    @allure.title("管理熵的行业熵流")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('ManageEntropy_industryflow.yml'))
    def test_busSystemManagerEntropy(self, caseinfo):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['orgCode'] = YamlUtil().read_extract_yaml('companyCode')
        result = Request().send_request(url, method, header, data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
        print(result)
    @allure.feature('管理熵')
    @allure.title("单项经营能力熵值分析")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('ManageEntropy_industryMsConfig.yml'))
    def test_industryMsConfig(self, caseinfo,web_endDate):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['orgCode'] = YamlUtil().read_extract_yaml('companyCode')
        data['endDate'] = web_endDate
        result = Request().send_request(url, method, header, data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
        print(result)

    @allure.feature('管理熵')
    @allure.title("核心财务数据")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('ManageEntropy_coreFinData.yml'))
    def test_coreFinData(self, caseinfo):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['orgCode'] = YamlUtil().read_extract_yaml('companyCode')
        data['endDate'] = '2023-12-31'
        result = Request().send_request(url, method, header, data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
        print(result)

    @allure.feature('管理熵')
    @allure.title("范式成长画像")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('ManageEntropy_getByIndicator.yml'))
    def test_getByIndicator(self, caseinfo):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        result = Request().send_request(url, method, header, data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
        print(result)

    @allure.feature('管理熵')
    @allure.title("公司范式阶段")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('ManageEntropy_groupData.yml'))
    def test_groupData(self, caseinfo,web_endDate):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['orgCode'] = YamlUtil().read_extract_yaml('companyCode')
        data['endDate'] = web_endDate
        result = Request().send_request(url, method, header, data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
        print(result)

    @allure.feature('管理熵')
    @allure.title("公司行业信息")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('companyhomepage_CompanyIndustryData.yml'))
    def test_queryCompanyIndustryData(self, caseinfo):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['companyCode'] = YamlUtil().read_extract_yaml('companyCode')
        result = Request().send_request(url, method, header, data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)


    @allure.feature('管理熵')
    @allure.title("猜你想看列表")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('ManageEntropy_getIndustryCompanyRecommend.yml'))
    def test_getIndustryCompanyRecommend(self, caseinfo):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['companyCode'] = YamlUtil().read_extract_yaml('companyCode')
        data['userId'] = YamlUtil().read_extract_yaml('userId')
        result = Request().send_request(url, method, header, data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
        YamlUtil().write_extract_yaml({'companyCodeList': result['data']['guessyoulike'][:4]}) #切片取前面四个
        print(result)


    @allure.feature('管理熵')
    @allure.title("猜你想看")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('ManageEntropy_getCompanyEfficiencyOther.yml'))
    def test_getCompanyEfficiencyOther(self, caseinfo):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['companyCodeList']=YamlUtil().read_extract_yaml('companyCodeList')
        result = Request().send_request(url, method, header, data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
        print(result)
    @allure.feature('管理熵诊断详情')
    @allure.title("生成报告")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('createReport.yml'))
    def test_createReport(self, caseinfo):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['companyCode'] = YamlUtil().read_extract_yaml('companyCode')
        data['userId'] = YamlUtil().read_extract_yaml('userId')
        data['year'] = YamlUtil().read_extract_yaml('java_year')
        result = Request().send_request(url, method, header, data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
        print(result)
        

    @allure.feature('管理熵对比页')
    @allure.title("查询公司名称及简称")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('companyhomepage_CompanyName.yml'))
    def test_queryCompanyName(self, caseinfo):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['companyCodeList'] = YamlUtil().read_extract_yaml('companyCodeList')
        result = Request().send_request(url, method, header, data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
        print(result)

    @allure.feature('管理熵对比页')
    @allure.title("对比公司管理熵排名和值")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('ManageEntropy_compare_getEntropyPoint.yml'))
    def test_comparegetEntropyPoint(self, caseinfo):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['orgCodes'] = YamlUtil().read_extract_yaml('companyCodeList')
        data['endDate'] = YamlUtil().read_extract_yaml('java_endDate')
        result = Request().send_request(url, method, header, data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
        print(result)

    @allure.feature('管理熵对比页')
    @allure.title("管理熵核心评价维度对比")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('ManageEntropy_compare_coreMS7.yml'))
    def test_comparecoreMS7(self, caseinfo):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['orgCodes'] = YamlUtil().read_extract_yaml('companyCodeList')
        data['endDate'] = YamlUtil().read_extract_yaml('java_endDate')
        result = Request().send_request(url, method, header, data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
        print(result)


    @allure.feature('管理熵对比页')
    @allure.title("经营系统管理熵")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('ManageEntropy_Compare_BusSystemManagerEntropy.yml'))
    def test_comparebusSystemManagerEntropy(self, caseinfo):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['orgCodes'] = YamlUtil().read_extract_yaml('companyCodeList')
        data['endDate'] = YamlUtil().read_extract_yaml('java_endDate')
        result = Request().send_request(url, method, header, data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
        print(result)

    @allure.feature('管理熵对比页')
    @allure.title("熵流分析")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('ManageEntropy_compare_innerOuter.yml'))
    def test_compareinnerOuter(self, caseinfo):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['orgCodes'] = YamlUtil().read_extract_yaml('companyCodeList')
        data['endDate'] = YamlUtil().read_extract_yaml('java_endDate')
        result = Request().send_request(url, method, header, data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
        print(result)


    @allure.feature('管理熵对比页')
    @allure.title("企业经营系统管理熵评价系统")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('ManageEntropy_compare_industryMsConfig.yml'))
    def test_compareindustryMsConfig(self, caseinfo):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['orgCodes'] = YamlUtil().read_extract_yaml('companyCodeList')
        data['endDate'] = YamlUtil().read_extract_yaml('java_endDate')
        result = Request().send_request(url, method, header, data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)

    @allure.feature('管理熵对比页')
    @allure.title("企业核心财务数据")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('ManageEntropy_compare_coreFinData.yml'))
    def test_comparecoreFinData(self, caseinfo):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['orgCodes'] = YamlUtil().read_extract_yaml('companyCodeList')
        data['endDate'] = YamlUtil().read_extract_yaml('java_endDate')
        result = Request().send_request(url, method, header, data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
        print(result)



    @allure.feature('经营诊断详情')
    @allure.title("经营诊断详情")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('GeneraLdetail.yml'))
    def test_getGeneral(self, caseinfo):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['companyCode'] = YamlUtil().read_extract_yaml('companyCode')
        data['year'] = YamlUtil().read_extract_yaml('java_year')
        result = Request().send_request(url, method, header, data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
        print(result)

    @allure.feature('经营诊断详情')
    @allure.title("经营诊断详情neo4j")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('general_selectNeo4jMap.yml'))
    def test_selectNeo4jMap(self, caseinfo):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['companyCode'] = YamlUtil().read_extract_yaml('companyCode')
        data['userId']=YamlUtil().read_extract_yaml('userId')
        data['year'] = YamlUtil().read_extract_yaml('java_year')
        result = Request().send_request(url, method, header, data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
        print(result)

    
    @allure.feature('经营诊断详情')
    @allure.title("经营诊断编辑页")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('General_edit.yml'))
    def test_getGeneral_pdf(self, caseinfo):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['companyCode'] = YamlUtil().read_extract_yaml('companyCode')
        data['userId'] = YamlUtil().read_extract_yaml('userId')
        data['year'] = YamlUtil().read_extract_yaml('java_year')
        result = Request().send_request(url, method, header, data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
        YamlUtil().write_extract_yaml({'generalId':result['data']['id']})
        print(result)

    @allure.feature('经营诊断详情')
    @allure.title("经营诊退出断编辑页")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('generalback.yml'))
    def test_generalback(self, caseinfo):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['generalId'] = YamlUtil().read_extract_yaml('generalId')
        data['userId'] = YamlUtil().read_extract_yaml('userId')
        result = Request().send_request(url, method, header, data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
        print(result)
    @allure.feature('经营诊断对比')
    @allure.title("经营诊断核心亮点")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('General_getNlgShort.yml'))
    def test_getNlgShort(self, caseinfo):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['orgCode'] = YamlUtil().read_extract_yaml('companyCode')
        data['year'] = YamlUtil().read_extract_yaml('java_year')
        result = Request().send_request(url, method, header, data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
        print(result)
        '''

    '''
    @allure.feature('专题诊断详情')
    @allure.title("专题诊断详情")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('specialgetGeneral.yml'))
    def test_specialgetGeneral(self, caseinfo):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['orgCode'] = YamlUtil().read_extract_yaml('companyCode')
        data['year'] = YamlUtil().read_extract_yaml('java_year')
        result = Request().send_request(url, method, header, data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
        print(result)

    @allure.feature('基线制定')
    @allure.title("基线制定")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('BaselineSetting.yml'))
    def test_getBaseListData(self, caseinfo):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['orgCode'] = YamlUtil().read_extract_yaml('companyCode')
        data['userId'] = YamlUtil().read_extract_yaml('userId')
        data['year'] = YamlUtil().read_extract_yaml('java_year')+1
        result = Request().send_request(url, method, header, data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
        print(result)

    @allure.feature('企业筛选')
    @allure.title("企业筛选病症")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('EnterpriseScreen_CharacterConfigAll.yml'))
    def test_selectCompCharacterConfigAll(self, caseinfo):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        result = Request().send_request(url, method, header)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
        YamlUtil().write_extract_yaml({'title':'病症筛选编码'})
        YamlUtil().write_extract_yaml({'character_code':result['data'][0]['character_code']})
        print(result)

    @allure.feature('企业筛选')
    @allure.title("获取行业")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('EnterpriseScreen_getIndustryAll.yml'))
    def test_getIndustryAll(self, caseinfo):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        result = Request().send_request(url, method, header)
        YamlUtil().write_extract_yaml({'title': '行业信息'})
        YamlUtil().write_extract_yaml({'industryCode':result['data'][26]['industryCode']})
        YamlUtil().write_extract_yaml({'industryName': result['data'][26]['industryName']})
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
        print(result)


    @allure.feature('企业筛选')
    @allure.title("企业筛选")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('EnterpriseScreen_CharacterSearch.yml'))
    def test_companyCharacterSearch(self, caseinfo,web_year):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data= caseinfo['request']['data']
        data['code']=YamlUtil().read_extract_yaml('character_code')
        data['endDate'] = web_year#调用fixture函数的返回值，而不调用函数的本身
        result = Request().send_request(url, method, header,data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
        print(data)
        print(result)
    @allure.feature('企业筛选')
    @allure.title("企业自定义筛选导出")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('filterexport2.yml'))
    def test_filterexport2(self, caseinfo, web_year):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['code'] = YamlUtil().read_extract_yaml('character_code')
        data['endDate'] = web_year  # 调用fixture函数的返回值，而不调用函数的本身
        result = requests.post(url=url, headers=header, json=data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
        print(data)
        print(result.text)

    @allure.feature('企业筛选')
    @allure.title("企业自定义筛选")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('EnterpriseScreen_findCompanyPage.yml'))
    def test_findCompanyPage(self, caseinfo):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['endDate'] =YamlUtil().read_extract_yaml('java_year')
        data['industryCode'] = YamlUtil().read_extract_yaml('industryCode')
        data['industryName'] = YamlUtil().read_extract_yaml('industryName')
        result = Request().send_request(url, method, header, data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
        print(data)
        print(result)

    @allure.feature('企业筛选')
    @allure.title("企业自定义筛选导出")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('filterexport.yml'))
    def test_filterexport(self, caseinfo):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['endDate'] = YamlUtil().read_extract_yaml('java_year')
        data['industryCode'] = YamlUtil().read_extract_yaml('industryCode')
        data['industryName'] = YamlUtil().read_extract_yaml('industryName')
        result = requests.post(url=url, headers=header,json=data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
        print(data)
        print(result.text)

    @allure.feature('行业分析')
    @allure.title("行业发展趋势")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('IndustryAnalysis_industryGrowthCompare.yml'))
    def test_industryGrowthCompare(self, caseinfo,web_endDate):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['endDate'] =web_endDate
        result = Request().send_request(url, method, header, data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
        print(data)
        print(result)

    @allure.feature('行业分析')
    @allure.title("行业财务分析")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('IndustryAnalysis_industryKeyFinals.yml'))
    def test_industryKeyFinals(self, caseinfo, web_endDate):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['endDate'] = web_endDate
        result = Request().send_request(url, method, header, data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
        print(data)
        print(result)

    @allure.feature('行业分析')
    @allure.title("行业发展趋势1")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('IndustryAnalysis_industryTrend.yml'))
    def test_industryTrend(self, caseinfo, web_endDate):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['endDate'] = web_endDate
        data['firstCode'] = YamlUtil().read_extract_yaml('industryCode')
        result = Request().send_request(url, method, header, data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
        print(data)
        print(result)

    @allure.feature('行业分析')
    @allure.title("行业管理熵发展")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('IndustryAnalysis_industryTrendMsScore.yml'))
    def test_industryTrendMsScore(self, caseinfo, web_endDate):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['endDate'] = web_endDate
        data['firstCode'] = YamlUtil().read_extract_yaml('industryCode')
        result = Request().send_request(url, method, header, data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
        print(data)
        print(result)

    @allure.feature('行业分析')
    @allure.title("行业上市公司分布")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('IndustryAnalysis_onMarket.yml'))
    def test_onMarket(self, caseinfo, web_endDate):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['endDate'] = web_endDate
        data['firstCode'] = YamlUtil().read_extract_yaml('industryCode')
        result = Request().send_request(url, method, header, data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
        print(data)
        print(result)

    @allure.feature('行业分析')
    @allure.title("行业竞争梯队")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('IndustryAnalysis_competeEchelon.yml'))
    def test_competeEchelon(self, caseinfo, web_endDate):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['endDate'] = web_endDate
        data['firstCode'] = YamlUtil().read_extract_yaml('industryCode')
        result = Request().send_request(url, method, header, data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)


    @allure.feature('行业分析')
    @allure.title("行业集中度")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('IndustryAnalysis_competeConcentration.yml'))
    def test_competeConcentration(self, caseinfo, web_endDate):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['endDate'] = web_endDate
        data['firstCode'] = YamlUtil().read_extract_yaml('industryCode')
        result = Request().send_request(url, method, header, data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
    @allure.feature('行业分析')
    @allure.title("行业分析头部")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('IndustryAnalysis_industryHead.yml'))
    def test_industryHead(self, caseinfo, web_endDate):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['endDate'] = web_endDate
        data['firstCode'] = YamlUtil().read_extract_yaml('industryCode')
        result = Request().send_request(url, method, header, data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)

    @allure.feature('行业分析')
    @allure.title("行业分析龙头行业")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('IndustryAnalysis_getSecondIndustry.yml'))
    def test_getSecondIndustry(self, caseinfo, web_endDate):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['endDate'] = web_endDate
        data['SecondCode'] = YamlUtil().read_extract_yaml('industryCode')
        data['SecondName'] = YamlUtil().read_extract_yaml('industryName')
        result = Request().send_request(url, method, header, data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)

    @allure.feature('行业分析')
    @allure.title("五力分析")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('IndustryAnalysis_modelgetByIndicator.yml'))
    def test_modelgetByIndicator(self, caseinfo):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        result = Request().send_request(url, method, header, data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
    @allure.feature('行业分析')
    @allure.title("行业绩效分析")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('IndustryAnalysis_industryPerformance.yml'))
    def test_industryPerformance(self, caseinfo,web_endDate):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['endDate'] = web_endDate
        data['firstCode'] = YamlUtil().read_extract_yaml('industryCode')
        data['endDate'] = web_endDate
        result = Request().send_request(url, method, header, data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)

    @allure.feature('行业分析')
    @allure.title("同业公司对比")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('IndustryAnalysis_companyCompare.yml'))
    def test_companyCompare(self, caseinfo, web_endDate):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['endDate'] = web_endDate
        data['firstCode'] = YamlUtil().read_extract_yaml('industryCode')
        result = Request().send_request(url, method, header, data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)


    @allure.feature('行业分析')
    @allure.title("行业排行榜")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('IndustryAnalysis_industryRank.yml'))
    def test_industryRank(self, caseinfo, web_endDate):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['endDate'] = web_endDate
        result = Request().send_request(url, method, header, data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)


    @allure.feature('产业链中心')
    @allure.title("热门公司")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('chain_selectList.yml'))
    def test_chainselectList(self, caseinfo, web_endDate):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        result = Request().send_request(url, method, header, data)
        YamlUtil().write_extract_yaml({'title':'产业链code'})
        YamlUtil().write_extract_yaml({'chain_code':result['data'][0]['chain_code']})
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)


    @allure.feature('产业链中心')
    @allure.title("热门赛道")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('chain_selectChainCategoryList.yml'))
    def test_chainselectChainCategoryList(self, caseinfo):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        result = Request().send_request(url, method, header)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
    @allure.feature('产业链中心')
    @allure.title('我的产业链')
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('chain_findChainUsersList.yml'))
    def test_chainfindChainUsersList(self, caseinfo):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['userId'] = YamlUtil().read_extract_yaml('userId')
        result = Request().send_request(url, method, header,data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
       

    @allure.feature('产业链中心')
    @allure.title('产业链全景')
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('chain_getChaInData.yml'))
    def test_chaingetChanData(self, caseinfo, web_year):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['chainCode'] = YamlUtil().read_extract_yaml('chain_code')
        data['year'] = web_year
        result = Request().send_request(url, method, header, data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)

    @allure.feature('产业链中心')
    @allure.title('产业链分析')
    @pytest.mark.parametrize("caseinfo",YamlUtil().read_testcase_yaml('chain_analysis.yml'))
    def test_chainanalysis(self, caseinfo):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['chainCode'] = YamlUtil().read_extract_yaml('chain_code')
        result = Request().send_request(url, method, header, data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
    @allure.feature('产业链中心')
    @allure.title('产业链创建')
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('chain_create.yml'))
    def test_chaincreate(self, caseinfo):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['userId'] = YamlUtil().read_extract_yaml('userId')
        result = Request().send_request(url, method, header, data)
        YamlUtil().write_extract_yaml({'title':'新建产业链code'})
        YamlUtil().write_extract_yaml({'creat_chain_id':result['data']['data']['id']})
        YamlUtil().write_extract_yaml({'creat_chain_code': result['data']['data']['chain_code']})
        YamlUtil().write_extract_yaml({'creat_chain_name': result['data']['data']['chain_name']})
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
        

    @allure.feature('产业链中心')
    @allure.title('产业链产品')
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('chain_selectProductCompanys.yml'))
    def test_chainselectProductCompanys(self, caseinfo, web_year):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        result = Request().send_request(url, method, header, data)
        YamlUtil().write_extract_yaml({'title':'产品code'})
        YamlUtil().write_extract_yaml({'product_code': result['data'][0]['product_code']})
        YamlUtil().write_extract_yaml({'product_name':result['data'][0]['product_name']})
        YamlUtil().write_extract_yaml({'产品公司的长度':len(result['data'])})#
        YamlUtil().write_extract_yaml({'title': '产品公司的code'})
        print(len(result['data']))
        for i in range(len(result['data'])):
            YamlUtil().write_extract_yaml({'org_code_'+str(i):result['data'][i]['org_code']})
            YamlUtil().write_extract_yaml({'org_name_abbr_'+str(i):result['data'][i]['org_name_abbr']})
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)

    @allure.feature('产业链中心')
    @allure.title('产业链保存产品')
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('chain_insertChan.yml'))
    def test_chaininsertChan(self, caseinfo, web_year):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['chainCode'] = YamlUtil().read_extract_yaml('creat_chain_code')
        data['chainName'] = YamlUtil().read_extract_yaml('creat_chain_name')
        data['id'] = YamlUtil().read_extract_yaml('creat_chain_id')
        data['userId'] = YamlUtil().read_extract_yaml('userId')
        s=YamlUtil().read_extract_yaml('产品公司的长度')
        companys=[]
        for i in range(int(s)):#创字典，加入列表
            dict = {'orgCode':YamlUtil().read_extract_yaml('org_code_'+str(i))
                    ,'name':YamlUtil().read_extract_yaml('org_name_abbr_'+str(i))}
            companys.append(dict)
        data['list1'][0]['productName'] = YamlUtil().read_extract_yaml('product_name')
        data['list1'][0]['productCode'] = YamlUtil().read_extract_yaml('product_code')
        data['list1'][0]['companys']=companys
        result = Request().send_request(url, method, header, data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
        

    @allure.feature('产业链中心')
    @allure.title('新建产业链')
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('chain_getChanDataUser.yml'))
    def test_chaingetChanDataUser(self, caseinfo, web_year):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['chainId'] = YamlUtil().read_extract_yaml('creat_chain_id')
        data['year'] = web_year
        result = Request().send_request(url, method, header, data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
        

    @allure.feature('产业链中心')
    @allure.title('删除产业链')
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('chain_delete.yml'))
    def test_Chaindelete(self, caseinfo):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['id'] = YamlUtil().read_extract_yaml('creat_chain_id')
        result = Request().send_request(url, method, header, data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)



    @allure.feature('企业排行榜')
    @allure.title('企业排行榜')
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('rankingSelectAllRankConfigRoot.yml'))
    def test_selectAllRankConfigRoot(self, caseinfo,web_endDate):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['endDate'] = web_endDate
        result = Request().send_request(url, method, header, data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
        print(result)

    @allure.feature('企业排行榜')
    @allure.title('企业排行榜模块')
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('rankingallType.yml'))
    def test_selectAllRankConfigRoot(self, caseinfo):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        result = Request().send_request(url, method, header)
        YamlUtil().write_extract_yaml({'rankingallType_code': result['data'][random.randint(0, 11)]['code']})
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)

    @allure.feature('企业排行榜')
    @allure.title('企业排行榜二级页面')
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('rankingcompany.yml'))
    def test_rankingcompany(self, caseinfo, web_endDate):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['endDate'] = web_endDate
        data['code'] = YamlUtil().read_extract_yaml('rankingallType_code')
        result = Request().send_request(url, method, header, data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
        # print(result)

    @allure.feature('基线库')
    @allure.title('基线库指标')
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('baselineindexList.yml'))
    def test_baselineindexList(self, caseinfo):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        result = Request().send_request(url, method, header, data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
        print(result)

    @allure.feature('在线诊断')
    @allure.title('创建公司')
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('diagnosis_insertCompanyInfo.yml'))
    def test_baselineindexList(self, caseinfo):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['userId'] = YamlUtil().read_extract_yaml('userId')
        result = Request().send_request(url, method, header, data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
        print(result)

    @allure.feature('在线诊断')
    @allure.title('在线诊断')
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('diagnosis_queryCompanyInfos.yml'))
    def test_queryCompanyInfos(self, caseinfo):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['userId'] = YamlUtil().read_extract_yaml('userId')
        result = Request().send_request(url, method, header, data)
        allure.attach(str(data), name='请求参数', attachment_type=allure.attachment_type.JSON)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
        YamlUtil().write_extract_yaml({"companyinfoCode": result['data']['list'][0]['org_code']})
        print(result)

    @allure.feature('在线诊断')
    @allure.title('公司详情')
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('diagnosis_findCompanyInfo.yml'))
    def test_findCompanyInfo(self, caseinfo):
        url = test_host + caseinfo['request']['url']+ YamlUtil().read_extract_yaml('companyinfoCode')
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        result = Request().send_request(url, method, header)
        YamlUtil().write_extract_yaml({"title": '获取公司的经营单元'})
        YamlUtil().write_extract_yaml({"busi_unit_code": result['data']['busiUnitMains'][0]['busi_unit_code']})
        YamlUtil().write_extract_yaml({"busi_unit_type": result['data']['busiUnitMains'][0]['busi_unit_type']})
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
        print(result)
    @allure.feature('在线诊断')
    @allure.title('资产负债表的2023年添加数据')
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('diagnosis_createDatabalance.yml'))
    def test_createData_balance(self, caseinfo):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['org_code'] = YamlUtil().read_extract_yaml('companyinfoCode')
        result = Request().send_request(url, method, header, data)
        allure.attach(str(data), name='请求参数', attachment_type=allure.attachment_type.JSON)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
        print(result)

    @allure.feature('在线诊断')
    @allure.title('删除资产负债表的20403数据')
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('diagnosis_deleteDatabalance.yml'))
    def test_deleteDatabalance(self, caseinfo):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['orgCode'] = YamlUtil().read_extract_yaml('companyinfoCode')
        result = Request().send_request(url, method, header, data)
        allure.attach(str(data), name='请求参数', attachment_type=allure.attachment_type.JSON)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
        print(result)

    @allure.feature('在线诊断')
    @allure.title('上传资产负债表的数据')
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('diagnosis_importbalance.yml'))
    def test_import_balance(self, caseinfo):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['orgCode'] = YamlUtil().read_extract_yaml('companyinfoCode')
        with open(r'../data/importdata/balance.xlsx', 'rb') as f:
            file = {"file": f}
            header = {'Accept-Encoding': 'gzip, deflate, br'}
            header['Authorization'] = YamlUtil().read_extract_yaml('token')
            res = requests.request(url=url, method=method, headers=header, data=data,files=file)
            result = res.json()
        allure.attach(str(data), name='请求参数', attachment_type=allure.attachment_type.JSON)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
        YamlUtil().write_extract_yaml({"title": '资产负债表的数据'})
        YamlUtil().write_extract_yaml({"balance_innerList": result['data']['innerList']})
        print(result)

    @allure.feature('在线诊断')
    @allure.title('插入资产负债表的数据')
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('diagnosis_batchInsertbalance.yml'))
    def test_batchInsert_balance(self, caseinfo):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['orgCode'] = YamlUtil().read_extract_yaml('companyinfoCode')
        data['innerList'] = YamlUtil().read_extract_yaml('balance_innerList')

        result = Request().send_request(url, method, header, data)
        allure.attach(str(data), name='请求参数', attachment_type=allure.attachment_type.JSON)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)


    @allure.feature('在线诊断')
    @allure.title('上传利润表的数据')
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('diagnosis_importincome.yml'))
    def test_import_income(self, caseinfo):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['orgCode'] = YamlUtil().read_extract_yaml('companyinfoCode')
        with open(r'../data/importdata/income.xlsx', 'rb') as f:
            file = {"file": f}
            header = {'Accept-Encoding': 'gzip, deflate, br'}
            header['Authorization'] = YamlUtil().read_extract_yaml('token')
            res = requests.request(url=url, method=method, headers=header, data=data, files=file)
            result = res.json()
        allure.attach(str(data), name='请求参数', attachment_type=allure.attachment_type.JSON)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
        YamlUtil().write_extract_yaml({"title": '利润表的数据'})
        YamlUtil().write_extract_yaml({"income_innerList": result['data']['innerList']})


    @allure.feature('在线诊断')
    @allure.title('利润表上插入数据')
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('diagnosis_batchInsertincome.yml'))
    def test_batchInsert_income(self, caseinfo):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['orgCode'] = YamlUtil().read_extract_yaml('companyinfoCode')
        data['innerList'] = YamlUtil().read_extract_yaml('income_innerList')

        result = Request().send_request(url, method, header, data)
        allure.attach(str(data), name='请求参数', attachment_type=allure.attachment_type.JSON)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)


    @allure.feature('在线诊断')
    @allure.title('现金流量表上传数据')
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('diagnosis_importCashFlow.yml'))
    def test_import_CashFlow(self, caseinfo):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['orgCode'] = YamlUtil().read_extract_yaml('companyinfoCode')
        with open(r'../data/importdata/CashFlow.xlsx', 'rb') as f:
            file = {"file": f}
            header = {'Accept-Encoding': 'gzip, deflate, br'}
            header['Authorization'] = YamlUtil().read_extract_yaml('token')
            res = requests.request(url=url, method=method, headers=header, data=data, files=file)
            result = res.json()
        allure.attach(str(data), name='请求参数', attachment_type=allure.attachment_type.JSON)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
        YamlUtil().write_extract_yaml({"title": '利润表的数据'})
        YamlUtil().write_extract_yaml({"CashFlow_innerList": result['data']['innerList']})

    @allure.feature('在线诊断')
    @allure.title('现金流量表上插入数据')
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('diagnosis_batchInsertCashFlow.yml'))
    def test_batchInsert_CashFlow(self, caseinfo):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['orgCode'] = YamlUtil().read_extract_yaml('companyinfoCode')
        data['innerList'] = YamlUtil().read_extract_yaml('CashFlow_innerList')
        print(data)
        result = Request().send_request(url, method, header, data)
        allure.attach(str(data), name='请求参数', attachment_type=allure.attachment_type.JSON)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
        print(result)

    @allure.feature('在线诊断')
    @allure.title('完成开始计算第一步')
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('diagnosis_done1.yml'))
    def test_done1(self, caseinfo):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['orgCode'] = YamlUtil().read_extract_yaml('companyinfoCode')
        result = Request().send_request(url, method, header, data)
        allure.attach(str(data), name='请求参数', attachment_type=allure.attachment_type.JSON)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
        print(result)

    @allure.feature('在线诊断')
    @allure.title('完成开始计算第二步')
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('diagnosis_done1.yml'))
    def test_done2(self, caseinfo):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['orgCode'] = YamlUtil().read_extract_yaml('companyinfoCode')
        data['step']=2
        result = Request().send_request(url, method, header, data)
        allure.attach(str(data), name='请求参数', attachment_type=allure.attachment_type.JSON)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)

    @allure.feature('在线诊断')
    @allure.title('删除企业')
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('diagnosis_deleteCompanyInfo.yml'))
    def test_deleteCompanyInfo(self, caseinfo):
        url = test_host + caseinfo['request']['url']+YamlUtil().read_extract_yaml('companyinfoCode')
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        result = Request().send_request(url, method, header)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)

    @allure.feature('个人中心')
    @allure.title("改变角色")
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_testcase_yaml('updateuserType.yml'))
    def test_updateuserType(self, caseinfo):
        url = test_host + caseinfo['request']['url']
        header = caseinfo['request']['header']
        method = caseinfo['request']['method']
        header['Authorization'] = YamlUtil().read_extract_yaml('token')
        data = caseinfo['request']['data']
        data['userId'] = YamlUtil().read_extract_yaml('userId')
        data['userType'] =random.randint(1,4)
        result = Request().send_request(url, method, header, data)
        allure.attach(str(result), name='接口返回数据', attachment_type=allure.attachment_type.JSON)
        print(result)
        '''






if __name__ == "__main__":
    pytest. main(['-vs '])

