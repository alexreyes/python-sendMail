import smtplib    

try:

    # The body of the e-mail
    body = 'Hello World.'

    # The mail server.
    mail = smtplib.SMTP('smtp.gmail.com',587)
    
    # My credentials: 
    myUsername = 'yourEmail@gmail.com'
    password = 'yourPassword'
    personTo = 'otherPersonsEmail@gmail.com'

    # Stuff that verfies the email process.
    mail.ehlo()
    mail.starttls()

    # Login and send the mail. And quit the process.
    mail.login(myUsername, password)
    mail.sendmail(myUsername, personTo, "subject", body)
    mail.quit

    # Announce that it worked.
    print "Successfully sent Email"

# If it throws an error, show the error and notify the programmer.
except smtplib.SMTPException,error:
    print str(error)
    print "Error: unable to send email"