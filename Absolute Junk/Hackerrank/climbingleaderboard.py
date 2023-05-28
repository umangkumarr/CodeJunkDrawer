
def climbingLeaderboard(ranked, player):
    temp=[]
    for i in player:
        a=ranked.copy()
        a.append(i)
        a=list(set(a))
        a.sort(reverse=True)
        temp.append(a.index(i)+1)
    return temp
ranked=list(map(int,'100 100 50 40 40 20 10'.split()))
player=list(map(int,'5 25 50 120'.split()))
print(climbingLeaderboard(ranked,player))

