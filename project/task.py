# coding! utf-8
import os
import sys
import smtplib
from project import conf
from scrapy.cmdline import execute
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


def debug_scrapy():
    #jincai
    #yidong
    #liantong
    #jianyu
    #dongfang

    scrapy_name = 'dongfang'
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    execute(['scrapy', 'crawl', scrapy_name])


def send_mail():
    att = MIMEText(open(conf.excel_file, 'rb').read(), "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename=%s' % str(os.path.split(conf.excel_file)[1])
    cont = MIMEText('这是邮件正文', 'plain', 'utf-8')
    # pic_name = 'abc.png'
    # pic = MIMEBase('image', 'png', filename=pic_name)
    # pic.add_header('Content-Disposition', 'attachment', filename=pic_name)
    # pic.add_header('Content-ID', '<0>')
    # pic.add_header('X-Attachment-Id', '0')
    # pic.set_payload(open('abc.png', 'rb').read())
    # encoders.encode_base64(pic)

    msg = MIMEMultipart()
    msg['Subject'] = Header("邮件标题", 'utf-8')
    msg['From'] = conf.from_email
    msg['To'] = ",".join(conf.to_email)
    msg.attach(att)
    msg.attach(cont)
    # msg.attach(att1)
    # msg.attach(mime)
    try:
        email = smtplib.SMTP(conf.smtp_server, conf.smtp_port)
        email.login(conf.from_username, conf.from_pwd)
        email.sendmail(conf.from_email, conf.to_email, msg.as_string())
    except Exception as err:
        print("邮件发送失败！%s" % err)
    else:
        print("邮件发送成功")
    finally:
        email.quit()


if __name__ == '__main__':
    # send_mail()
    debug_scrapy()
