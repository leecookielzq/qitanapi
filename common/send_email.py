import smtplib, os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from config.user_config import email_list


class SendEmail(object):
    def __init__(self, send_msg,  # 发送邮件正文
                 smtpserver="smtp.qq.com",  # 设置第三方SMTP
                 sender="3168498358@qq.com",  # 第三方SMTP发送邮箱账号
                 psw="mdmdpaslkjzedfbi",  # 第三方SMTP发送邮箱验证码，qq: qjnddrsdnxmlbhjg, 163: XCFEBAZUDNKCIACT
                 receivers=email_list,  # 接收邮箱
                 port=465,  # 第三方SMTP端口
                 attachment=None):  # 发送附件
        self.send_msg = send_msg
        self.smtpserver = smtpserver
        self.sender = sender
        self.psw = psw
        self.receiver = receivers
        self.port = port
        self.attachment = attachment

    def send_mail(self):
        """发送最新测试报告内容"""
        print('开始发送邮件！')
        # 定义邮件
        msg = MIMEMultipart()
        msg["subject"] = Header("企探1.3接口自动化测试报告", "utf-8")  # 主题
        msg["from"] = Header(self.sender)  # 发送者
        msg["to"] = ','.join(self.receiver)  # 接收者
        # print(msg)

        # 添加附件
        if self.attachment:
            file_name = self.attachment.split(os.path.sep)[-1]
            att = MIMEText(open(self.attachment, "rb").read(), "base64", "utf-8")
            att["Content-Type"] = "application/octet-stream"
            # att["Content-Disposition"] = "attchment; filename='request_auto_report.html'"
            att.add_header('Content-Disposition', 'attachment', filename=file_name)
            msg.attach(att)

        # 读取邮件内容
        with open(self.send_msg, 'rb') as f:
            mail_body = f.read()
        body = MIMEText(mail_body, _subtype="html", _charset='utf-8')
        msg.attach(body)

        smtp = smtplib.SMTP_SSL(host=self.smtpserver)  # 创建一个连接
        # smtp = smtplib.SMTP(host=self.smtpserver)  # 创建一个连接
        smtp.set_debuglevel(1)
        smtp.connect(self.smtpserver, self.port)  # 连接发送邮件服务器
        # smtp.starttls()

        print('开始登录')
        # 用户登录并发送邮件
        smtp.login(self.sender, self.psw)  # 登录服务器
        print('开始发送')
        # 填入邮件的相关信息并发送
        smtp.sendmail(self.sender, msg["to"].split(','), msg.as_string())
        smtp.quit()  # 退出登录
        # return msg

'''调试代码'''
if __name__ =='__main__':
    try:
        sendmail = SendEmail(send_msg=u"..\\data\\email_text",
                             attachment=u"..\\report\\index.html")

        #
        sendmail.send_mail()
        # print()
        # print(SendEmail.send_mail)
        print("发送邮件成功")
    except smtplib.SMTPException as err:
        print("发送邮件失败：{}".format(err))