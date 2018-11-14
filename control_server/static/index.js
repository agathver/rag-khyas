const socket = io();

document.addEventListener('keypress', event => {
  const key = event.key;

  switch (key) {
    case 'w':
      socket.emit('move forward');
      break;
    case 'a':
      socket.emit('turn left');
      break;
    case 's':
      socket.emit('move backward');
      break;
    case 'd':
      socket.emit('turn right');
      break;
    case 'ArrowLeft':
      socket.emit('rotate arm left');
      break;
    case 'ArrowRight':
      socket.emit('rotate arm right');
      break;
    case ' ':
      socket.emit('break');
      break;
    default:
      console.log(key);
    //   socket.emit('move forward');
      break;
  }
});
