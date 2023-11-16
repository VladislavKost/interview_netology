import email
import smtplib
import imaplib
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart


class Mail:
    def __init__(self, login, password):
        self.login = login
        self.password = password


    def send_message(self, recipients, subject, message, GMAIL_SMTP):
        msg = MIMEMultipart()
        msg["From"] = self.login
        msg["To"] = ", ".join(recipients)
        msg["Subject"] = subject
        msg.attach(MIMEText(message))

        ms = smtplib.SMTP(GMAIL_SMTP, 587)
        # identify ourselves to smtp gmail client
        ms.ehlo()
        # secure our email with tls encryption
        ms.starttls()
        # re-identify ourselves as an encrypted connection
        ms.ehlo()

        ms.login(self.login, self.password)
        ms.sendmail(self.login, ms, msg.as_string())
        ms.quit()

    def recieve_message(self, header, GMAIL_IMAP):
        mail = imaplib.IMAP4_SSL(GMAIL_IMAP)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % header if header else "ALL"
        result, data = mail.uid("search", None, criterion)
        assert data[0], "There are no letters with current header"
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid("fetch", latest_email_uid, "(RFC822)")
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()


if __name__ == "__main__":
    GMAIL_SMTP = "smtp.gmail.com"
    GMAIL_IMAP = "imap.gmail.com"

    login = "login@gmail.com"
    password = "qwerty"
    subject = "Subject"
    recipients = ["vasya@email.com", "petya@email.com"]
    message = "Message"
    header = None


    mail = Mail(login, password)
    mail.send_message(recipients, subject, message, GMAIL_SMTP)
    mail.recieve_message(header, GMAIL_IMAP)
