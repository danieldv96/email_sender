import smtplib
import csv
import tkinter
import time

window = tkinter.Tk()
window.geometry("1000x800")


def sendemail(email, password):
    smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_object.starttls()
    smtp_object.login(email, password)
    subtxt = open('subject.txt', 'r')
    subtxt = subtxt.read()
    mailtxt = open('mail.txt', 'r')
    mailtxt = mailtxt.read()
    introtxt = open('intro.txt', 'r')
    introtxt = introtxt.read()
    endtxt = open('end.txt', 'r')
    endtxt = endtxt.read()
    with open('mailist.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            from_address = email
            to_address = line[0]
            subject = subtxt
            message = introtxt+f"{line[1]},\n\n" + \
                mailtxt + "\n\n" + endtxt
            msg = "Subject:" + subject + "\n" + message
            smtp_object.sendmail(from_address, to_address, msg)
            label = tkinter.Label(
                window, text="sending email", font="Helvetica 20")
            label.pack()
            time.sleep(1.2)


def captureinput():
    mail = entry1.get()
    password = widget.get()
    sendemail(mail, password)


label = tkinter.Label(
    window, text="Ingresa tu correo y contraseña para enviar los mail", font="Helvetica 20")
label.pack()
label1 = tkinter.Label(window, text="\n", font="Helvetica 20")
label1.pack()
label2 = tkinter.Label(window, text="Correo:", font="Helvetica 20")
label2.pack()
entry1 = tkinter.Entry(window, font="Helvetica 16")
entry1.pack(ipadx=50, ipady=5)
label3 = tkinter.Label(window, text="\n", font="Helvetica 20")
label3.pack()
label4 = tkinter.Label(window, text="Clave:", font="Helvetica 20")
label4.pack()
widget = tkinter.Entry(window, show="*", font="Helvetica 16")
widget.pack(ipadx=50, ipady=5)
boton = tkinter.Button(window, text="Start",
                       command=captureinput, font="Helvetica 20")
boton.pack()
label5 = tkinter.Label(window, text="", font="Helvetica 20")
label5.pack()

window.mainloop()
