// Socket.io event handlers for real-time features

const socketHandler = (io) => {
  // Store connected users
  const connectedUsers = new Map();

  io.on('connection', (socket) => {
    console.log(`✅ User connected: ${socket.id}`);

    // User joins with their ID
    socket.on('user:join', (userId) => {
      connectedUsers.set(userId, socket.id);
      socket.userId = userId;
      
      // Notify others that user is online
      socket.broadcast.emit('user:online', userId);
      
      console.log(`User ${userId} joined`);
    });

    // User sends a message in community forum
    socket.on('forum:message', (data) => {
      io.emit('forum:new-message', {
        ...data,
        timestamp: new Date()
      });
    });

    // Real-time notification
    socket.on('notification:send', (data) => {
      const { recipientId, notification } = data;
      const recipientSocketId = connectedUsers.get(recipientId);
      
      if (recipientSocketId) {
        io.to(recipientSocketId).emit('notification:receive', notification);
      }
    });

    // Donation received (notify admins)
    socket.on('donation:new', (donation) => {
      // Broadcast to all admin users
      io.emit('donation:received', donation);
    });

    // Student progress update
    socket.on('student:progress', (data) => {
      const { studentId, progress } = data;
      
      // Notify assigned volunteers
      io.emit('student:progress-update', {
        studentId,
        progress,
        timestamp: new Date()
      });
    });

    // Typing indicator for chat
    socket.on('chat:typing', (data) => {
      socket.broadcast.emit('chat:user-typing', {
        userId: socket.userId,
        ...data
      });
    });

    // User disconnects
    socket.on('disconnect', () => {
      if (socket.userId) {
        connectedUsers.delete(socket.userId);
        socket.broadcast.emit('user:offline', socket.userId);
        console.log(`User ${socket.userId} disconnected`);
      }
      console.log(`❌ User disconnected: ${socket.id}`);
    });

    // Error handling
    socket.on('error', (error) => {
      console.error('Socket error:', error);
    });
  });

  // Helper function to emit to specific user
  io.emitToUser = (userId, event, data) => {
    const socketId = connectedUsers.get(userId);
    if (socketId) {
      io.to(socketId).emit(event, data);
    }
  };

  // Helper function to emit to specific role
  io.emitToRole = (role, event, data) => {
    io.emit(`${role}:${event}`, data);
  };

  return io;
};

module.exports = socketHandler;
