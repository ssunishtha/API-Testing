import requests
url = "https://reqres.in/api/users?page=2"
response = requests.get(url)

#to get the version and copyright of requests library
print(requests.__version__)
print(requests.__copyright__)

url = "https://reqres.in/api/users?page=2"
response = requests.get(url)

#to get all the headers 
print(response.headers)

#to get any specific information
print("SERVER: " + response.headers['server'])
print("CONTENT TYPE: " + response.headers['content-type'])
print("DATE: " + response.headers['date'])
print("CONNECTION: " + response.headers['connection'])
print("VIA: " + response.headers['via'])

#number of response 
print(response)

# the status code tell the status of the request
print( response.status_code)

print(response.content)