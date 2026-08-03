import time

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

for i in range(low_lim, up_lim + 1):
    divisors = 0
    if i % 2 == 0 and i != 2:
        continue

    for j in range(2, i):
        if i % j == 0:
            divisors += 1

    if divisors == 0:
        primelist.append(i)

if 1 in primelist:
    primelist.remove(1) 
if 0 in primelist:
    primelist.remove(0)

end = time.perf_counter()

print("Finished computing")
print(f"\nTime elapsed: {end-start:.6f} seconds")

with open(r"prime generator\primes.txt", "w") as file:
    file.write(

f"""Primes from {low_lim}-{up_lim}

{primelist}

Total of {len(primelist)} primes
Elapsed Time: {end-start:.6f} seconds
Density: {100*((len(primelist))/(up_lim-low_lim+1)):.3f}%"""
)

print("Details in primes.txt")
