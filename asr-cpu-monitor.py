from netmiko import ConnectHandler
import time
import re
import pprint
import string
import smtplib
import getpass



'''
print("please input your username:")
username=input()
print("please input your password:")
password=input()
'''
print('Please input device account:')
dev_login = getpass.getpass(prompt='Username: ',stream=None)
print('Please input devce password:')
dev_pass = getpass.getpass(prompt='Password: ',stream=None)
print('Please input email account:')
email_login = getpass.getpass(prompt='Email account: ',stream=None)
print('Please input email_password:')
email_pass = getpass.getpass(prompt='Password: ',stream=None)
cisco_asr = {
    'device_type':'cisco_xe',
    'host':'10.28.10.135',
    'username':dev_login,
    'password':dev_pass,
    'port':22,
    'secret':'',}
while True:
    net_connect = ConnectHandler(**cisco_asr)   
    output = net_connect.send_command('show crypto isakmp sa count')
    output = output + "\n" + '''++++++++++++++++Above is VPN status+++++++++++++++++++\n\n\n'''
    output1 = net_connect.send_command('show process cpu history')
    output1 = output1 + '\n' + "++++++++++++++++Above is CPU status+++++++++++++++++++"
    output = output + output1
    SUBJECT = 'Subject: HCSLIDCASR01 CPU and VPN usage!!!'
    TEXT = output
    message = 'Subject: {}\n\n{}'.format(SUBJECT,TEXT)
#pprint.pprint(output,width=100)
    conn = smtplib.SMTP('smtp.live.com',587)
    type(conn)
    conn.ehlo()
    conn.starttls()
    conn.login(email_login,email_pass)
    conn.sendmail('hongtao.zhao@hotmail.com','hongtao.zhao@telus.com',message)
    conn.quit()
    net_connect.disconnect()
    time.sleep(60)
    
    

'''for line in net_connect:
 net_connect = net_connect.rstrip('\n')


hotmail-user= 'hongtao.zhao@hotmail.com'
hotmail-password= ""

from_addr = "hongtao.zhao@hotmail.com"
to_add = "hongtao.zhao@telus.com"
smtp_srv = "smtp.live.com"



subject = "LIDCASR01 real-time CPU usage"
message = output
smtp = smtplib.SMTP



while True:
    output = net_connect.send_command('show process cpu history')
    pprint.pprint(output)
    time.sleep(20)
''' 
