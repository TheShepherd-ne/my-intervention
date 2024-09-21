# Worldcup Results

# (---------------------imports---------------------)

from functools import partial

# (---------------------class---------------------)

class WCG :
    def __init__(self, name) :
        self.name = name

    def teamgoals ( self, i = 0 ) :
        return i

    def wins ( self, win_counts = 0 ) :
        win_counts += 0
        print(f"\t{self.name}'s win counts : {win_counts}")#return win_counts

    def equals (self, equal_counts = 0 ) :
        equal_counts += 0
        print(f"\t{self.name}'s equal counts : {equal_counts}")
    
    def loses (self, losing_counts = 0 ) :
        losing_counts += 0
        print(f"\t{self.name}'s losing counts : {losing_counts}")

    def goaldiffs (self, ig, og) :
        print( ig - og )

# (---------------------def---------------------)
def goalnum (teams, team , goal) :
    goal_counts = 0

    for i in range(0, len(teams)) :
        if   teams[i][0] == team :    goal_counts += goal[i][0]
        elif teams[i][1] == team :    goal_counts += goal[i][1]
    
    return goal_counts

def income_goal (teams, team , goal) :
    income_goal_counts = 0

    for i in range(0, len(teams)) :
        if   teams[i][0] == team :    income_goal_counts += goal[i][1]
        elif teams[i][1] == team :    income_goal_counts += goal[i][0]
    
    return income_goal_counts

def wining (teams, match_res) :
    for t in range( 0, len(teams) ) :
        if match_res[t][0] > match_res[t][1] :
            print(f" {teams[t][0]} is winner")
            if teams[t][0] == "iran" :    iran.wins(1)
            elif teams[t][0] == "spain" :    spain.wins(1)
            elif teams[t][0] == "portugal" :    portugal.wins(1)
            else :    morocco.wins(1)
            if teams[t][1] == "iran" :    iran.loses(1)
            elif teams[t][1] == "spain" :    spain.loses(1)
            elif teams[t][1] == "portugal" :    portugal.loses(1)
            else :    morocco.loses(1)
        
        elif match_res[t][0] < match_res[t][1] :
            print(f" {teams[t][1]} is winner")
            if teams[t][1] == "iran" :    iran.wins(1)
            elif teams[t][1] == "spain" :    spain.wins(1)
            elif teams[t][1] == "portugal" :    portugal.wins(1)
            else :    morocco.wins(1)
            if teams[t][0] == "iran" :    iran.loses(1)
            elif teams[t][0] == "spain" :    spain.loses(1)
            elif teams[t][0] == "portugal" :    portugal.loses(1)
            else :    morocco.loses(1)
        
        else :
            print(f" equal")
            if teams[t][0] == "iran" :    iran.equals(1)
            elif teams[t][0] == "spain" :    spain.equals(1)
            elif teams[t][0] == "portugal" :    portugal.equals(1)
            else :    morocco.equals(1)
            if teams[t][1] == "iran" :    iran.equals(1)
            elif teams[t][1] == "spain" :    spain.equals(1)
            elif teams[t][1] == "portugal" :    portugal.equals(1)
            else :    morocco.equals(1)

# def answr (team_name) :
#     for item in team_name :
#         print (f"{item}  wins: {item.wins} , loses: {item.loses} , draws: {item.draws} , goal difference: {item.goaldiffs}  , points: {item.points}")

# (---------------------Main---------------------)

games = [ ("iran", "spain"), ("iran", "portugal"), ("iran", "morocco"), ("portugal", "spain"), ("spain", "morocco"), ("portugal", "morocco") ]
gresult = [ (2,2), (2,1), (1,2), (2,2), (3,1), (2,1) ]

team_name = ["iran", "spain", "portugal", "morocco"]

iran     = WCG("iran")
spain    = WCG("spain")
portugal = WCG("portugal")
morocco  = WCG("morocco")


iran.goaldiffs(    iran.teamgoals(     goalnum( games, "iran"   , gresult) ), iran.teamgoals(     income_goal(games, "iran",     gresult) ))
spain.goaldiffs(   spain.teamgoals(    goalnum( games, "spain"  , gresult) ), spain.teamgoals(    income_goal(games, "spain",    gresult) ))
portugal.goaldiffs(portugal.teamgoals( goalnum(games, "portugal", gresult) ), portugal.teamgoals( income_goal(games, "portugal", gresult) ))
morocco.goaldiffs( morocco.teamgoals(  goalnum(games, "morocco",  gresult) ), morocco.teamgoals(  income_goal(games, "morocco",  gresult) ))

# print( spain.teamgoals(goal_counts) )
print("\n-------------.: Wins :.-------------")

# iran.wins()
# spain.wins()
# portugal.wins()
# morocco.wins()

wining(games, gresult)
print("\n")

# iran     = { "wins": 0, "loses": 0, "draws": 0, "goaldiffs": 0, "points": 0 }

# output >
# print (f"{team_name}  wins: {wins} , loses: {loses} , draws: {draws} , goal difference: {goaldiffs}  , points: {points}")
# Iran       wins: 1 , loses: 1 , draws: 1 , goal difference: 0  , points: 4
