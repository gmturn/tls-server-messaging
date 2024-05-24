# Documentation

### Contents
1. Overview
2. Installation and Setup
3. Usage

## Overview
This project si a simple messaging program that utilizes a client and server SSL wrapped socket. The client connects to the server via the specified port in the .conf file. The client and server can then send secure messages through TLS. The connection terminates when the client disconnects from the server.

## Installation and Setup
Run the following command in your terminal:
`git clone https://github.com/gmturn/tls-server-messaging/`

Run the `setup.py` file by executing the following command in your terminal:
`pip install -e .`

## Usage
To run either the client or server script, enter one of the following commands into your terminal:
- `python scripts/run_server.py`
- `python scripts/run_client.py`
