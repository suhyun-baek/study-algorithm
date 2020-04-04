def minion_game(str_input):
    # your code goes here
    int_len_input = len(str_input)
    int_score_stuart = 0
    int_score_kevin = 0

    for index in range(int_len_input):
        if str_input[index] in ["A", "E", "I", "O", "U"]:
            int_score_kevin += int_len_input - index
        else:
            int_score_stuart += int_len_input - index
    
    if int_score_kevin > int_score_stuart:
        print("Kevin", int_score_kevin)
    elif int_score_kevin < int_score_stuart:
        print('Stuart {0}'.format(int_score_stuart))
    else:
        print('Draw')
        
if __name__ == '__main__':
    # s = input()
    s = "NAAMA"
    minion_game(s)