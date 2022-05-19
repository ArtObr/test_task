s1 = "aaaabbbbccddg"
s2 = "ccaaffddecee"
s3 = "eeee"
s4 = "example"


def solution(s):
    delete_counter = 0

    counter = {}
    for letter in s:
        c = counter.setdefault(letter, 0)
        counter[letter] = c + 1

    counter_list = sorted(counter.values())

    ending = False
    while not ending:
        for i in range(len(counter_list)):
            if i == len(counter_list) - 1:
                ending = True
                break
            if counter_list[i] == counter_list[i + 1] and counter_list[i] != 0:
                counter_list[i] -= 1
                delete_counter += 1
                break

    return delete_counter


print(solution(s1))
print(solution(s2))
print(solution(s3))
print(solution(s4))
