from bs4 import BeautifulSoup
import sys
import requests
from urllib.parse import unquote #take this off if it breaks 
								 #code
ddgfooter=''
userInput=[]
ddg="https://duckduckgo.com/html?q="
#ddgfooter="+site%3Aazlyrics.com" use this to look
								# for resulst in 1 particular 
								#site
sizeOfInput=int(len(sys.argv)) #count command line args




print (sizeOfInput)
if (len(sys.argv)>1):
    for i in range (1,sizeOfInput):
    	userInput.append(sys.argv[i])

print(userInput)

#query="%20".join(map(str,userInput))

query="+".join(userInput)
print (query)
url=ddg+query+ddgfooter
print(url)

page=requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
firstLink=soup.find_all(class_="result__a")
#print(firstLink)
#print(firstLink[0])

print(firstLink[0]['href']) #printing the href value
strurl = unquote(firstLink[0]['href']) #getting clean url
noeqto=strurl.split("uddg=") #getting rid of a ddg custom tag
print(noeqto[1])			         #clean url lies after '='
						#that's in the 2nd element
						#of the list

#print(fistLink.prettify())
#print(page.content)





