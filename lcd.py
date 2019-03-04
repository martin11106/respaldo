import lcddriver
from time import *
from flask import Flask, render_template
from flask_socketio import SocketIO
lcd = lcddriver.lcd()
lcd.lcd_display_string("Bitajor.com", 1)
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
@socketio.on('message')
def handMessage('msg):
	print('menssage'+msg)
	send(msg,broadcast=True)

if __name__ == '__main__':
    socketio.run(app)


