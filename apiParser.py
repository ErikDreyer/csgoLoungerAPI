#!/usr/bin/env python3
import apiSQL


class Match:
    """parse the data of a match from a line out of the matchData file"""

    def __init__(self, match_id, date, time, team_a, team_b, winner, closed, event):
        self.match_id = match_id
        self.date = date
        self.time = time
        self.team_a = team_a
        self.team_b = team_b
        self.winner = winner
        self.closed = closed
        self.event = event

    def match_to_str(self):
        match_data = 'ID: ' + self.match_id + ' Date: ' + self.date + ' ' + self.time + ' Team A: ' + self.team_a + ' Team B: ' + self.team_b + ' Winner: ' + self.winner + ' Event: ' + self.event + ' Closed: ' + str(self.closed)
        return match_data


def parse_api():

    print('> Starting api parser...')
    input_file_name = 'matchData.txt'
    input_file = open(input_file_name, "r")

    output_file_name = 'matches.txt'
    output_file = open(output_file_name, "w")

    settings_file_name = 'settings.txt'
    settings_file = open(settings_file_name, "r+")

    match_lines = input_file.readlines()

    for match in match_lines:
        match = match[match.find('"match"') + 9:]
        match_id = match[:match.find('"')]

        # date and time
        match = match[match.find('"when"') + 8:]
        date = match[:11]
        time = match[11: match.find('"')]

        # team A
        match = match[match.find('"a"') + 5:]
        team_a = match[:match.find('"')]

        # team B
        match = match[match.find('"b"') + 5:]
        team_b = match[:match.find('"')]

        # winner
        match = match[match.find('"winner"') + 10:]
        winner = match[:match.find('"')]

        if winner == 'a':
            winner = team_a
        if winner == 'b':
            winner = team_b
        if winner == 'c':
            winner = 'draw'

        # closed
        match = match[match.find('"closed"') + 10:]
        closed = match[:match.find('"')]

        if closed == '1':
            closed = 'TRUE'
        if closed == '0':
            closed = 'FALSE'

        # event
        match = match[match.find('"event"') + 9:]
        event = match[:match.find('"')]

        match = Match(match_id, date, time, team_a, team_b, winner, closed, event)

        output_file.write(match.match_to_str() + '\n')

    input_file.close()
    output_file.close()
    settings_file.close()

    print('> Raw match data parsed to textFile:', output_file_name)

    apiSQL.main()

if __name__ == '__main__':
    parse_api()
