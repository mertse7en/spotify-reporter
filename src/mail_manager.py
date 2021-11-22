import smtplib
import os
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage


class MailManager:
    def __init__(self):
        self.sender = os.environ["SENDER_MAIL"]
        self.password = os.environ["MAIL_PASSWORD"]
        self.server = 'smtp.gmail.com'
        self.port = 587
        connection = smtplib.SMTP(self.server, self.port)        
        connection.ehlo()
        connection.starttls()
        connection.ehlo
        connection.login(self.sender, self.password)
        self.connection = connection

    def send_mail(self, subject, receiver, html='template', img_path=None, additional=None):
        msgRoot = MIMEMultipart('related')
        msgRoot['Subject'] = subject # 'Last week spotify history!'
        msgRoot['From'] = self.sender
        msgRoot['To'] = receiver

        msgAlternative = MIMEMultipart('TOP 5')
        msgRoot.attach(msgAlternative)

        # msgText = MIMEText('Alternative plain text message.')
        # msgAlternative.attach(msgText)

        if html == 'template':
            msgText = MIMEText('<h1>This weeks most listened songs!!!</h1><br></br><b><i>TOP 5</i></b><br><img src="cid:image1">', 'html')
        else:
            msgText = MIMEText(html, 'html')
            
        msgAlternative.attach(msgText)

        if img_path is not None:
            #Attach Image 
            fp = open(img_path, 'rb') #Read image 
            msgImage = MIMEImage(fp.read())
            fp.close()

            # Define the image's ID as referenced above
            msgImage.add_header('Content-ID', '<image1>')
            msgRoot.attach(msgImage)
        
        self.connection.sendmail(self.sender, receiver, msgRoot.as_string())

        
