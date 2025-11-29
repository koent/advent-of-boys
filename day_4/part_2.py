from collections import defaultdict

with open('input.txt', 'r') as f:
    data = [d.split() for d in f.readlines()]

data2 = sorted(data)


current_guard = None
falls_time = None
day_guard_asleep_times = defaultdict(lambda: defaultdict(lambda: [0] * 60))

for day, time, action, nr, *_ in data2:
    if action == "Guard":
        current_guard = nr
    if action == "falls":
        falls_time = int(time[3:5])
    if action == "wakes":
        wakes_time = int(time[3:5])
        for i in range(falls_time, wakes_time):
            day_guard_asleep_times[current_guard][day][i] = 1

# For each guard, count how many times they were asleep at each minute
guard_minute_counts = {}
for guard in day_guard_asleep_times:
    minute_counts = [0] * 60
    for day in day_guard_asleep_times[guard]:
        for minute in range(60):
            minute_counts[minute] += day_guard_asleep_times[guard][day][minute]
    guard_minute_counts[guard] = minute_counts

# For each guard, find their most frequently slept minute and its count
best_guard = None
best_minute = None
best_count = 0

for guard in guard_minute_counts:
    for minute in range(60):
        count = guard_minute_counts[guard][minute]
        if count > best_count:
            best_count = count
            best_guard = guard
            best_minute = minute

print(best_minute * int(best_guard[1:]))