import socket
import pickle
import re


def parser(data):
    split_str = re.split(r' ', data)
    split_str = validator(split_str)
    split_str[2] = split_str[2][:-2]
    return split_str


def validator(split_str):
    if len(split_str) == 4:
        if re.match(r'\d{2}:\d{2}:\d{2}.\d{3}', split_str[2]) is None:
            split_str[0] = 'Error'
        elif re.match(r'\d{4}', split_str[0]) is None:
            split_str[0] = 'Error'
        elif re.match(r'\w{2}', split_str[1]) is None:
            split_str[0] = 'Error'
        elif re.match(r'\d{2}', split_str[3]) is None:
            split_str[0] = 'Error'
    else:
        split_str = ['Error', 'Error', 'Error', 'Error']
    return split_str


if __name__ == "__main__":
    serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
    serv_sock.bind(('', 7777))
    serv_sock.listen(10)
    while True:
        connection = None
        try:
            client_sock, client_addr = serv_sock.accept()
            print('Connected by', client_addr)
            while True:
                data = client_sock.recv(1024)
                if not data:
                    break
                split_str = parser(data.decode('utf-8'))
                data_string = pickle.dumps(split_str)
                client_sock.send(data_string)
        except KeyboardInterrupt:
            if connection:
                connection.close()
            break
