import requests
from settings import *

def send_email(user, pwd, recipient, subject, body):
    import smtplib

    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print 'successfully sent the mail'
    except:
        print "failed to send mail"

def login():
    cookie = {'FLMcookie': 'cookie'}
    headers = {
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cache-Control': 'max-age=0',
        'Referer': 'https://www.filmai.in/',
        'Connection': 'keep-alive',
    }

    content = requests.post(
        'https://www.filmai.in',
        cookies=cookie,
        data={'login_name': login_data['name'], 'login_password': login_data['password'], 'login': 'submit'},
        headers=headers
    )

    if (content.content.find('upoints points') == -1):
        if bool(email['sender']) and bool(email['password']) and bool(email['sender']):
            send_email(email['sender'], email['password'], email['recipient'], 'login filmai.in', 'Nepavyko prisijungti')
        else:
            raise Exception('Nepavyko prisijungti')
    else:
        print 'success'


login()



