#Two lines once the dictionary is established.
def romanToInt(s):
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }
    k = list(map(lambda x: roman_dict[x], list(s)))
    return(sum([-k[x] if k[x+1] > k[x] else k[x] for x in range(0, len(k) - 1)]) + k[-1])