import random
from datetime import datetime, timedelta

ITEMS = 120
PREFIXES = ["WA10", "WA20", "WA30"]


current_date = datetime(2021, 4, 19, 11, 0, 0)
result = {
    "timestamps": [int(current_date.timestamp())],
    "values": {},
}
change_t = timedelta(minutes=1)

# add timestamps
for t in range(1, ITEMS):
    current_date += change_t
    result["timestamps"].append(int(current_date.timestamp()))

for prefix in PREFIXES:
    for index in range(1, 21):
        number = index if index >= 10 else f"0{index}"
        key = f"{prefix}{number}"

        start = float(random.randint(190, 350)) / 10.0
        current = [start]
        for t in range(1, ITEMS):
            change = random.randint(-1, 1)
            if change == 0:
                current.append(current[-1])
            else:
                change_val = float(random.randint(1, 10)) / 10.0
                if change == 1:
                    current.append(round(current[-1] + change_val, 1))
                else:
                    current.append(round(current[-1] - change_val, 1))

        result["values"][key] = current

print(result)
