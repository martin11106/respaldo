import lcddriver
from time import *
from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handleMessage(msg):
    print('Message: ' + msg)
    lcd = lcddriver.lcd()
    lcd.lcd_display_string(msg, 1)	
    send(msg, broadcast = True)
	
if __name__ == '__main__':
    socketio.run(app,host='192.168.137.207',port=4000)
