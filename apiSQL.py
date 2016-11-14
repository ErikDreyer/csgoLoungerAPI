#!/usr/bin/env python3
import pymysql
import sys


class Matches:
        """Write the match data to sql database"""

        def __init__(self, match_id, date, time, team_a, team_b, winner, event, closed):
                self.match_id = match_id
                self.date = date
                self.time = time
                self.team_a = team_a
                self.team_b = team_b
                self.winner = winner
                self.closed = closed
                self.event = event


def main():

        print("> Starting SQL writer...")
        
        try:
                sql_host = "127.0.0.1"
                conn = pymysql.connect(host=sql_host, port=3306, user="admin", passwd="erik1998", db="csgoData")
                print("> Connection to database successful...")
        except RuntimeError:
                print("> Connection failed, quitting")
                sys.exit()

        # load the input file
        input_file_name = "matches.txt"
        input_file = open(input_file_name, "r")

        # get the settings file
        settings_file_name = "settings.txt"
        settings_file = open(settings_file_name, "+r")

        matches = input_file.readlines()
        prev_match = settings_file.readline()
        cursor = conn.cursor()

        for match in matches:
                # matchID
                match_id = match[match.find("ID:") + 4: match.find("Date:")]

                # date and time
                match = match[match.find("Date:") + 6:]
                date = match[: match.find(' ')]
                match = match[match.find(" ") + 2:]
                time = match[: match.find(" ")]

                # team_a
                match = match[match.find("Team A") + 8:]
                team_a = match[: match.find(" ")]

                # team_b
                match = match[match.find("Team B") + 8:]
                team_b = match[: match.find(" ")]

                # winner
                match = match[match.find("Winner") + 8:]
                winner = match[: match.find(" ")]

                # event
                match = match[match.find("Event") + 7:]
                event = match[: match.find(" ")]

                # closed
                match = match[match.find("Closed") + 8:]
                closed = match[: match.find(" ")]

                match = Matches(match_id, date, time, team_a, team_b, winner, event, closed)

                if int(match_id) > int(prev_match):
                        sql = """INSERT INTO matches(matchID,matchDate,matchTime,teamA,teamB,winner,eventName,closed)
                        VALUES(%s,'%s','%s',"%s","%s","%s","%s",%s);""" % \
                                (match.match_id, match.date, match.time, match.team_a, match.team_b, match.winner, match.event, match.closed)
                        cursor.execute(sql)
                
        if int(prev_match) < int(match.match_id):
                settings_file.seek(0)
                settings_file.write(match.match_id)

        print("> Data written to database successfully...")
        print("> Committing table and closing connection...")

        # commit and close
        conn.commit()
        conn.close()
        input_file.close()
        settings_file.close()

if __name__ == "__main__":
        main()
