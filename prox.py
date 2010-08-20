import socket, select, re, time

#This will need to be replaced if we start accepting multiple MUSHes.
main_mush = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
main_mush.connect(("localhost",1987)) #Change this to the MUSH server and port of your choice.
time.sleep(2) #May not be necessary, I really don't know
main_mush.send("connect <name> <password>\n\r") #Replace <name> and <password> with your username and password.

clients = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clients.bind(("",4077)) #If you change the port output.php uses, you also need to change this.
clients.listen (1)
clients.setblocking(0)

def main():
  while True:
    read_ready, write_ready, error = select.select([main_mush, clients],[],[])
    for i in read_ready:
      if i is main_mush:
        mushListen(i)
      elif i is clients:
        print i
        sock = clients.accept()[0]
        data = sock.recv(1024)
        main_mush.send(data)
        sock.close()

def mushListen(conn):
  data = conn.recv(128)
  if data[0] == chr(255): #I THINK this throws out control Chars.
    try: data = data[3:]
    except:
      print "Something screwy when throwing out control Chars!"
      return 0
  if len(data) == 0: return 0 #Why the frak does this ever happen?!
  expression = chr(27)+"\\[.*?m" #For clearing colors
  data = re.sub(expression,"",data)
  expression = "<|>"
  data = re.sub(expression,"|",data)
  f = open('./log.log','a')
  expression = "\r" #For linebreaks
  data = re.sub(expression,"\r<br>",data)
  f.write(data)
  f.close()

main()
