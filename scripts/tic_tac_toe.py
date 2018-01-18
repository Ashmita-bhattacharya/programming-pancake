import random
import collections

compare = lambda x, y: collections.Counter(x) == collections.Counter(y)

states1 = [[1,0,0,0,0,0,0,0,0], [0,1,0,0,0,0,0,0,0], [0,0,0,1,0,0,0,0,0]]
states2 = []
states3 = []
states4 = []
states5 = []
states6 = []
states7 = []
states8 = []
states9 = []

def next_level(statesa, statesb, move):
    for i in range(len(statesa)):
        for j in range(9):
            ns = []
            if statesa[i][j]==0:
                ns = list(statesa[i]) 
                ns[j] = move
                statesb.append(ns)


def random_list(indexList):
    rand_list = []
    for i in range(10):
        r = random.randint(0,8)
        if indexList.count(r) == 1:
            rand_list.append(r)
        else:
            i = i-1
    return rand_list

def set_random_moves(states):
    for i in range(len(states)):
        indexlist = []
        for j in range(len(states[i])):
            if states[i][j] == 0:
                indexlist.append(j)
        actions = random_list(indexlist)
        sa = [states[i] , actions]
        states_action.append(sa)
        print(i)


def check_win(state):
    if state[0] == 1 and state[1] == 1 and state[2] == 1:
        return 1
    if state[3] == 1 and state[4] == 1 and state[5] == 1:
        return 1
    if state[6] == 1 and state[7] == 1 and state[8] == 1:
        return 1
    if state[0] == 1 and state[3] == 1 and state[6] == 1:
        return 1
    if state[1] == 1 and state[4] == 1 and state[7] == 1:
        return 1
    if state[2] == 1 and state[5] == 1 and state[8] == 1:
        return 1
    if state[0] == 1 and state[4] == 1 and state[8] == 1:
        return 1
    if state[2] == 1 and state[4] == 1 and state[4] == 1:
        return 1


    if state[0] == 2 and state[1] == 2 and state[2] == 2:
        return 2
    if state[3] == 2 and state[4] == 2 and state[5] == 2:
        return 2
    if state[6] == 2 and state[7] == 2 and state[8] == 2:
        return 2
    if state[0] == 2 and state[3] == 2 and state[6] == 2:
        return 2
    if state[1] == 2 and state[4] == 2 and state[7] == 2:
        return 2
    if state[2] == 2 and state[5] == 2 and state[8] == 2:
        return 2
    if state[0] == 2 and state[4] == 2 and state[8] == 2:
        return 2
    if state[2] == 2 and state[4] == 2 and state[4] == 2:
        return 2

    return 0



next_level(states1,states2,2)
next_level(states2,states3,1)
next_level(states3,states4,2)
next_level(states4,states5,1)
next_level(states5,states6,2)
next_level(states6,states7,1)
next_level(states7,states8,2)
next_level(states8,states9,1)
states = states1 + states2 + states3 + states4 + states5 + states6 + states7 + states8 + states8

states_action = []
set_random_moves(states)

states = states + [[[0,0,0,0,0,0,0,0,0],[0,1,4,0,1,4,0,1,4,0,1,4,0,1,4,0,1,4,0,1,4,0,1,4,0,1,4,0,1,4,0,1,4,0,1,4,0,1,4,0,1,4,0,1,4,0,1,4]]]

def start_learn(states):
    game_state = [[[0,0,0,0,0,0,0,0,0],[]]]
    for i in range(300):
        for s in states:
            if compare(s[0],game_state[-1][0]):
                move1 = random.choice[s[1]]
                game_state[-1][0][move1] = 1
                game_state[-1][1].append(move1)

        for s in states:
            if compare(s[0],game_state[-1][0]):
                move2 = random.choice[s[1]]
                game_state[-1][0][move2] = 2
                game_state[-1][1].append(move2)








