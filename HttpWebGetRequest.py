import requests
def get_data(url_address):
    url_test=url_address[0:11]
    if url_test.lower=="http://www.".lower:
        data = requests.get(url_address)
        return data
    else:
        print("Check your url and ensure it starts with http://www.")

print("\t\t\tMAKE URL GET REQUESTS FROM HERE\n")
address=str(input("Please enter the url address you wish to get data from : "))
url_data= get_data(address)
print ("\t\t\tYour data")
try:
    print(url_data.json())
except AttributeError:
    print("We couldn't get data for you due to incorrect url")
