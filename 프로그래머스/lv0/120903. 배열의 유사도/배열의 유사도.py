def solution(s1, s2):
    return len(set(s1) & set(s2))  # len(set(s1).intersection(set(s2)))
