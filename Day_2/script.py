FILE_NAME = "strategy_guide.txt"

rules = {
    "scissors": "paper",
    "paper": "rock",
    "rock": "scissors"
}

play_scores = {
    "scissors": 3,
    "paper": 2,
    "rock": 1
}

opponent_mapping = {
    "A": "rock",
    "B": "paper",
    "C": "scissors"
}

player_mapping = {
    "X": "rock",
    "Y": "paper",
    "Z": "scissors"
}

# Part 1
def get_player_score(file):
    score = 0
    for line in file:
        arr = line.split()
        opponent_play = opponent_mapping[arr[0]]
        player_play = player_mapping[arr[1]]
        score += play_scores[player_play]
        if player_play == opponent_play:
            score += 3
        elif rules[player_play] == opponent_play:
            score += 6
    return score

def rock_paper_scissors_part1():
    file = open(FILE_NAME, "r")
    score = get_player_score(file)
    file.close()
    return score

# Part 2
def get_player_score_2(file):
    score = 0
    for line in file:
        arr = line.split()
        opponent_play = opponent_mapping[arr[0]]
        outcome = arr[1]
        if outcome == "X":
            player_play = rules[opponent_play]
        elif outcome == "Y":
            player_play = opponent_play
            score += 3
        elif outcome == "Z":
            player_play = list(rules.keys())[list(rules.values()).index(opponent_play)]
            score += 6
        score += play_scores[player_play]
    return score

def rock_paper_scissors_part2():
    file = open(FILE_NAME, "r")
    score = get_player_score_2(file)
    file.close()
    return score

### TEST AREA
# Part 1
#print(rock_paper_scissors_part1())
# Output: 8392

# Part 2
#print(rock_paper_scissors_part2())
# Output: 10116
