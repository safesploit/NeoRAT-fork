import smtplib


def send_email(sender, sender_pw, recievers, subject, text):
  message = f'From: {sender}\nTo: {recievers}\nSubject: {subject}\n\n{text}'

  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.ehlo()
  server.starttls()
  server.login(sender, sender_pw)
  server.sendmail(sender, recievers, message)
  server.close()