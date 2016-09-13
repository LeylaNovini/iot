import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.mime.image import MIMEImage

fromaddr = 'youreemail@gmail.com'
toaddr = 'anotheremail@gmail.com'
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = 'Fun Facts About Alpacas'

body = 'Have you ever wondered about the fascinating life of an alpaca ? They are truely extrordinary animals. The alpaca has fur that is waterproof and fire resistant. The alpaca also '
msg.attach(MIMEText(body,'plain'))


# We reference the image in the IMG SRC attribute by the ID we give it below
# msgText = MIMEText('<b>Some <i>HTML</i> text</b> and an image.<br><img src="cid:image1"><br>Nifty!', 'html')
# msgAlternative.attach(msgText)

# This example assumes the image is in the current directory
fp = open('alpaca.png', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

# Define the image's ID as referenced above
msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)

# for file in images:
#     with open(file, 'alpaca') as fp:
#         img = MIMEImage(fp.read())
#     msg.attach(img)

# def imagecount(n): #define function emailcount
#     if n > 0: 
#         print "you have "+str(n)+" picture(s) of alpacas"
#     else: 
#         print "you have no pictures of alpacas"

wordlist = body.split()

wordfreq = []
for w in wordlist:
    wordfreq.append(wordlist.count(w))

# print("String\n" + body +"\n")
# print("List\n" + str(wordlist) + "\n")
print("The word alpaca appears " + str(wordfreq) + " times in this email")
# print("Pairs\n" + str(zip(wordlist, wordfreq)))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, '******')
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()