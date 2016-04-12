#/usr/env/bin python3
# coding = utf-8

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.header import Header
import os,time,datetime

def sentmail(file_new):
    mail_from = 'wqqtest001@163.com'
    mail_to = 'qiaoqiwu@pptv.com'
    subject = u"PPTV首页自动化测试报告"

    f = open(file_new,'rb')
    mail_body = f.read()
    f.close()
    #msg = MIMEText(mail_body,_subtype='html',_charset='utf-8')
    msg = MIMEMultipart('alternative')
    
    msg['Subject'] = Header(subject,'utf-8')
    msg['date'] = time.strftime('%a,%d %b %Y %H:%M:%S %z')
    msg['From'] = mail_from
    msg['To'] = mail_to

    att1 = MIMEText(mail_body,'base64','utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment;filename = %s' % file_new
    msg.attach(att1)

    att2 = MIMEText(mail_body,_subtype='html',_charset='utf-8')
    msg.attach(att2)
    
    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com')
    smtp.login('wqqtest001@163.com','bangbus')
    smtp.sendmail(mail_from,mail_to,msg.as_string())
    smtp.quit()

def sendreport():
    result_dir = 'D:\\'
    lists = os.listdir(result_dir)
    lists.sort(key=lambda fn:os.path.getmtime(result_dir + "\\" + fn) if not os.path
               .isdir(result_dir + "\\" + fn) else 0)
    print(u'最新测试生成的报告: ' +lists[-1])
    file_new = os.path.join(result_dir,lists[-1])
    sentmail(file_new)
