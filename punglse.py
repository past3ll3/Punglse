import subprocess
import sys
import time
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed

line = ''.join("\033[96m+\033[0m" if i % 2 == 0 else "\033[94m+\033[0m" for i in range(67))
banner = """                       

    8888888b.                             888                   
    888   Y88b                            888                   
    888    888                            888                   
    888   d88P 888  888 88888b.   .d88b.  888 .d8888b   .d88b.  
    8888888P"  888  888 888 "88b d88P"88b  888 88K      d8P  Y8b 
    888        888  888 888  888 888  888  888 "Y8888b. 88888888 
    888        Y88b 888 888  888 Y88b 888  888      X88 Y8b.     
    888         "Y88888 888  888  "Y88888 888  88888P'  "Y8888  
                                      888                       
                                 Y8b d88P                       
                                  "Y88P"                        

                                                               v1.0     
"""

def check_ping(host, wait_time, count):
    ping_command = ["ping", "-c", str(count), "-W", str(wait_time), host]

    try:
        subprocess.run(ping_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        print(f"\033[92m{host} is up\033[0m")
        return True
    except subprocess.CalledProcessError:
        print(f"\033[91m{host} is down\033[0m")
        return False

class CustomArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write(f'\033[91mError: {message}\033[0m\n')
        self.print_help()
        sys.exit(2)

def introduction():
    print("\033[94m\n" + line + "\033[0m")
    print("\033[96m" + banner + "\033[0m")
    print("\033[94m" + line + "\033[0m")
    print("\033[97m- Reconnaissance tool designed to iterate through a list of hosts, \n  identifying those that respond positively to ping requests.\033[0m")
    print("\033[94m" + line + "\033[0m")

def main():
    introduction()

    parser = CustomArgumentParser(description='Reconnaissance tool for pinging a list of hosts.')
    parser.add_argument('-f', '--file', required=True, help='Path to the file containing the list of hosts')
    parser.add_argument('-w', '--timeout', type=float, default=0.5, help='Time to wait for a response in seconds (minimum: 0.2)')
    parser.add_argument('-c', '--count', type=int, default=1, help='Number of ping requests to send (minimum: 1)')

    args = parser.parse_args()
    filename = args.file
    wait_time = max(args.timeout, 0.2)  # Ensure wait time is at least 0.2 seconds
    count = max(args.count, 1)  # Ensure count is at least 1

    start_time = time.time()
    total_count = 0
    positive_count = 0
    up_hosts = []

    try:
        with open(filename, 'r') as file:
            hosts = [host.strip() for host in file]

        with ThreadPoolExecutor(max_workers=100) as executor:
            future_to_host = {executor.submit(check_ping, host, wait_time, count): host for host in hosts}

            for future in as_completed(future_to_host):
                host = future_to_host[future]
                total_count += 1
                if future.result():
                    positive_count += 1
                    up_hosts.append(host)

    except FileNotFoundError:
        print(f"\033[91mError: File '{filename}' not found.\033[0m")
        sys.exit(1)

    elapsed_time = time.time() - start_time
    minutes, seconds = divmod(elapsed_time, 60)

    print("\033[94m" + line + "\033[0m")  # Blue text
    print(f"\033[97m{total_count} hosts scanned in {int(minutes)}m{int(seconds)}s\033[0m")
    print(f"\033[97mFound \033[92m{positive_count}\033[97m hosts available :\033[0m")
    
    if up_hosts:
        for host in up_hosts:
            print("\033[92m" + host + "\033[0m")

    print("\033[94m" + line + "\033[0m")  

if __name__ == "__main__":
    main()