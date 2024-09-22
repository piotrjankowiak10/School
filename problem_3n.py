def collatz_cycle_length(n):
    length = 1  
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        length += 1
    return length

def max_cycle_length(i, j):
    start, end = min(i, j), max(i, j)
    max_length = 0
    for n in range(start, end + 1):
        length = collatz_cycle_length(n)
        if length > max_length:
            max_length = length
    return max_length

def main():
    try:
        while True:
            line = input().strip()
            if not line:
                break
            i, j = map(int, line.split())
            result = max_cycle_length(i, j)
            print(i, j, result)
    except EOFError:
        pass

if __name__ == "__main__":
    main()
