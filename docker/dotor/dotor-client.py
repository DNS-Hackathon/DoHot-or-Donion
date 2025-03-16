import socket, dns, re, hmac
import dns.message as dnsmessage
from hashlib import sha1

hostname_pattern = re.compile(r'^.+(?= IN A)')

dumme_key = b'\x3a\x7b\x1c\x9d\x2e\x0f\x46\x81\x59\xa3\xc7\xe2\xb8\xd4\xf0\x16\x35\x92\x8e\x47'

def form_cell(hostname, secret):

    payload = b'\x03' # Address type 'hostname'
    payload += hostname.encode('utf-8')#.bytes()
    print(payload)
    digest = hmac.new(secret, payload, sha1).digest()
    #print(f'HMAC digest size: {digest.digest_size()}')
    #Cell header
    hex = b'\x00\x04' #circuit_id
    hex += b'\x03' #Cell-type = REALAY
    hex += b'\x02\x00' # payload-size (fixed length 512)
    # RELAY header
    hex += b'\x07' # Type = RELAY_RESOLVE
    hex += b'\x00' # Recognised, flow control and default 0
    hex += b'\x00' #stream-id, 0 means entire circuit
    hex += digest
    hex += b'\x02\x00' # payload-size, repeated,  (fixed length 512)
    # PAYLOAD
    hex+= payload
    for _  in range(512-len(hex)):
        hex += b'\x00'
    
    #Done like this due to some dev-stuff, might change later bu8t it works so....    
    cell = hex
    return cell


def form_cell_dummy(hostname):
    hex = '00' #header
    cell =bytes.fromhex(hex)
    return cell

def extract_hostname(data) -> str:
    message = dnsmessage.from_wire(data)
    hostname= hostname_pattern.search(message.sections[0][0].to_text()).group()
    return hostname

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s_in, socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s_out:
        s_in.bind(('', 1337))
        s_out.bind(('', 9050))
        #s_in.listen()
        while True:
            data, a = s_in.recvfrom(1024)
            hostname = extract_hostname(data)
            print(f'{hostname} has resulted in the following cell (size: {len(form_cell(hostname, dumme_key))}): {form_cell(hostname, dumme_key)}')
            #s_out.send(form_cell_dummy(hostname))


        


        


if __name__ == '__main__':
    main()