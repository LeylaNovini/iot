import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.mime.image import MIMEImage

fromaddr = 'youremail@gmail.com'
toaddr = 'anotheremail@gmail.com'
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = 'Fun Facts About Alpacas'

body = 'Have you ever wondered about the fascinating life of an alpaca? They are truely extrordinary animals.'
msg.attach(MIMEText(body,'plain'))

for file in images:
    with open(file, 'alpaca') as fp:
        img = MIMEImage(fp.read())
    msg.attach(img)

# def imagecount(n):
#     if n > 0: 
#         print "you have "+str(n)+" picture(s) of alpacas"
#     else: 
#         print "you have no pictures of alpacas"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, '******')
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()