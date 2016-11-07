import pymysql
import sys

class matchesSQL:
	"Write the match data to sql database"

	def __init__(self, matchID, date, time, teamA, teamB, winner, event, closed):
		self.matchID = matchID
		self.date = date
		self.time = time
		self.teamA = teamA
		self.teamB = teamB
		self.winner= winner
		self.closed = closed
		self.event = event	


#disconnect form database
def disconnectFromDataBase():
	conn.commit()
	conn.close()


	

def closeTextFiles():
	#close text files

	inputFile.close()
	settingsFile.close()

#main        
def main():
	
	print("> Starting SQL writer...")
	
	try:
		SQLhost = "127.0.0.1"
		conn = pymysql.connect(host=SQLhost, port=3306, user="admin", passwd="erik1998", db="csgoData")
		print ("> Connection to database successful...")
	except:
		print("> Connection failed, quitting")
		sys.exit()

	#load the input file
	inputFileName = "matches.txt"
	inputFile = open(inputFileName, "r")

	#get the settings file
	settingsFileName = "settings.txt"
	settingsFile = open(settingsFileName, "r")

	matches = inputFile.readlines()

	cur = conn.cursor()

	for match in matches:
		#matchID
		matchID = match[match.find("ID:") + 4: match.find("Date:")]

		#date and time
		match = match[match.find("Date:") + 6:]
		date =  match[: match.find(' ')]
		match = match[match.find(" ") + 2:]
		time = match[: match.find(" ")]

		#teamA
		match = match[match.find("Team A") + 8:]
		teamA = match[: match.find(" ")]

		#teamB
		match = match[match.find("Team B") + 8:]
		teamB = match[: match.find(" ")]

		#winner
		match = match[match.find("Winner") + 8:]
		winner = match[: match.find(" ")]

		#event
		match = match[match.find("Event") + 7:]
		event = match[: match.find(" ")]

		#closed
		match = match[match.find("Closed") + 8:]
		closed = match[: match.find(" ")]


		match = matchesSQL(matchID, date, time, teamA, teamB, winner, event, closed)
		sql = """INSERT INTO matches(matchID,matchDate,matchTime,teamA,teamB,winner,eventName,closed) VALUES(%s,'%s','%s',"%s","%s","%s","%s",%s);""" % (match.matchID, match.date, match.time, match.teamA, match.teamB, match.winner, match.event, match.closed) 
		#print(sql)
		cur.execute(sql)

	print ("> Data written to database successfully...")
	print ("> Committing table and closing connection...")
	conn.commit()
	conn.close()

if __name__ == "__main__":
	main()
