import os, pathlib, argparse, webbrowser
current_path = pathlib.Path(__name__).absolute().parent

def serverNow(host, port):
    webbrowser.open_new_tab('http://{}:{}'.format(host, port))
    os.system('php -S {}:{}'.format(host, port))
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', help='Host: Localhost')
    parser.add_argument('--port', help='Port: 8000')
    arguments = parser.parse_args()
    host = ''
    port = ''
    
    if arguments.host == None:
        host = 'localhost'
    else:
        host = arguments.host
    if arguments.port == None:
        port = 8000
    else:
        port = int(arguments.port)
    serverNow(host, port)
    print('Working')