# coding! utf-8
# 发邮件的任务

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.multipart import MIMEBase
from project import conf
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.header import Header

def xxxxx():
    def _format_addr(s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr.encode('utf-8')))

    smtp_server = 'smtp.qq.com'

    # 邮件对象:
    msg = MIMEMultipart()
    msg['From'] = _format_addr(u'Python爱好者 <%s>' % conf.from_email)
    msg['To'] = _format_addr(u'管理员 <%s>' % conf.to_email)
    msg['Subject'] = Header(u'来自SMTP的问候……', 'utf-8').encode()


    #读取附件的内容
    att1 = MIMEText(open(conf.excel_file, 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    #生成附件的名称
    att1["Content-Disposition"] = 'attachment; filename=abc.xlsx'
    #将附件内容插入邮件中
    msg.attach(att1)

    # 邮件正文是MIMEText:
    msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))

    # 添加附件就是加上一个MIMEBase，从本地读取一个图片:
    with open('/Users/michael/Downloads/test.png', 'rb') as f:
        # 设置附件的MIME和文件名，这里是png类型:
        mime = MIMEBase('image', 'png', filename=conf.excel_file)
        # 加上必要的头信息:
        mime.add_header('Content-Disposition', 'attachment', filename=conf.excel_file)
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        # 把附件的内容读进来:
        mime.set_payload(f.read())
        # 用Base64编码:
        encoders.encode_base64(mime)
        # 添加到MIMEMultipart:
        msg.attach(mime)


# 发送QQ邮件
def send_email(text):
    today = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    subject = "[api_test]接口自动化测试结果通知{}".format(today)

    msg = MIMEText(text, 'html', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = conf.from_email
    msg['To'] = conf.to_email
    try:
        smtp = smtplib.SMTP_SSL(conf.smtp_server, 465)
        smtp.login(conf.from_email, conf.from_pwd)
        smtp.sendmail(conf.from_email, conf.to_email, msg.as_string())
    except Exception as e:
        print("发送失败，因为:{}.".format(e))


if __name__ == '__main__':
    send_email('ds')


