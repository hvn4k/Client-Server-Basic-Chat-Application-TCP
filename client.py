from ctypes.wintypes import MSG
import socket
import threading
import tkinter as tk
from tkinter import *

def connect(s):
    global conn
    try:
        ip = entry1.get()
        port = int(entry2.get())
    except Exception as e:
        print(e)
        exit(0)
    print("ip" , ip)
    print("port",port)
    try:
        conn = s.connect_ex((ip,port))
    except Exception as e:
        print("Invalid IP or PORT")
        exit(0)
    if(conn == 0):
        thred(s)

def is_still_connected(s):
    try:
        s.sendall(b"ping")
        return True
    except:
        return False

def send(s,message):
   
   s.send(message.encode())
   entry3.delete(0,END)
   entry3.insert(0,"")
   entry4.insert(END,'Client : ' + message + '\n')
  	

def recieve(s):
    
    while True:
        try:
            data = s.recv(1024)
            data = data.decode()
            entry4.insert(END,'Server : ' + data + '\n')
        
            print("from server: ")
            print(data)
        except Exception as e:
            if(is_still_connected(s)):
                continue
            else:
                s.close()


def thred(s):  
        x = threading.Thread(target=recieve, args=(s,))
        x.start()
        

    



def on_closing():
   global s
   s.close()
   window.destroy()
        
    
    

if __name__ == "__main__":
    global s
    window = tk.Tk()
    window.geometry('400x300')
    window.title('Client Window')
    s = socket.socket()
    l1 = tk.Label(text="ip")
    l1.grid()
    entry1 =Entry(window)
    entry1.grid()
    l2 = tk.Label(text="port")
    l2.grid()
    entry2 = Entry(window)
    entry2.grid()
    button = Button(window,text="connect",bg = 'blue' , fg='white',command=lambda: connect(s)).grid()
    l3 = tk.Label(text="send message to server")
    l3.grid()
    entry3 = Entry(window)
    entry3.grid()
    button1 = Button(window,text="send",bg = 'blue' , fg='white',command=lambda: send(s,entry3.get())).grid()
    l4 = tk.Label(text="recieved message from server")
    l4.grid()
    entry4 = Text(window,width=50,height=5)
    entry4.grid()
    
    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.mainloop() 