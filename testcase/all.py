import pytest
import os,smtplib
import shutil
# from common.send_email import SendEmail
import subprocess
if __name__ == "__main__":
    # pytest.main(['-vs'])

    pytest.main(['-vs', '--alluredir', '../temp'])  #--alluredir temp
    # os.system('allure serve ./report')#启动生成报告
    #  allure generate 生成测试数据  测试数据目录
    # -o 生成测试报告 测试报告目录

    shutil.copy('../environment.properties', '../temp/environment.properties')#负责文件到temp报告
    os.system('allure generate ../temp -o ../report --clean')
    # try:
    #     sendmail = SendEmail(send_msg=u"..\\data\\email_text")
    #     #
    #     sendmail.send_mail()
    #     print("发送邮件成功")
    # except smtplib.SMTPException as err:
    #     print("发送邮件失败：{}".format(err))
    #
    #
    # port = 8000
    # # PowerShell 命令来启动 HTTP 服务并打开默认浏览器
    # powershell_cmd = f"""
    # $listener = New-Object System.Net.HttpListener
    # $listener.Prefixes.Add("http://+:{port}/")
    # $listener.Start()
    #  Start-Process -FilePath "http://192.168.100.149:{port}"
    #     # $listenerContext = $listener.GetContext()
    #     # $listenerContext.Response.OutputStream.Close()
    #     # """
    #     # subprocess.Popen(["powershell.exe", "-Command", powershell_cmd])