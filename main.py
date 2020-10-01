# Importing the SMTP library which handles sending E-mails and routing E-mails between mail servers.
import smtplib
from tkinter import *



# create root window 
root = Tk() 
  
# root window title and dimension 
root.title("Python Send E-mails") 
root.geometry('350x200') 

#Establish SMTP Connection
s = smtplib.SMTP('smtp.gmail.com', 587)

#Start TLS based SMTP Session
s.starttls() 

# adding the Sender E-mail label to the root window 
lbl_1 = Label(root, text = "Sender E-mail address: ") 
lbl_1.grid() 

# adding Entry Field 
sender_e_mail_address = Entry(root, width=30) 
sender_e_mail_address.grid(column = 1, row =0) 

# adding the Sender E-mail label to the root window 
lbl_2 = Label(root, text = "Receiver E-mail address: ") 
lbl_2.grid() 

# adding Entry Field 
receiver_e_mail_address = Entry(root, width=30) 
receiver_e_mail_address.grid(column = 1, row =1) 
  
# function to display text when 
# button is clicked 
def clicked(): 
    #Login Using Your E-mail & Password
    s.login(sender_e_mail_address, "<sender-E-mail-password")

    #Email Body Content
    message = """
    Hello, this is an example message!
    """

    #To Send the E-mail
    s.sendmail(sender_e_mail_address, receiver_e_mail_address, message)
    
    #Terminating the SMTP Session
    s.quit()

    
# button widget with text inside 
btn = Button(root, text = "Send" , 
             fg = "black", command=clicked) 
  
btn.grid(column=1, row=3) 


root.mainloop()


