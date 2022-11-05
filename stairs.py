import sys

# 5 stairs 
# 5 (1) steps
# 2,2,1
# 2,1,2
# 1112
# 222 not allowed!

# 1: f(1) = 1
# 2: f(2) = 2
# 3: f(3) = f(2) + f(1) = 3
# 4: f(4) = f(3) + f(2) = 5
# 5: f(5) = f(4) + f(3) = 8
# n: f(n) = f(n - 1) + f(n - 2)

def step(left, memory = None):
    if (memory == None):
        memory = dict()
    # base case
    if left == 1:
        return 1
    if left == 2:
        return 2
    if not left in memory:
        memory[left] = step(left - 1, memory) + step(left - 2, memory)
    return memory[left]

def main(args):
    # print(args)
    mem = {}
    print(step(40, mem))
    print(mem)

if __name__ == "__main__":
    main(sys.argv)