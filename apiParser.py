def parseAPI():

    print ('Starting api parser')
    
    inputFileName = 'rawData.txt'
    outputFileName = 'matchData.txt'
    inputFile = open(inputFileName, "r")
    outputFile = open(outputFileName, "w")
    
    Counter = 0

    with inputFile as f:
        matches = f.readlines()

    for match in matches:
        #get time of match
        time = match[:8]

        #get teamA of match
        tagPos = match.find('"a"')
        match = match[tagPos + 4:]
        commaPos = match.find(',')
        teamA = match[:commaPos]

        #get teamB of match
        tagPos = match.find('"b"')
        match = match[tagPos + 4:]
        commaPos = match.find(',')
        teamB = match[:commaPos]

        #get winner of match
        tagPos = match.find('"winner"')
        match = match[tagPos + 9:]
        commaPos = match.find(',')
        winner = match[1:commaPos-1]

        if winner == 'a':
            winner = teamA
        if winner == 'b':
            winner = teamB
        if winner == 'c':
            winner = 'Draw'

        #get closed value of match
        tagPos = match.find('"closed"')
        match = match[tagPos + 9:]
        commaPos = match.find(',')
        closed = match[1:commaPos-1]

        if closed == '1':
            closed = True
        if closed == '0':
            closed = False
            
        #get event name of match
        tagPos = match.find('"event"')
        match = match[tagPos + 8:]
        commaPos = match.find(',')
        event = match[:commaPos]

        #get match ID
        tagPos = match.find('"match"')
        match = match[tagPos + 8:]
        commaPos = match.find(',')
        ID = match[1:commaPos-1]
        
        #get date
        match = match[match.find('when') + 7:]
        date = match[:10]

        output = 'ID:' +  ID + ' Date:' + date + ' Team A:'+ teamA + ' Team B:'+ teamB + ' Winner:'+ winner + ' Closed:' + str(closed) + ' Event:' + event   
        outputFile.write(output)
        
    inputFile.close()
    outputFile.close()
    print ('Raw match data parsed to textFile:', outputFileName)

if __name__ == '__main__':
    parseAPI()
