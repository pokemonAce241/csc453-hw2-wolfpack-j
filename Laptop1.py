import socket
import os
import sys
import termios
import fcntl

# default to localhost
TCP_IP = '127.0.0.1'
TCP_PORT = 8080

def main():
    print("test")
    global tcp_ip=TCP_IP,file_name=Null

    # parse the command line arguments
    try:
        opts, args = getopt.getopt(sys.argv[1:], "i:")
    except getopt.GetoptError:
        print('GET OPT ERROR')
    for opt, arg in opts:
        if opt == '-i':
            tcp_ip = arg
        if opt == '-f'
            file_name = arg

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((tcp_ip, TCP_PORT))
    count = 0

   # handle reading and sending from stdin
   if file_name == Null:
        while True:
            message = getch(sys.stdin)
            s.send(message)
            print "message sent:"
    else:
        # handle reading and sending from a file
        fd = open(file_name,"r")
        message = fd.read() # returns one big string
        s.send(message)
        print "message sent"

    s.close()

# function to get a single character from an input file without waiting for a \n character
def getch(file):
  fd = file.fileno()

  oldterm = termios.tcgetattr(fd)
  newattr = termios.tcgetattr(fd)
  newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
  termios.tcsetattr(fd, termios.TCSANOW, newattr)

  oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
  fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)

  try:
    while 1:
      try:
        c = file.read(1)
        break
      except IOError: pass
  finally:
    termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
  return c

print("Test")
main()
