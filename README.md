# HTTP Echo Server

A simple HTTP echo server implemented in Python using the built-in `http.server` module.

## Features
- Handles GET and POST requests
- Returns request path and headers for GET requests
- Echoes back POST data
- Runs on port 4000 by default

## Usage

1. Start the server:
   ```bash
   python3 echo_server.py
   ```

2. Test with curl:
   ```bash
   # GET request
   curl http://localhost:4000/test

   # POST request
   curl -X POST -d "Hello World" http://localhost:4000/
   ```

## Requirements
- Python 3.x

## License
MIT