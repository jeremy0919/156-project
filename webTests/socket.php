<?php
require 'vendor/autoload.php';

use Ratchet\MessageComponentInterface;
use Ratchet\ConnectionInterface;
use Ratchet\WebSocket\WsServer;
use Ratchet\Http\HttpServer;
use Ratchet\IoServer;
class TicTacToeServer implements MessageComponentInterface {
    protected $clients;

    public function __construct() {
        $this->clients = new \SplObjectStorage;
    }

    public function onOpen(ConnectionInterface $conn) {
        $this->clients->attach($conn);
    }

    public function onMessage(ConnectionInterface $from, $msg) {
        foreach ($this->clients as $client) {
            if ($client !== $from) {
                $client->send($msg);
            }
        }
    }

    public function onClose(ConnectionInterface $conn) {
        $this->clients->detach($conn);
    }

    public function onError(ConnectionInterface $conn, \Exception $e) {
        $conn->close();
    }
}

$server = IoServer::factory(
    new HttpServer(
        new WsServer(
            new TicTacToeServer()
        )
    ),
    8080
);

$server->run();
/*

The provided code is a PHP script that defines and creates a WebSocket server using the Ratchet library. Here's a breakdown of what this code does:

1. **Include Composer Autoloader**:
   
   ```php
   require 'vendor/autoload.php';
   ```

   This line includes the Composer autoloader, allowing your script to autoload classes from the installed Composer packages, including the Ratchet library.

2. **Use Statements**:

   ```php
   use Ratchet\MessageComponentInterface;
   use Ratchet\ConnectionInterface;
   use Ratchet\WebSocket\WsServer;
   use Ratchet\Http\HttpServer;
   use Ratchet\IoServer;
   ```

   These `use` statements import classes and interfaces from the Ratchet library, making them available for use in your script.

3. **Class Definition**:

   ```php
   class TicTacToeServer implements MessageComponentInterface {
   ```

   This section defines a PHP class named `TicTacToeServer`, which implements the `MessageComponentInterface` interface. This interface is part of the Ratchet library and provides methods for handling WebSocket connections, messages, and errors.

   The class includes the following methods:

   - `__construct()`: This is the constructor for the `TicTacToeServer` class. It initializes an empty storage (`\SplObjectStorage`) to keep track of connected clients.

   - `onOpen(ConnectionInterface $conn)`: This method is called when a new connection is established. It attaches the connection to the list of clients.

   - `onMessage(ConnectionInterface $from, $msg)`: This method is called when a message is received from a client. It broadcasts the message to all connected clients except the sender.

   - `onClose(ConnectionInterface $conn)`: This method is called when a client connection is closed. It detaches the connection from the list of clients.

   - `onError(ConnectionInterface $conn, \Exception $e)`: This method is called when an error occurs. It closes the connection in response to the error.

4. **WebSocket Server Configuration**:

   ```php
   $server = IoServer::factory(
       new HttpServer(
           new WsServer(
               new TicTacToeServer()
           )
       ),
       8080
   );
   ```

   This section configures and creates a WebSocket server using the Ratchet library. It sets up an HTTP server and WebSocket server using the `HttpServer` and `WsServer` classes, wrapping your `TicTacToeServer` class.

   The WebSocket server will listen on port 8080.

5. **Run the Server**:

   ```php
   $server->run();
   ```

   This line starts the WebSocket server, allowing it to listen for incoming WebSocket connections on port 8080.

In summary, this code defines a WebSocket server using Ratchet, which is designed to handle WebSocket connections, messages, and errors as specified in the `MessageComponentInterface`. It creates the server, wraps it with HTTP and WebSocket server components, and then starts the server to accept WebSocket connections on port 8080.*/
?>

