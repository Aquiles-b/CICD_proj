import socket, sys

if __name__ == "__main__":
    client_fd = socket.socket()
    if (len(sys.argv) != 3):
        print(f"Usage: {sys.argv[0]} <ip_address> <port>")
        exit(1)

    ip = sys.argv[1]
    port = int(sys.argv[2])

    client_fd.connect((ip, port))

    try:
        print("(Welcome to Calc App! Type help for help.)")
        while True:
            inp = input("> ")
            if (inp == ""):
                continue
            if (inp in "quit"):
                print("Bye")
                break
            client_fd.send(inp.encode())
            res = client_fd.recv(2048).decode("utf-8")
            if (not res):
                print("Connection lost!")
                break
            print(f"= {res}")

    except KeyboardInterrupt:
        print("\nBye")
