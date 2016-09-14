import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.mime.image import MIMEImage
from cStringIO import StringIO
from email.generator import Generator
import time


# Define these once; use them twice!
strFrom = 'you@email.com'
strTo = 'another@email.com'

# Create the root message and fill in the from, to, and subject headers
msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = 'Fun Facts About Alpacas'
msgRoot['From'] = strFrom
msgRoot['To'] = strTo
msgRoot.preamble = 'Have you ever wondered about the fascinating life of an alpaca ? They are truely extrordinary animals. The alpaca has fur that is waterproof and fire resistant. The alpaca also has a variation of 22 different colors of fur.'

# Encapsulate the plain and HTML versions of the message body in an
# 'alternative' part, so message agents can decide which they want to display.
msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

msgText = MIMEText('This is the alternative plain text message.')
msgAlternative.attach(msgText)

# We reference the image in the IMG SRC attribute by the ID we give it below
msgText = MIMEText('Have you ever wondered about the fascinating life of an alpaca ? They are truely extrordinary animals. The alpaca has fur that is waterproof and fire resistant. The alpaca also has a variation of 22 different colors of fur.', 'html')
msgAlternative.attach(msgText)

# This example assumes the image is in the current directory
fp = open('alpaca.png', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

# Define the image's ID as referenced above
msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)

# while True:
# 	newimage = open('alpaca.png', 'rb')
# 	def imagecount(n):
# 	    if n > 0: 
# 	        print "you have "+str(n)+" picture(s) of alpacas"
# 	    else: 
# 	        print "you have no pictures of alpacas"

# 	    imagecount(newimage)
# 	    time.sleep(5) 

body = 'Have you ever wondered about the fascinating life of an alpaca ? They are truely extrordinary animals. The alpaca has fur that is waterproof and fire resistant. The alpaca also has a variation of 22 different colors of fur.'
wordlist = body.split()

wordfreq = []
for w in wordlist:
    wordfreq.append(wordlist.count(w))

print("The word alpaca appears " + str(wordfreq) + " times in this email")

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(strFrom, '******')
text = msgRoot.as_string()
server.sendmail(strFrom, strTo, text)
server.quit()