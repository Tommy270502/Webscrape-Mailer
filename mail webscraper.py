from bs4 import BeautifulSoup
import requests
import re
import smtplib
from email.mime.multipart import MIMEMultipart

news = ""
r = requests.get("www.yourwebsite.com")
soup = BeautifulSoup(r.text, 'html.parser')
result = soup.find('yourhtml', attrs = {'class':'yourclassname'})

news += result.text

gmail_user = 'yourmail@gmail.com' #Enter your gmail address
gmail_password = 'yourpassword'   #Enter your Email pasword
sent_from = gmail_user
to = ['receivermail@mail.com']      #list of destination Email address

#Email title
msg = """Subject:
"""
#add news to email massage
msg += news

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, msg)
    server.close()

    print ('Email sent!')
except:
    print ('Something went wrong...')
