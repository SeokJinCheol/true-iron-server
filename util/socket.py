import socketio

sio_server = socketio.AsyncServer(
    async_mode = 'asgi',
    cors_allowed_origins=[]
)

sio_app = socketio.ASGIApp(
    socketio_server=sio_server,
    socketio_path='/ws/socket.io'
)

@sio_server.on('join')
async def join(sid, data):
    print(f'{sid} :: {data}')
    await sio_server.enter_room(sid, data['room'])

@sio_server.on('connect')
async def connect(sid, environ, auth):
    print(f'{sid}: connected')

@sio_server.on('message')
async def message(sid, data):
    room = data.get('room')
    message = data.get('message')
    await sio_server.send(message, room)

@sio_server.on('disconnect')
async def disconnect(sid):
    print(f'{sid}: disconnected')