import socket

def scan_port(target, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)

    result = scanner.connect_ex((target, port))

    scanner.close()

    if result == 0:
        return True
    else:
        return False


target = input("Enter target IP or website: ")

ports = [21, 22, 80, 443, 3306, 8080]

print("\nScanning target:", target)
print("----------------------")

for port in ports:
    if scan_port(target, port):
        print(f"Port {port} is OPEN")
    else:
        print(f"Port {port} is CLOSED")