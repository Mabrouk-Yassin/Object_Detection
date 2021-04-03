import base64
import smtplib
import imghdr
from email.message import EmailMessage
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition)


def sendEmail(username, to, subject, body):
    message = Mail(
        from_email=username,
        to_emails=to,
        subject=subject,
        html_content=body)
    with open('ImgToSend/img0.jpg', 'rb') as f:
        data = f.read()
        f.close()
    encoded_file = base64.b64encode(data).decode()

    attachedFile = Attachment(
        FileContent(encoded_file),
        FileName('img0.jpg'),
        FileType('application/image'),
        Disposition('attachment')
    )
    message.attachment = attachedFile
    sg = SendGridAPIClient('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')
    sg.send(message)

def email(username,password,to,subject,body):

    newMessage = EmailMessage()  # creating an object of EmailMessage class
    newMessage['Subject'] = subject  # Defining email subject
    newMessage['From'] = username  # Defining sender email
    newMessage['To'] = to  # Defining reciever email
    newMessage.set_content(body)  # Defining email body

    #files = ['image1.jpg']
    #for file in image :
    with open('ImgToSend/img0.jpg','rb') as m:
        file_date = m.read()
        file_type = imghdr.what(m.name)
        file_name =m.name
    newMessage.add_attachment(file_date , maintype = 'image',subtype = file_type ,filename= file_name)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(username, password)  # Login to SMTP server
        smtp.send_message(newMessage)  # Sending email using send_message method by passing EmailMessage object
