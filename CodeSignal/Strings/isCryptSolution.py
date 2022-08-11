def solution(crypt, solution):
    solution_dict = dict(solution)
    word1_number = ''
    word2_number = ''
    word3_number = ''
    
    #First Word 
    for char in crypt[0]:
        word1_number += solution_dict.get(char)
    if word1_number[0] == '0' and len(word1_number) != 1:
        return False
    word1_number = int(word1_number)

    #Secornd word
    for char in crypt[1]:
        word2_number += solution_dict.get(char)
    if word2_number[0] == '0' and len(word2_number) != 1:
        return False
    word2_number = int(word2_number)

    #Third word
    for char in crypt[2]:
        word3_number += solution_dict.get(char)
    if word3_number[0] == '0' and len(word3_number) != 1:
        return False
    word3_number = int(word3_number)

    return (word1_number + word2_number) == word3_number