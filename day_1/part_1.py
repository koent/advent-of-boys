with open('input.txt', 'r') as f:
    print(sum(int(i) for i in f.readlines()))
