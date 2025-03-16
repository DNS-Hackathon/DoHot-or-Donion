import socket, dns, re, hmac, subprocess
import dns.message as dnsmessage
from hashlib import sha1

hostname_pattern = re.compile(r'^.+(?= IN A)')

def extract_hostname(data) -> str:
    message = dnsmessage.from_wire(data)
    hostname= hostname_pattern.search(message.sections[0][0].to_text()).group()
    return hostname

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s_in:
        s_in.bind(('0.0.0.0', 1337))
        #s_in.listen()
        while True:
            data, a = s_in.recvfrom(1024)
            client_host, client_port = a
            hostname = extract_hostname(data)
            response = subprocess.check_output(['tor-resolve', hostname])
            print(response)
            s_in.sendto(response, (client_host, client_port))


        


        


if __name__ == '__main__':
    main()
