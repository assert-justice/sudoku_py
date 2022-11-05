import sys

def parse_puzzle(text):
    result = []
    for c in text:
        if c != '0':
            result.append( int(c) )
    return result
    return [int(c) for c in text if c != '0']
    # text.split('').filter(c => c !== '0').map(c => Number(c))

def print_puzzle(puzzle):
    for i in range(9):
        print(puzzle[i*9:(i+1)*9])

def get(puzzle, x, y):
    idx = x + y * 9
    return puzzle[idx]

def set(puzzle, x, y, n):
    idx = x + y * 9
    puzzle[idx] = n

def possible(puzzle, x, y, n):
    for i in range(9):
        if get(puzzle, x, i) == n:
            return False
        if get(puzzle, i, y) == n:
            return False
    bx = x // 3 * 3
    by = y // 3 * 3
    for i in range(3):
        for f in range(3):
            if get(puzzle, bx + i, by + f) == n:
                return False
    return True

def solve(puzzle):
    for x in range(9):
        for y in range(9):
            if get(puzzle, x, y) == 0:
                for i in range(1,10):
                    if possible(puzzle, x, y, i):
                        set(puzzle, x, y, i)
                        solve(puzzle)
                        set(puzzle, x, y, 0)
                return
    print_puzzle(puzzle)

def main(args):
    if len(args) < 2:
        print("not enough arguments")
        return
    with open(args[1]) as f:
        puzzles = [parse_puzzle(line) for line in f.read().splitlines()]
        print_puzzle(puzzles[0])
        print()
        solve(puzzles[0])
    
if __name__ == "__main__":
    main(sys.argv)