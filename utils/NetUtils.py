import socket

# https://stackoverflow.com/questions/19196105/how-to-check-if-a-network-port-is-open
def is_tcp_port_open(host='127.0.0.1', port=80, timeout=5) -> bool:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    result = sock.connect_ex((host, port))
    return result == 0
