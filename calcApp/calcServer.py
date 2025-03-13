import socketserver
import calc
import sys

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            data = self.request.recv(2048).decode("utf-8")
            if (not data):
                break
            exp = calc.validate_expression(data)
            if (not exp):
                self.request.sendall("Invalid expression!".encode())
            else:
                try:
                    res = calc.evaluate_expression(exp)
                    self.request.sendall(f"{res:.2f}".encode())
                except ZeroDivisionError:
                    self.request.sendall("Division by zero!".encode())

if __name__ == "__main__":
    if (len(sys.argv) != 3):
        print(f"Usage: {sys.argv[0]} <ip_addr> <port>")
        exit(1)
    HOST, PORT = sys.argv[1], int(sys.argv[2])

    print(f"Server starting on {HOST}:{PORT}")
    try:
        with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
            server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer closed.")
