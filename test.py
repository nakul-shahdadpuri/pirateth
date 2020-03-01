import requests

print("Enter site to be tested - ")
site = input()
output = requests.get(site)

if output.status_code == 200:
	print("Site can be used")
elif output.status_code >= 500:
	print("Site cannot be used since it is down.")
else:
	print("Check your connection.")