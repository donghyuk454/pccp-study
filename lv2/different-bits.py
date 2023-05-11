# https://school.programmers.co.kr/tryouts/72111/challenges?language=python3

def solution(numbers):
    answer = []

    for number in numbers:
        binary_number_string = str(bin(number))[2:]

        if binary_number_string[-1] == "0":
            answer.append(number + 1)
            continue

        is_all_one = True
        for b in binary_number_string:
            if b != "1":
                is_all_one = False
                break

        if is_all_one:
            binary_number_string = "10" + binary_number_string[1:]
            answer.append(binary_to_integer(binary_number_string))
            continue

        idx = len(binary_number_string) - 1
        while idx > 0:
            if binary_number_string[idx] == "0":
                break
            idx -= 1

        binary_number_string = binary_number_string[:idx] + "10" + binary_number_string[idx+2:]
        answer.append(binary_to_integer(binary_number_string))

    return answer

def binary_to_integer(number):
    value = 0
    for i in range(1, len(number)+1):
        if number[-1*i] == '1':
            value += (2**(i-1))
    return value