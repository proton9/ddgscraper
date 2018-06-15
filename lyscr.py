import sys
import urllib2
userInput=[]
ddg="http://api.duckduckgo.com/?q="
sizeOfInput=int(len(sys.argv))

print (sizeOfInput)
if (len(sys.argv)>1):
    for i in range (1,sizeOfInput):
    	userInput.append(sys.argv[i])

print(userInput)

query="%20".join(map(str,userInput))
print (query)

print(ddg+query)



