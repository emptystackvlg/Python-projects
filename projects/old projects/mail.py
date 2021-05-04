import smtplib
mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.starttls()
mail.login('krykov976@gmail.com','12345Pravda??')
mail.sendmail("krykov976@gmail.com","krykov976@gmail.com","ОАОТОТВАВ".encode('utf8'))
mail.close()