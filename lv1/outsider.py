# https://school.programmers.co.kr/tryouts/72136/challenges

def solution(input_string):
    answer = ''
    counts = dict()
    before = input_string[0]
    
    alpha_set = set(list(input_string))
    
    for alpha in alpha_set:
        is_outsider = False
        check = False
        is_first = True
        for i in input_string:
            if i == alpha and is_first and not check:
                check = True
            elif i == alpha and check and not is_first:
                is_outsider = True
                break
            elif i != alpha and is_first and check:
                is_first = False
            
        if is_outsider:
            answer += alpha
    
    if len(answer) == 0:
        answer = "N"
    
    return "".join(sorted(answer))