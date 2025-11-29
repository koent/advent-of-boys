with open('1.txt', 'r') as f:
    print(sum(int(i) for i in f.readlines()))
