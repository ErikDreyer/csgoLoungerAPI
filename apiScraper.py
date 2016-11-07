#!/usr/bin/env python3
import urllib.request
from apiParser import parseAPI

def main():

    print ('> Starting api scraper...')
    
    outputFileName = 'rawData.txt'
    outputFile = open(outputFileName, "w")
    Counter = 0    

    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

    url = "https://csgolounge.com/api/matches.php"
    headers={'User-Agent':user_agent,} 

    request=urllib.request.Request(url,None,headers) #The assembled request
    response = urllib.request.urlopen(request)
    data = response.read()

    outputFile.write(data.decode("utf-8"))

    outputFile.close()
    print ('> Match data scrapped to:', outputFileName )

    print ('> Sorting data into seperate matches...')
    
    inputFileName = 'rawData.txt'
    outputFileName = 'matchData.txt'
    inputFile = open(inputFileName, "r")
    outputFile = open(outputFileName, "w")
    

    data = inputFile.read()
    data = data[1:]

    while len(data) > 1:
        match = data[:data.find('}') + 1]
        data = data[data.find('}') + 2:]
        outputFile.write(match + '\n')         

    outputFile.close()

    print ('> API scrape finished...')
    parseAPI()

    print ('> Done!')
    
    
if __name__ == '__main__' :
    main()

