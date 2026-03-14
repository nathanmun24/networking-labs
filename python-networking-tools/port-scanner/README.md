# Python Port Scanner

Simple multithreaded TCP port scanner

## Features
- TCP port scanner
- Multithreaded scanning for faster execution time
- Port range is configurable
- Timeout configured to handle hanging connection

## What it Does

1. The program creates a TCP socket
2. The port is scanned with socket.connect_ex()
3. When there is a successful connection (result == 0), port is open
4. The program tries to identify the service on the port
5. Threading allows for multiple ports to be scanned simultaneously

## Example Output
135 is open (epmap)
445 is open (microsoft-ds)
4511 is open (Unknown)

## Running the Program
- `python port_scanner.py`
Then enter in the targer IP address

## Used Techologies
- Python
- Threading
- Socket Library
