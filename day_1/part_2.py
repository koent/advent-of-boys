with open('input.txt', 'r') as f:
    data = [int(s) for s in f.read().splitlines()]

print(data)

seen_numbers = set()

index = 0
running_counter = 0
len_data = len(data) - 1
while True:
    current_event = data[index]

    running_counter += current_event

    if running_counter in seen_numbers:
        break
    else:
        seen_numbers.add(running_counter)

    
    if index == len_data:
        index = 0
    else: index += 1
    
print(running_counter)
