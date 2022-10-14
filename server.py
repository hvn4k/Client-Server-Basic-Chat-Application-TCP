import socket
import threading
import tkinter as tk
from tkinter import *

def connect():
  global conn
  HOST = "127.0.0.1"
  try:
    PORT = int(entry1.get())
    
  except Exception as e:
     print(e)
     exit(0)
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        x = threading.Thread(target=recieve,args=())
        x.start()
    
    
global msg
def send(message):
    global conn
    conn.send(message.encode())
    entry3.delete(0,END)
    entry3.insert(0,"")
    entry4.insert(END,'Server : ' + message + '\n')

def on_closing():
   
   window.destroy()

def recieve():
   global conn
   print("here")
   while True:
       try:
                data = conn.recv(4096)
                data = data.decode()
                
                entry4.insert(END,'Client : ' + data + '\n')

                print("from client: ")
                print(data)
       except Exception as e:
           print(e)
           exit(0)

if __name__ == "__main__":
    
    window = tk.Tk()
    window.geometry('400x300')
    window.title('Server Window')
    l1 = tk.Label(text="port")
    l1.grid()
    entry1 =Entry(window)
    entry1.grid()
    button = Button(window,text="connect", bg = 'blue' , fg='white',command=lambda: connect()).grid()
    l3 = tk.Label(text="send message to client")
    l3.grid()
    entry3 = Entry(window)
    entry3.grid()
    button1 = Button(window,text="send", bg = 'blue' , fg='white',command=lambda: send(entry3.get())).grid()
    l4 = tk.Label(text="recieved message from client")
    l4.grid()
    entry4 = Text(window,width=50,height=5)
    entry4.grid()
    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.mainloop()
 
         