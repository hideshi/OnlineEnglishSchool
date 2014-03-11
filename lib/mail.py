import smtplib

def send_mail(msg):
  # 初期設定
  host = 'smtp.xxxx.com'
  port = '587'
  username = 'username'
  password = 'password'
  subject = 'Subject'
  message_body = str(msg)

  message = '''
  From: {0}
  To: {1}
  Subject: {2}

  {3}
  '''.format(username, username, subject, message_body)

  # メールを送信
  server = smtplib.SMTP(host, port)
  server.ehlo()
  server.starttls()
  server.ehlo()
  server.login(username, password)
  server.sendmail(username, username, message)
  server.quit()
