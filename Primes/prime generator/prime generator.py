import time
from datetime import datetime

while True:
    try:
        low_lim = int(input("Lower limit:\n>>> "))
        if low_lim < 1:
            print("Lower limit can't be smaller than 1")
            continue
        else:
            break
    except ValueError:
        print("\nValueError. Try again\n")


while True:
    try:
        up_lim = int(input("Upper limit:\n>>> "))

        if up_lim < low_lim:
            print(f"Must be higher then {low_lim}")
        else:
            break
    except ValueError:
        print("\nValueError. Try again\n")

primelist = []

start = time.perf_counter()

for i in range(max(low_lim, 2), up_lim+1):
    if i == 2:
        primelist.append(i)
        continue

    if i % 2 == 0:
        continue

    for j in range(3, int(i**0.5)+1, 2):
        if i % j == 0:
            break

    else:
        primelist.append(i)

end = time.perf_counter()

print("Finished computing")
print(f"\nTime elapsed: {end-start:.6f} seconds")

log = datetime.now().strftime(r"Primes\prime generator\logs\%Y-%m-%d_%H-%M-%S.log")

with open(log, "w") as file:
    file.write(

f"""Primes from {low_lim}-{up_lim}

{primelist}

Total of {len(primelist)} primes
Elapsed Time: {end-start:.6f} seconds
Density: {100*((len(primelist))/(up_lim-low_lim+1)):.3f}%"""
)

print(f"Details in {log}")
