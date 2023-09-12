import os

def ping(ip_address):
    response = os.system("ping -c 1 " + ip_address + " > /dev/null 2>&1")
    if response == 0:
        return True
    else:
        return False

def read_file(file_name):
    with open(file_name, 'r') as f:
        ip_list = f.readlines()
    return ip_list

def main():
    file_name = "ip_list.txt"
    ip_list = read_file(file_name)
    for ip in ip_list:
        ip = ip.strip()  # remove leading/trailing whitespace
        if ping(ip):
            print(ip + " is reachable")
        else:
            print(ip + " is not reachable")

if __name__ == '__main__':
    main()
