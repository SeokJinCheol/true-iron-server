from datetime import time

import socketio
import datetime

sio_server = socketio.AsyncServer(
    async_mode = 'asgi',
    cors_allowed_origins=[]
)

sio_app = socketio.ASGIApp(
    socketio_server=sio_server,
    socketio_path='/ws/socket.io'
)

@sio_server.on('connect')
async def connect(sid, environ, auth):
    print(f'{sid}: connected')

@sio_server.on('message')
async def message(sid, data):
    await sio_server.send({
        "user": data['user'],
        "text": data['text'],
        "timestamp": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    })

@sio_server.on('disconnect')
async def disconnect(sid):
    print(f'{sid}: disconnected')