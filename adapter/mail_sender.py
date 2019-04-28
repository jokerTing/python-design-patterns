import smtplib
from email.mime.text import MIMEText
from user_fetcher import UserFetcher

class Mailer(object):
    def send(self, sender, recipients, subject, message):
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = ",".join(recipients)
        print("[email]{}".format(msg))
        '''
        mail_sender = smtplib.SMTP('localhost')
        mail_sender.send_message(msg)
        mail_sender.quit()
        '''

class Logger(object):
    def output(message):
        print("[Logger]{}".format(message))

class LoggerAdapter(object):
    def __init__(self, what_i_have):
        self.what_i_have = what_i_have

    # 将原Logger接口修改邮件发送情况下的接口
    def send(self, sender, recipients, subject, message):
        log_message = "From: {}\nTo: {}\nSubject: {}\nMessage: {}".format(
            sender, recipients, subject, message
        )
        self.what_i_have.output(log_message)
    
    def __getattr__(self, attr):
        return getattr(self.what_i_have, attr)

if __name__ == "__main__":
    user_fetcher = UserFetcher('adapter/users.csv')
    #mailer = Mailer()
    mail_logger = LoggerAdapter(Logger)
    mail_logger.send(
        'me@example.com', 
        [x["email"] for x in user_fetcher.fetch_users()],
        "This is your message", "Have a good day"
    )
    mail_logger.output("Provited function")
