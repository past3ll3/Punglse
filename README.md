# Punglse
Reconnaissance tool designed to iterate through a list of hosts, identifying those that respond positively to ping requests.

## Basic usage  <br> 
```
python3 punglse.py -h
```
![image](https://github.com/user-attachments/assets/5e69b4ab-cee8-4132-8fbe-e28835a5b870)


Run the script with your list of target : 
```
python3 punglse.py -f list.txt
```
![image](https://github.com/user-attachments/assets/21b52d87-6f12-4371-857a-6673336472f0)

The hosts list should be one item per line like like this : 

![image](https://github.com/user-attachments/assets/4039a134-f428-4fe4-bb41-c7063731897e)

Run the script with specified waiting time and ping amount  : 
```
python3 punglse.py -f list.txt -w 0.2 -c 2
```
![image](https://github.com/user-attachments/assets/501dcbb4-8b48-434c-9426-2f7239d5a63c)
