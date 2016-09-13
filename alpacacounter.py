import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.mime.image import MIMEImage
from cStringIO import StringIO
from email.generator import Generator

fromaddr = 'youreemail@gmail.com'
toaddr = 'anotheremail@gmail.com'
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = 'Fun Facts About Alpacas'

body = 'Have you ever wondered about the fascinating life of an alpaca ? They are truely extrordinary animals. The alpaca has fur that is waterproof and fire resistant. The alpaca also has a variation of 22 different colors of fur.'
msg.attach(MIMEText(body,'plain'))

fp = open('images/alpaca.png', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()


# for file in images:
with open(file, 'alpaca') as fp:
    img = MIMEImage(fp.read())
msg.attach(img)

# def imagecount(n):
#     if n > 0: 
#         print "you have "+str(n)+" picture(s) of alpacas"
#     else: 
#         print "you have no pictures of alpacas"

wordlist = body.split()

wordfreq = []
for w in wordlist:
    wordfreq.append(wordlist.count(w))

print("The word alpaca appears " + str(wordfreq) + " times in this email")

# b = email.message_from_string(a)
# if b.is_multipart():
#     for part in b.walk():
#         ctype = part.get_content_type()
#         cdispo = str(part.get('Content-Disposition'))

#         # skip any text/plain (txt) attachments
#         if ctype == 'text/plain' and 'attachment' not in cdispo:
#             body = part.get_payload(decode=True)  # decode
#             break
# # not multipart - i.e. plain text, no attachments, keeping fingers crossed
# else:
#     body = b.get_payload(decode=True)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, '*****')
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()