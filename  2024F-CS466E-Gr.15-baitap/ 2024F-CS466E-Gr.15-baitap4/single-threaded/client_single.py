import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12346))
    
    while True:
        message = input("Enter a message to send to the server (or type 'exit' to quit): ")
        if message.lower() == 'exit':
            break
        client_socket.send(message.encode('utf-8'))
        
        try:
            response = client_socket.recv(1024).decode('utf-8')
            print(f"Response from server: {response}")
        except ConnectionAbortedError:
            print("Connection to the server was lost.")
            break
    
    client_socket.close()

if __name__ == "__main__":
    start_client()
