from bs4 import BeautifulSoup
import urllib

url = raw_input("Enter the Studyblue Link to Take All the Index Cards: ")

r = urllib.urlopen(url).read()
soup = BeautifulSoup(r, "lxml")

test1 = soup.find_all("div", class_="front")
test2 = soup.find_all("div", class_="back")

front = []
back = []
for element in test1:
	front.append(element.get_text().strip())

for element in test2:
	back.append(element.get_text().strip())

for i in range(len(front)):
	print "------------------------------------------------"
	print front[i]
	print "		" + back[i]
	print "------------------------------------------------"

