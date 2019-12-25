def find_winner_of_the_day(*match_tuple):
    team1_count =0
    team2_count =0
    for team_name in match_tuple:
        if team_name == "Team1":
            team1_count +=1
        else:
            team2_count +=1

    if team1_count == team2_count:
        return "Tie"
    elif team1_count> team2_count:
        return "Team1"
    else :
        return "Team2"

if __name__ =="__main__":
     print(find_winner_of_the_day("Team1","Team2","Team1"))
     print(find_winner_of_the_day("Team1","Team2"))
     print(find_winner_of_the_day("Team1","Team2","Team2","Team2"))