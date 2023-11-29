game_input = "A2B1A2B2A1A2A2A2"
#game_input = "A2B2A1B2A2B1A2B2A1B2A1A1B1A1A2"
b_score = 0
a_score = 0
who_scored = ""
every_other = 2

def score_count(a, b):
    if a >= 11 and b != a-1:
        print("A")
    elif b >= 11 and a != b-1:
        print("B")

for x in game_input:
    
    if every_other % 2 == 0:
        who_scored = x
    else: 
        if who_scored == "A":
            a_score = a_score + int(x)
        else:
            b_score = b_score + int(x)
    every_other = every_other + 1
    score_count(a_score, b_score)



