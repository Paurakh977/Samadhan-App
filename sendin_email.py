from smtplib import SMTP

sender = "pandeypaurakhraj@gmail.com"
receiver = "dollarchaeyo@gmail.com"
subject = "Testing"
message = "Hello World!"

server = SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender, "wofe qapr tmzk pymt") 
server.sendmail(sender, receiver, message)
print("done")

server.quit()
