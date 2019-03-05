from flask import Flask, render_template
from flask_socketio import SocketIO
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)
@app.route('/')
def index():
	return "hello"
@socketio.on('message')
def handMessage(msg):
	print('menssage'+msg)
	send(msg,broadcast=True)

if __name__ == '__main__':
    socketio.run(app,host='192.168.137.207', port=5000)
