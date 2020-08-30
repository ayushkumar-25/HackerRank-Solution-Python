def minion_game(string):
    # your code goes here
    k_score = 0
    s_score = 0
    vowel = 'AEIOU'
    
    for i in range(len(string)):
        if string[i] in vowel:
            k_score += len(string)-i
        else:
            s_score += len(string)-i
    
    if k_score > s_score:
        print("Kevin", k_score)
    elif s_score > k_score:
        print("Stuart", s_score)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)