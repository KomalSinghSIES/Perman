import smtplib
import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content

s = smtplib.SMTP('smtp.gmail.com', 587)

def sendmail(TEXT,email,SUBJECT,tt):
    
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()

    s.login("singhkomal19@siesgst.ac.in", "abc12345")
    message  = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    s.sendmail("singhkomal19@siesgst.ac.in", email, message)
    
    
    
    message  = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    s.sendmail("singhkomal19@siesgst.ac.in", "singhkomal19@siesgst.ac.in", tt)
    s.quit()
    