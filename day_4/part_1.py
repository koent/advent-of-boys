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

# for g in day_guard_asleep_times:
#     print(g)
#     for d in day_guard_asleep_times[g]:
#         print(d, day_guard_asleep_times[g][d])

nof_minutes_asleep = {g:sum(sum(day_guard_asleep_times[g][d]) for d in day_guard_asleep_times[g]) for g in day_guard_asleep_times}

# print(nof_minutes_asleep)

guard = max(nof_minutes_asleep, key=nof_minutes_asleep.get)

total = [0] * 60
for d in day_guard_asleep_times[guard]:
    for minute in range(60):
        total[minute] += day_guard_asleep_times[guard][d][minute]

minute_most_asleep = max(enumerate(total), key=lambda x: x[1])[0]

print(minute_most_asleep * int(guard[1:]))