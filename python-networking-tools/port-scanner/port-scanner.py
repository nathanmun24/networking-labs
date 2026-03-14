import socket
import threading

def scan(address, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # Create TCP socket with IPv4 address
    s.settimeout(0.5) # Prevent long delays on closed ports
    result = s.connect_ex((address, port))  # Check to see if port is open by attempting to connect

    if result == 0:
        try:
            service = socket.getservbyport(port)    # Attempt to get service associated with port
        except OSError:
            service = "Unknown"
        print(f"{port} is open ({service})")
    s.close()


target = input("Enter in target IP address: ")

threads = []

# Create a thread for each port
for port in range(1, 10001):
    t = threading.Thread(target=scan , args=(target, port))
    t.start()
    threads.append(t)

# Wait for all threads to finish
for thread in threads:
    thread.join()
