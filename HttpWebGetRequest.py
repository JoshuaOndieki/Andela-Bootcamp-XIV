import requests
from socket import *
import urllib
def get_data(url_address):
    url_test=url_address[0:7]
    if url_test=="http://":
        data = requests.get(url_address,timeout=10)
        return data
    else:
        print("Check your url and ensure it starts with http://")

print("\t\t\tMAKE URL GET REQUESTS FROM HERE\n")
address=str(input("Please enter the url address you wish to get data from : "))
url_data= get_data(address)
print ("\t\t\tYour data")
try:
    print(url_data.json())
except AttributeError:
    print("We couldn't get data for you due to incorrect url")
except TimeoutError:
    print("Timed Out")