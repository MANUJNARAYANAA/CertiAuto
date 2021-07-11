from os import read
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def read_contacts(filename):
    fnames=[]
    lnames=[]
    receivers=[]
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            fnames.append(a_contact.split()[0])
            lnames.append(a_contact.split()[1])
            receivers.append(a_contact.split()[2])
    return fnames,lnames,receivers


fnames, lnames, receivers = read_contacts('contacts.txt')

sender = 'stateofyouthkpm@gmail.com'
password= 'soykpmkpm'

session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls()
session.login(sender, password)


for fname, lname, email in zip(fnames, lnames, receivers):
    body= "Dear "+ fname + "!"+"\n"+"\n"+"Attached herewith is your certificate"+"\n"+"\n"+"Regards,"+"\n"+"\n"+"State of Youth Namakkal."
    receiver = email
    message = MIMEMultipart()
    message['From']= sender
    message['To'] = receiver
    message['Subject'] = 'Certificate'

    message.attach(MIMEText(body, 'plain'))

    pdfname= './certificates/'+'certificate_'+fname+' '+lname+'.pdf'
    binary_pdf = open(pdfname, 'rb')

    payload = MIMEBase('application', 'octate-stream', Name=pdfname)
    payload.set_payload((binary_pdf).read())

    encoders.encode_base64(payload)

    payload.add_header('Content-Decomposition','attachment', filename = pdfname)
    message.attach(payload)

    text = message. as_string()
    session.sendmail(sender, receiver, text)
    print('Mail Sent to ', fname)

session.quit()

    

    