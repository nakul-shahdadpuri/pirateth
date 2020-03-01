import requests
import bs4 as bs
import time
import os

def get_image_type(x):
	l = x.headers.get('content-type')
	return l[6:]


print("Enter the number of pages - ")
number = int(input())
print("Enter the name of the book - ")
name = input()
os.mkdir(name)
print("Enter parent link - ")
parent_link = input()
for i in range(1,number+1):
	raw_html = requests.get(parent_link +str(i)).content


	soup = bs.BeautifulSoup(raw_html,'lxml')
	k = soup.find_all('img')
	link = k[1]['src']


	x = requests.get(link)
	open(name + "/"+str(i)+"."+ get_image_type(x) ,'wb').write(x.content)
	print(i)



