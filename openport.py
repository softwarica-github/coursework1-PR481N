''' This project is for checking open ports of the ip or domain in GUI'''
# Author : Prabin Subedi
# Date : 2023/01/27


# imports
import socket
from tkinter import *

def scann(ipaddr, portnum):
    # create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # set a timeout for the socket
    s.settimeout(0.5)
    # try to connect to the host and port
    try:
        result = s.connect((ipaddr, portnum))
        status = 'Open'
        s.close()
    except:
        status = "Close"
        s.close()
    return status


# process function
def scanner():
    ipaddr = ipentry.get()
    portnum = int(portentry.get())

    status = scann(ipaddr,portnum)

    result.config(text = f"Ip or domain: {ipaddr}\nPort : {portnum} \nStatus: {status}")
    portentry.delete(0, "end")



# GUI screen
root = Tk()
root.geometry("800x550+400+100") # screen size
root.title("Open Port Checker")

title = Label(root, text="\nOpen Port Checker", font=("Calibri",35), fg = "red")
title.pack()

# number location label
frame = Frame(root)
frame.pack(pady=20)

# label for ip or domain
ip = Label(frame, text= "Enter ip or domain:",font=("Calibri", 15))
ip.pack()
# ip entry
ipentry = Entry(frame, font= ("Calibri", 15))
ipentry.pack(pady = 10)

# port label
port = Label(frame, text= "Enter port you want to scan:",font=("Calibri", 15))
port.pack()
# port entry
portentry = Entry(frame, font= ("Calibri", 15))
portentry.pack(pady = 10)
# scan button
scan= Button(frame, text= "Search", width= 15, font = 20, bg = "yellow", fg = "red", command=scanner)
scan.pack()
# result label
result = Label(frame, font=('Calibri', 15))
result.pack(pady=20)
# program exit 
Exit = Button(frame, text = "Exit", font= ('Calibri', 15), padx =10, fg='white', bg = 'brown', command = root.destroy)
Exit.pack()
root.mainloop()