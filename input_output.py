#Leyla Novini input/output
import RPi.GPIO as GPIO
import time
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import subprocess
import socket
import datetime
import urllib2


GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.IN)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(15, GPIO.IN)


while True:
	input = GPIO.input(7)

	if input == True:
		GPIO.output(11,GPIO.HIGH)
		fromaddr = "your@email.com"
		toaddr = "another@email.com"
		msg = MIMEMultipart()
		msg['From'] = fromaddr
		msg['To'] = toaddr
		msg['Subject'] = "Your Child Needs Assistance"
 
		body = "Your child has pushed the button on his buddy and needs your help."
		msg.attach(MIMEText(body, 'plain'))

		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login(fromaddr, "**********")
		text = msg.as_string()
		server.sendmail(fromaddr, toaddr, text)
		
		status = 1

	if input == False:
		GPIO.output(11,GPIO.LOW)
		status = 0
	print status

	input2 = GPIO.input(15)
	if input2 == True:
		server.quit()


GPIO.cleanup()