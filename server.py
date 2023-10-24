import socket
import threading
# import wikipedia

IP = socket.gethostbyname(socket.gethostname())
PORT = 5566
ADDR = (IP, PORT)
SIZE = 1023
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"

def handle_client(conn, addr):
    print("[NEW CONNECTION] {addr} connected. ")


    conncted = True
    while conncted:
        msg = conn.recv(SIZE).decode(FORMAT)
        if msg == DISCONNECT_MSG:
            conncted = False
        
        print(f"[{addr} {msg}]")
        msg = f"Msg received: {msg}"
        # msg = wikipedia.summary(msg, sentence=1)
        conn.send(msg.encode(FORMAT))

    conn.close()

def main():
    print("[STARTING] Server menunggu..... ")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print(f"[LISTENING] Server mendengarkan {IP} : {PORT}")


    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
if __name__ == "__main__":
    main()