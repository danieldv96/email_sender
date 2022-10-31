import smtplib
import csv
import getpass

print("heeeeeeeeeeeeeeeeey")


def sendemail():
    smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_object.starttls()
    email = input("Email: ")
    password = getpass.getpass("password: ")
    print("password received")
    smtp_object.login(email, password)
    mailtxt = open('mail.txt', 'r')
    mailtxt = mailtxt.read()
    with open('mailist.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            print("email sent")
            from_address = email
            to_address = line[0]
            subject = "Reconciliacion"
            message = f"Buen dia {line[1]},\n\n" + \
                mailtxt + "\n\n" + "Cordialmente,"
            msg = "Subject:" + subject + "\n" + message
            smtp_object.sendmail(from_address, to_address, msg)


sendemail()
