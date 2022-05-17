import socket
import pickle


def print_log(data_variable):
    file = open('tmp/log.txt', 'a')
    check = True
    line = 'Incorrect value'
    if data_variable[0] != 'Error':
        line = f"спортсмен, нагрудный номер {data_variable[0]} \
прошёл отсечку {data_variable[1]} в «{data_variable[2]}»"
        file.write(line + '\n')
    else:
        file.write(line + '\n')
        check = False
    file.close()
    return line, check


if __name__ == "__main__":
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.connect(('localhost', 7777))
    while True:
        connection = None
        try:
            print('Введите данные:')
            send_data = input()
            client_sock.sendall(send_data.encode('utf-8'))
            data = client_sock.recv(1024)
            data_variable = pickle.loads(data)
            line, bool = print_log(data_variable)
            if bool is False:
                continue
            if data_variable[3] == '00':
                print(line)
        except KeyboardInterrupt:
            if connection:
                connection.close()
            break
