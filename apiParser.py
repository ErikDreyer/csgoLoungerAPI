import apiSQL

class Match:
    "parse the data of a match from a line out of the matchData file"

    def __init__(self, matchID, date, time, teamA, teamB, winner, closed, event, form):
        self.matchID = matchID
        self.date = date
        self.time = time
        self.teamA = teamA
        self.teamB = teamB
        self.winner = winner
        self.closed = closed
        self.event = event
        self.form = form

    def matchToStr(self):
        matchData = 'ID: ' + self.matchID + ' Date: ' + self.date + ' ' + self.time + ' Team A: ' + self.teamA + ' Team B: ' + self.teamB + ' Winner: ' + self.winner + ' Event: ' + self.event + ' Closed: ' + str(self.closed)
        return matchData


def parseAPI():

    print ('> Starting api parser...')
    inputFileName = 'matchData.txt'
    inputFile = open(inputFileName , "r")
    outputFileName = 'matches.txt'
    outputFile = open(outputFileName, "w")
    settingsFileName = 'settings.txt'
    settingsFile = open(settingsFileName, "r+")

    matches = inputFile.readlines()

    for match in matches:
        match = match[match.find('"match"') + 9:]
        matchID = match[:match.find('"')]

        #date and time
        match = match[match.find('"when"') + 8:]
        date = match[:11]
        time = match[11: match.find('"')]

        #team A
        match = match[match.find('"a"') + 5:]
        teamA = match[:match.find('"')]

        #team B
        match = match[match.find('"b"') + 5:]
        teamB = match[:match.find('"')]

        #winner
        match = match[match.find('"winner"') + 10:]
        winner = match[:match.find('"')]

        if winner == 'a':
            winner = teamA
        if winner == 'b':
            winner = teamB
        if winner == 'c':
            winner = 'draw'

        #closed
        match = match[match.find('"closed"') + 10:]
        closed = match[:match.find('"')]

        if closed == '1':
            closed = 'TRUE'
        if closed == '0':
            closed = 'TRUE'

        #event
        match = match[match.find('"event"') + 9:]
        event = match[:match.find('"')]

        #form
        match  = match[match.find('"format"') + 10:]
        form = match[:match.find('"')]

        objMatch = Match(matchID, date, time, teamA, teamB, winner, closed, event, form)

        outputFile.write(objMatch.matchToStr() + '\n')


    previousMatch = settingsFile.readline()
    runSQL = False
    
    
    if int(previousMatch) < int(objMatch.matchID):
        settingsFile.seek(0)
        settingsFile.write(objMatch.matchID)
        runSQL = True
    else:
        runSQL = False
        print (previousMatch, objMatch.matchID)
        
    inputFile.close()
    outputFile.close()
    settingsFile.close()
    print ('> Raw match data parsed to textFile:', outputFileName)

    if runSQL == True:
        print ("> SQL database not up to date, updating...")
        apiSQL.main()
    else:
        print("> SQL database up to date, quitting")

if __name__ == '__main__':
    parseAPI()

