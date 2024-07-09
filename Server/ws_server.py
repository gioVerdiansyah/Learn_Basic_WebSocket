from flask import Flask
from flask import request
from flask_socketio import send, SocketIO, emit, join_room, leave_room

app = Flask(__name__)

socketio = SocketIO(app, cors_allowed_origins="*")


@socketio.on('connect')
def socket_connect():
    print(f"[CONNECTED] new user \nSID:{request.sid}")


@socketio.on("message")
def client_on_message(data):
    print(data)
    socketio.emit("response", f"Your message: {data}")


@socketio.on('disconnect')
def socket_disconnect():
    print(f"[DISCONNECTED]: {request.sid}")


if __name__ == "__main__":
    socketio.run(app, debug=True, host="127.0.0.1", port=4545)
