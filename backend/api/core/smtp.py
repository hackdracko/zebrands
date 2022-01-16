import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# CONFIGURATION FOR SEND NOTIFICATION BY EMAIL
def sendNotification(id, username, email):
    mail_content = 'The product ' + id + ' was updated by ' + username
    #The mail addresses and password
    sender_address = 'patolin00755@gmail.com'
    sender_pass = 'amohyrkaujkfajte'
    receiver_address = email
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Zebrands notification product updated'   #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()