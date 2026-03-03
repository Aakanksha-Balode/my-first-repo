import smtplib as s

ob = s.SMTP('smtp.gmail.com', 587)
ob.ehlo()
ob.starttls()
ob.login('aakankshabalode@gmail.com', 'password')
subject = "test python"
body = "i love python"
message = "subject: {}\n\n{}".format(subject, body)
listadd = ["resiver mail id"]
ob.sendmail('aakankshabalode@gmail.com', listadd,message)
print("send mail completed")
ob.quit()
