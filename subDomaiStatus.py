import requests
import time

# List of real-time subdomains to check
subdomains = [
    "http://www.google.com",
    "http://www.github.com",
    "http://www.python.org",
    "http://www.facebook.com"  
]

def check_status(url):
    #Check the HTTP status of a given URL.#
    try:
        response = requests.get(url, timeout=5)  # Timeout after 5 seconds
        return "UP" if response.status_code == 200 else "DOWN"
    except requests.RequestException:
        return "DOWN"

def display_status(statuses):
    #Display the status of the subdomains.#
    print("\nSubdomain Status:")
    print("{:<30} {:<10}".format("Subdomain", "Status"))  # Print headers
    for subdomain, status in statuses.items():
        print("{:<30} {:<10}".format(subdomain, status))  # Print each subdomain and its status

def main():
    #Main function to check and display the status of subdomains.#
    while True:
        statuses = {sub: check_status(sub) for sub in subdomains}  # Check all subdomains
        display_status(statuses)  # Display the results
        time.sleep(60)  # Wait for 1 minute before the next check

if __name__ == "__main__":
    main()
