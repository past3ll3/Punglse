# Punglse <br>

Reconnaissance tool designed to iterate through a large list of hosts, identifying those that respond positively to ping requests.

## Basic usage  <br> 
```
python3 punglse.py -h
```
![image](https://github.com/user-attachments/assets/ba7e8e7c-1c33-465d-a3b4-45e368e68039)



Run the script with your list of target : 
```
python3 punglse.py -f list.txt
```
![image](https://github.com/user-attachments/assets/d54751b8-d03c-464b-93b2-10fa055d0b2a)


The hosts list should be one item per line like this : 

![image](https://github.com/user-attachments/assets/09a2048e-19ae-4cbe-a0da-fc5949a360b3)


Run the script with specified waiting time, ping count and max-workers  : 
```
python3 punglse.py -f list.txt -w 0.2 -c 2 -mw 500
```
![image](https://github.com/user-attachments/assets/2457608f-ec72-41c8-8c4c-1f5e5389a0f0)
