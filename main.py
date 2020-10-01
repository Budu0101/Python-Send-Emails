# Importing the SMTP library which handles sending E-mails and routing E-mails between mail servers.
import smtplib
  
#Establish SMTP Connection
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
#Start TLS based SMTP Session
s.starttls() 

#Login Using Your E-mail & Password
s.login("<sender-E-mail-address>", "<sender-E-mail-password")

#Email Body Content
message = """
Hello, this is an example message!
"""

#To Send the E-mail
s.sendmail("<sender-E-mail-address>", "<receiver-E-mail-address>", message)
  
#Terminating the SMTP Session
s.quit()