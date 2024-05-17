import requests
from tabulate import tabulate
import time
import threading

# List of subdomains to check
subdomains = [
    'http://sub1.awesomeweb',
    'http://sub2.awesomeweb',
    'http://sub3.awesomeweb',    
]

def check_status(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return 'Up'
        else:
            return 'Down'
    except requests.ConnectionError:
        return 'Down'

def monitor_subdomains():
    while True:
        status_table = []
        for subdomain in subdomains:
            status = check_status(subdomain)
            status_table.append([subdomain, status])
        
        # Clear the screen
        print("\033c", end="")
        
        # Print the status table
        print(tabulate(status_table, headers=["Subdomain", "Status"], tablefmt="grid"))
        
        # Wait for 60 seconds before checking again
        time.sleep(60)

if __name__ == "__main__":
    monitor_thread = threading.Thread(target=monitor_subdomains)
    monitor_thread.start()
