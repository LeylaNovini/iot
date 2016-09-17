import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.mime.image import MIMEImage
from cStringIO import StringIO
from email.generator import Generator
import time

# emails
strFrom = 'your@email.com'
strTo = 'another@email.com'

# from, to, and subject headers
msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = 'Fun Facts About Alpacas'
msgRoot['From'] = strFrom
msgRoot['To'] = strTo
msgRoot.preamble = 'Have you ever wondered about the fascinating life of an alpaca ? They are truely extrordinary animals. The alpaca has fur that is waterproof and fire resistant. The alpaca also has a variation of 22 different colors of fur.'

msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

msgText = MIMEText('This is the alternative plain text message.')
msgAlternative.attach(msgText)

msgText = MIMEText('Have you ever wondered about the fascinating life of an alpaca ? They are truely extrordinary animals. The alpaca has fur that is waterproof and fire resistant. The alpaca also has a variation of 22 different colors of fur.', 'html')
msgAlternative.attach(msgText)

#open images
fp = open('alpaca.png', 'rb')
fp1 = open('3cuties.png', 'rb')
fp2 = open ('alpacahair.png', 'rb')
fp3 = open('group.png', 'rb')

msgImage = MIMEImage(fp.read())
msgImage1 = MIMEImage(fp1.read())
msgImage2 = MIMEImage(fp2.read())
msgImage3 = MIMEImage(fp3.read())
fp.close()
fp1.close()
fp2.close()
fp3.close()

msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)

msgImage1.add_header('Content-ID', '<image2>')
msgRoot.attach(msgImage1)

msgImage2.add_header('Content-ID', '<image3>')
msgRoot.attach(msgImage2)

msgImage3.add_header('Content-ID', '<image4>')
msgRoot.attach(msgImage3)

newMessage = None
#count the word alpaca
body = 'Have you ever wondered about the fascinating life of an alpaca ? They are truely extrordinary animals. The alpaca has fur that is waterproof and fire resistant. The alpaca also has a variation of 22 different colors of fur.  '
body2 = 'alpaca'
body3 = body.count(body2)

body4 = "The word alpaca appears " +str(body3)+ " times in this email.  "
print body4

#count the images
newimage = [msgImage, msgImage1, msgImage2, msgImage3]
finalimage = len(newimage)

body5 = "You have " +str(finalimage)+ " pictures of alpacas.  "
print body5

newMessage = body + body4 + body5

msgText2 = MIMEText(str(newMessage))
msgAlternative.attach(msgText2)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(strFrom, '*****')
text = msgRoot.as_string()
server.sendmail(strFrom, strTo, text)
server.quit()