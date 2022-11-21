from functools import reduce

def solve(n, repeats):
    num_list = []
    count_repeats = 1
    while count_repeats <= repeats:
        num_list.append(str(n)*count_repeats)
        count_repeats += 1
    result = reduce(lambda x, y: int(x) + int(y), num_list)
    return result

if __name__ == "__main__":
    solve(n, repeats)
