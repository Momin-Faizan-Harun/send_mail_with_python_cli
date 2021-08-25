
>>> import smtplib
>>> conn = smtplib.SMTP("smtp.gmail.com",587)
>>> type(conn)
<class 'smtplib.SMTP'>
>>> conn.ehlo()
(250, b'smtp.gmail.com at your service, [183.87.55.134]\nSIZE 35882577\n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nPIPELINING\nCHUNKING\nSMTPUTF8')

>>> conn.starttls()
(220, b'2.0.0 Ready to start TLS')


smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials j6sm21958464pfn.107 - gsmtp')
>>> conn.login('faizanmomin514@gmail.com','98202Hero@')
(235, b'2.7.0 Accepted')

>>> conn.sendmail('faizanmomin514@gmail.com','faizanmomin514@gmail.com','Subject:so long..\n\n Dear al')
{}
>>> conn.quit
<bound method SMTP.quit of <smtplib.SMTP object at 0x7fe88e178588>>
>>> conn.quit()
(221, b'2.0.0 closing connection j6sm21958464pfn.107 - gsmtp') 
