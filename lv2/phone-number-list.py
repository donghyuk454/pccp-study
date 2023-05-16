# https://school.programmers.co.kr/tryouts/72082/challenges?language=python3

def solution(phone_book):
    answer = True
    number_dict = dict()

    for number in phone_book:
        number_dict[number] = True

    for number in phone_book:
        for i in range(1, len(number)):
            if number[:i] in number_dict.keys():
                return False인

    return answer