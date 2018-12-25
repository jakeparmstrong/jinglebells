"""A simple program that displays datagrams received on a port."""
#JAKE USe PYTHON 3
import argparse
import socket
import RPi.GPIO as GPIO
import time

#GPIO Pin constants
C = 8
D = 25
E = 24
F = 23
G = 18
A = 15
B = 14

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(C, GPIO.OUT)
GPIO.setup(D, GPIO.OUT)
GPIO.setup(E, GPIO.OUT)
GPIO.setup(F, GPIO.OUT)
GPIO.setup(G, GPIO.OUT)
GPIO.setup(A, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)


def switcher(argument):
  switchy = {
  "g" : 8,
  "a" : 25,
  "b" : 24,
  "c" : 23,
  "d" : 18,
  "e" : 15,
  "f" : 14
  }
  return switchy.get(argument, "not found")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--ip",
        default="127.0.0.1",
        help="The ip to listen on")
    parser.add_argument(
        "--port",
        type=int,
        default=4585,
        help="The port to listen on")

    args = parser.parse_args()
    _PrintOscMessages(args.ip, args.port)


def _PrintOscMessages(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ip, port))
    print("Listening for UDP packets on {0}:{1} ...".format(ip, port))
    while True:
        data, _ = sock.recvfrom(1024)
        stringed_data = str(data)
        octave = stringed_data[2]
        pitch = stringed_data[4]

        pin = switcher(pitch)
        GPIO.output(pin, True)
        time.sleep(0.15)
        GPIO.output(pin, False)
        #print("Pitch:"+pitch+" | Octave: "+octave)  #debug

if __name__ == "__main__":
    main()
