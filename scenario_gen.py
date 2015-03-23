from itertools import combinations

teams1_list = ['A','B','C','D']
teams2_list = ['E','E','H','H']
teams3_list = ['I','J','K','L']
teams4_list = ['N', 'N','O','O']

brackets = ['ADAXHXIKKMOMAMA','ADDXHHIXIMPMDMD','ADDXHXJXXMPMXMM', 'ADAXHHJXXNPPAPA',
            'ACAXHHJXJMPMAMM', 'ACAXHXIKKMPMAKA', 'ACCXXXIKINONCII', 'ADDXHHJKKMPMDKD',
            'ACAXHXIXXMPMAMA', 'ACCXHXJKJMPMXMM', 'ADDXHXIKIMPPDII']


probs = {'A': [.945, 0, .708995, 0,0,0,0,0,0,0,0,0,.783582, 0,.617143],
         'B': [.055, 0, .181818, 0,0,0,0,0,0,0,0,0,.3, 0, .166667],
         'C': [0, .457, .306346, 0,0,0,0,0,0,0,0,0, .6, 0, .41667],
         'D': [0, .543, .331492, 0,0,0,0,0,0,0,0,0, .677778, 0, .491803],
         'E': [0,0,0, .71, 0, .332394, 0,0,0,0,0,0, .190678, 0, .266667],
         'F': [0,0,0, .29, 0, .175862, 0,0,0,0,0,0, .117647, 0, .166667],
         'G': [0,0,0,0, .446, .692825, 0,0,0,0,0,0, .20712, 0, .28125],
         'H': [0,0,0,0, .554, .729242, 0,0,0,0,0,0, .371287, 0, .453333],
         'I': [0,0,0,0,0,0, .549, 0, .4244408, 0,0,0,0, .480687, .401786],
         'J': [0,0,0,0,0,0, .451, 0, .392461, 0,0,0,0, .502825, .426966],
         'K': [0,0,0,0,0,0,0,.942, .617834, 0,0,0,0, .649485, .563492],
         'L': [0,0,0,0,0,0,0, .058, .137931, 0,0,0,0, .125, .5],
         'M': [0,0,0,0,0,0,0,0,0,.58, 0, .734483, 0, .507042, .50463],
         'N': [0,0,0,0,0,0,0,0,0,.42, 0,.685714, 0, .399306, .417391],
         'O': [0,0,0,0,0,0,0,0,0,0,.382, .227749, 0, .229885,.25],
         'P': [0,0,0,0,0,0,0,0,0,0, .618, .322006, 0, .341709, .352941]}


# takes four teams, lists all possible outcomes
def makeList(teams):
    output = []
    for i in range(0,2):
        for j in range(2,4):
            for k in range(0,2):
                if (k == 1):
                    output.append(teams[i]+teams[j]+teams[i])
                else:
                    output.append(teams[i]+teams[j]+teams[j])
    return output

teams1 = makeList(teams1_list)
teams2 = makeList(teams2_list)
teams3 = makeList(teams3_list)
teams4 = makeList(teams4_list)

outcomes = []
for teamA in teams1:
    for teamB in teams2:
        for teamC in teams3:
            for teamD in teams4:
                final_four = makeList([teamA[2],teamB[2],teamC[2],teamD[2]])
                for teamF in final_four:
                    outcomes.append((teamA + teamB + teamC + teamD + teamF))

score = 0
total_score = 0

all_scores = []
high_score = [0,0,0,0,0,0,0,0,0,0,0]
high_score_prob = [0,0,0,0,0,0,0,0,0,0,0]
total_prob = 0
for poss in outcomes:
    place = 0
    bracket_scores = [47,44,43,43,42,42,41,41,40,40,38]
    for person in brackets:
        score = 0
        for game in range(0,len(person)):
            if person[game] == poss[game]:
                if game in [0,1,3,4,6,7,9,10]:
                    score += 4
                elif game in [2,5,8,11]:
                    score += 8
                elif game in [12,13]:
                    score += 16
                else:
                    score +=32
        bracket_scores[place] += score
        place += 1
    high_score[bracket_scores.index(max(bracket_scores))] += 1
    prob = 1.0
    #if bracket_scores.index(max(bracket_scores)) == 9:

        #print poss
    for z in range(0,len(poss)):
        prob *= probs[poss[z]][z]
        
    high_score_prob[bracket_scores.index(max(bracket_scores))] += prob
    all_scores.append(bracket_scores)
    

print len(outcomes)
print high_score
    

