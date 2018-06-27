from bs4 import BeautifulSoup
import requests
import re

def main(urlarg):

	url='https://www.azlyrics.com/lyrics/coldplay/yellow.html'

	if (urlarg):
		url=urlarg
	
	page=requests.get(url)

	soup = BeautifulSoup(page.content , 'html.parser')
	lyrics = soup.find_all("div" , class_=False)
	print(lyrics)
	lyricsStr = str(lyrics)
	lyricsStr=lyricsStr.replace("<br/>","")
	lyricsStr = lyricsStr.replace("")
	lyricsClean=re.sub('[(<.!,;?>/\-)]', '' ,lyricsStr)
	

	#print(lyricsClean)
