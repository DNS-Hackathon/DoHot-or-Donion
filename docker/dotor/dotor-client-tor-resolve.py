import socket, dns, re, hmac, subprocess, dns.resolver
import dns.message as dnsmessage
from hashlib import sha1

hostname_pattern = re.compile(r'^.+(?= IN A)')

def extract_hostname(data):
    message = dnsmessage.from_wire(data)
    hostname= hostname_pattern.search(message.sections[0][0].to_text()).group()
    return hostname, message.id


def main():
    r_sample = dns.resolver.resolve('netnod.se')
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s_in:
        s_in.bind(('', 1337))
        #s_in.listen()
        while True:
            data, a = s_in.recvfrom(1024)
            client_host, client_port = a
            hostname, id = extract_hostname(data)
            correct_id = id.to_bytes(2,'big')
            r_sample.id=id #doesn't work
            q_r = dnsmessage.from_wire(r_sample.response.to_wire())
            response = subprocess.check_output(['tor-resolve', hostname])
            q = q_r.to_wire() 
            b_tmp = bytearray(q)
            b_tmp[0] = correct_id[0] #this is so inelegant its not ok, but i have like 5min
            b_tmp[1] = correct_id[1]
            q = bytes(b_tmp)
            print(f'{response} with id {id} from {client_host} at port {client_port}\nSent (id:{q_r.id}):\n{q}\n')
            s_in.sendto(q, a)


        


        


if __name__ == '__main__':
    main()
