
import socket


def Main():
    host = '127.0.0.1'

    port = 12486

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    sep = ''
    print('Send \"Thanks\" to exit conversation')
    print('Please wait for your turn')
    s.send('Hello Sir!!'.encode('ascii'))

    while True:

        try:
            data = s.recv(4096)
            print('Server :', str(data.decode('ascii')))
        except socket.error:
            # nothing recieved
            print('')

        message = input('Reporter : ')
        s.send(message.encode('ascii'))

        if message == 'Thanks':
            s.close()
            break
        else:
            continue
    s.close()


if __name__ == '__main__':
    Main()