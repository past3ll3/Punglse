# Punglse : Bulk Ping Tool for Mass Host Scanning
Punglse is an efficient reconnaissance tool designed to quickly iterate through large lists of hosts or URLs, identifying which ones respond to ping requests. If you need to test the availability of multiple hosts at once, Punglse is your go-to solution. Whether for network diagnostics, server availability checks, or security testing, this open-source utility will help you save time by handling thousands of pings in parallel.

# Key Features:
- Bulk Ping Requests: Ping multiple hosts at once from a list.
- Customizable Timeouts: Adjust the wait time for responses to suit your network conditions.
- Threaded Execution: Use multithreading to maximize the speed of large ping operations.
- Detailed Output: Get a summary of available (responsive) hosts.
## Why Use Punglse?
If you're a network engineer, system administrator, or security researcher, you often need to know which hosts are alive across a large number of servers or endpoints. Punglse simplifies this by automating the process and offering multithreaded performance, so you can ping hundreds or even thousands of hosts in seconds.

# Installation
Clone the repository to your local machine:
```
git clone https://github.com/past3ll3/Punglse
```
Navigate to the directory:
```
cd Punglse
```

# Basic Usage
**Quick Start**

Simply provide Punglse with a list of targets to ping:
```
python3 punglse.py -f list.txt
```
The list.txt file should contain one host (IP address or domain) per line:

```
192.168.1.1
google.com
example.com
whatever.google.com
```
# Custom Parameters
You can specify additional options such as wait time, ping count, and number of worker threads:

```
python3 punglse.py -f list.txt -w 0.2 -c 2 -mw 500
```
- -w 0.2 : Set the timeout to 0.2 seconds (default is 0.5 seconds).
- -c 2 : Send 2 ping requests to each host (default is 1 ping).
- -mw 500 : Use up to 500 threads for concurrent ping requests (default is 100).
  
**Full Command Breakdown:**

- -f, --file: Path to the file containing a list of hosts (required).
- -w, --timeout: Time to wait for a ping response in seconds (default: 0.5).
- -c, --count: Number of ping requests to send (default: 1).
- -mw, --max_workers: Max number of threads to use for concurrent pings (default: 100).

# Contributing
We welcome contributions! Please feel free to fork the repository and submit pull requests. If you find any bugs or want additional features, open an issue on GitHub.

# License
This project is licensed under the MIT License.

## Demo

![image](https://github.com/user-attachments/assets/ba7e8e7c-1c33-465d-a3b4-45e368e68039)

![image](https://github.com/user-attachments/assets/d54751b8-d03c-464b-93b2-10fa055d0b2a)

![image](https://github.com/user-attachments/assets/09a2048e-19ae-4cbe-a0da-fc5949a360b3)

![image](https://github.com/user-attachments/assets/2457608f-ec72-41c8-8c4c-1f5e5389a0f0)
