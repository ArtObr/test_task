some_text = "code cats uutu xxxy hhjk nmff lnmd f nnnmmmdddk nnnnmmdddk"


def solution(n):
    correct_words = []
    for word in some_text.split():
        if len(word) == n:
            counter = {}
            for letter in word:
                c = counter.setdefault(letter, 0)
                counter[letter] = c + 1
            if all(v % 2 == 1 for v in counter.values()):
                correct_words.append(word)

    return correct_words


print(solution(4))
print(solution(1))
print(solution(10))
