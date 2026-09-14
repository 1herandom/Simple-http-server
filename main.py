from time import sleep
import socket
import os

def main():
    HOST =  "0.0.0.0"
    PORT = 8069
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s :  
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
            s.bind((HOST, PORT))
            s.listen(5)

            print("Server is listening on port", PORT)
            while (True):
                    
                client_socket, client_add = s.accept()
                

                recive = client_socket.recv(1500).decode()
                
                print(recive)
                headers = recive.split("\n")
                first_header_comp = headers[0].split()

                http_method = first_header_comp[0]
                request_url = first_header_comp[1][1:]
                print(request_url)
                msg = str()
                if request_url == "":
                    request_url = "index.html"


                if http_method == 'GET':

                    if os.path.exists(request_url) :
                        fil = open(request_url)
                        content = fil.read()

                        msg = ('HTTP/1.1 200 OK\n\n' + content)
                    else:
                        msg = ('HTTP/1.1 404 Not Found\n\nFile not found')
                        print("File not found")
                else:

                    msg = ('HTTP/1.1 405 Method Not Allowed\n\nAllow: GET')

                client_socket.sendall(msg.encode())

                client_socket.close()
    except KeyboardInterrupt:
       print("\n surver sutting down ") 
    finally: 
        s.close()

    

main()
