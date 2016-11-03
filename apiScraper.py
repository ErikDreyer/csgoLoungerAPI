#!/usr/bin/env python3
import urllib.request
from apiParser import parseAPI

def main():

    print ('Starting api scraper')
    
    outputFileName = 'rawData.txt'
    outputFile = open(outputFileName, "w")
    Counter = 0
    

    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

    url = "https://csgolounge.com/api/matches.php"
    headers={'User-Agent':user_agent,} 

    request=urllib.request.Request(url,None,headers) #The assembled request
    response = urllib.request.urlopen(request)
    data = response.read()
    lines = data.split()

    for line in lines:
        currentLine = line.decode("utf-8")
        try:           
            if currentLine[10:13] == '"a"' and currentLine.find('when') != -1:    
                outputFile.write(currentLine + '\n')
                Counter += 1
        except:
            pass

    outputFile.close()
    print ('Match data scraped from csgolounge.com/api/matches successfully to file:', outputFileName )
    
    parseAPI()
    print ('API scrape and parse finished')
    
if __name__ == '__main__' :
    main()
