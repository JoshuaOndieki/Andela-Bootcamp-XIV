import requests
def get_data(url_address):
    data=requests.get(url_address)
    return data
print("\t\t\tMAKE URL GET REQUESTS FROM HERE\n")
url_data= get_data(input("Please enter the url address you wish to get data from : "))
print ("\t\t\tYour data")
print(url_data.json())