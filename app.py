from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def root():
    return render_template('main.html')

@socketio.on('connect')
def response():
    print 'User connected'

@socketio.on('message')
def chat_response(msg):
    print 'Message from Client: {}'.format(msg)
    #socketio.emit('chat message', msg)

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0')
