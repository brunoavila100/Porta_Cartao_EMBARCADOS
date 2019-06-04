# Start with a basic flask app webpage.
from flask_socketio import SocketIO, emit
from flask import Flask, render_template, url_for, copy_current_request_context, send_file
from random import random
from time import sleep
from threading import Thread, Event

# Adicional libs
from datetime import datetime
import serial
import csv

__author__ = 'hiroshi.siq'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True

#turn the flask app into a socketio app
socketio = SocketIO(app)

#random number Generator Thread
thread = Thread()
thread_stop_event = Event()

class SerialListener(Thread):
    def __init__(self):
        self.delay = 0.1
        self.names = {"d":"Denys", "b":"Bruno", "n":"Denied"}
        self.com_port = serial.Serial('/dev/ttyACM0', 9600)
        super(SerialListener,self).__init__()

    def readSerial(self):
        while not thread_stop_event.isSet():
            # Read line from serial
            serial_line = str(self.com_port.readline())

            # Check if valid format
            user = 'n'
            print(" ========================= ")
            print(serial_line)
            print(" ========================= ")
            if len(serial_line) == 8:
                user = serial_line[2]
            else:
                continue

            # Log
            with open('/home/wonderboy/rfid-gate/log_file.csv', mode='a') as employee_file:
                employee_writer = csv.writer(employee_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
                if(user == 'n'):
                    employee_writer.writerow(['-', datetime.now().strftime("%I:%M:%S %p"), datetime.now().strftime("%B %d, %Y"), self.names[user]])
                else:
                    employee_writer.writerow([self.names[user], datetime.now().strftime("%I:%M:%S %p"), datetime.now().strftime("%b %d, %Y"), 'Granted'])


            # Emit information
            socketio.emit('newsingin', {'name': self.names[user], 'datetime':datetime.now().strftime("%B %d, %Y - %I:%M:%S %p")}, namespace='/test')

            sleep(self.delay)

    def run(self):
        self.readSerial()

@app.route('/download')
def download():
    try:
        return send_file('/home/wonderboy/rfid-gate/log_file.csv', attachment_filename='log.csv')
    except Exception as e:
        return str(e)

@app.route('/')
def index():
    #only by sending this page first will the client be connected to the socketio instance
    return render_template('index.html')

@socketio.on('connect', namespace='/test')
def test_connect():
    # need visibility of the global thread object
    global thread
    print('Client connected')

    #Start the random number generator thread only if the thread has not been started before.
    if not thread.isAlive():
        print("Starting Thread")
        thread = SerialListener()
        thread.start()

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    socketio.run(app)
