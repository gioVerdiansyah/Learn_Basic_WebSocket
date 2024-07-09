import socketio

sio = socketio.Client()


@sio.event
def connect():
    print('connection established')
    while True:
        msg = input("Sent a message: ")
        sio.emit('message', msg)


@sio.event
def my_message(data):
    print('message received with ', data)


@sio.event
def disconnect():
    print('disconnected from server')


sio.connect(url='ws://127.0.0.1:4545')
sio.wait()
