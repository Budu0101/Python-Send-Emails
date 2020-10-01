# Python Send E-mails

Python Send E-mails is a script that lets you send automatic E-Mails with Python and the SMTP library.

## Warning

If you get an error while running the script it's because of a bug I can't seem to fix yet. I welcome you to test the app and try to solv the bug. If you solved it, please open a Pull Request with the solved main.py script.
For more details check the comments of the Tkinter GUI Pull Request.
## Installation

Python should come pre-installed with smtplib which is a required library for this project.
If not, a **pip install smtplib** should work.


## Usage

```python
# Importing the SMTP library which handles sending E-mails and routing E-mails between mail servers.
import smtplib
  
#Establish SMTP Connection
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
#Start TLS based SMTP Session
s.starttls() 

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


```

**IMPORTANT : If you're using Gmail you might need to allow less secure apps from your account settings.
When you try the script for the first time you might also need to go to your sender address and say that it was you to who ran the script to stop Google's warning that the program might not be secure.**

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## Licence

MIT License

Copyright (c) 2020 Stan Andrei

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
