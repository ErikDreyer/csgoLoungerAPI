#!/usr/bin/env python3
import urllib.request
from apiParser import parse_api


def main():

    print('> Starting api scraper...')
    
    output_file_name = 'rawData.txt'
    output_file = open(output_file_name, "w")
    counter = 0

    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

    url = "https://csgolounge.com/api/matches.php"
    headers = {'User-Agent': user_agent, }

    request = urllib.request.Request(url, None, headers) # The assembled request
    response = urllib.request.urlopen(request)
    data = response.read()

    output_file.write(data.decode("utf-8"))

    output_file.close()
    print('> Match data scraped to:', output_file_name )

    print('> Sorting data into separate matches...')
    
    input_file_name = 'rawData.txt'
    output_file_name = 'matchData.txt'
    input_file = open(input_file_name, "r")
    output_file = open(output_file_name, "w")

    data = input_file.read()
    data = data[1:]

    while len(data) > 1:
        match = data[:data.find('}') + 1]
        data = data[data.find('}') + 2:]
        output_file.write(match + '\n')

    output_file.close()

    print('> API scrape finished...')
    parse_api()

    print('> Done!')
    input("Press Enter to exit...")
    
if __name__ == '__main__':
    main()

