import { useEffect } from "react";
import { io } from "socket.io-client";

// const socket = io("ws://localhost:4545/", {
//   rejectUnauthorized: false,
//   transports: ["websocket"],
// });

const WebSocketComponent = () => {
  const socket = io("ws://127.0.0.1:4545");
  useEffect(() => {
    socket.emit('message', "hello server")
    socket.on('response', (data) => {
      console.log(data)
    })
  }, []);

  return (
    <div>
      <h1>WebSocket Communication</h1>
      <p>Check console for incoming messages.</p>
    </div>
  );
};

export default WebSocketComponent;
