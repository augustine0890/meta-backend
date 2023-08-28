NAMES = ["Augustine", "John", "Paul", "Ringo"]
AGES = [33, 25, 32, 35]

i = 0
while i < len(NAMES):
    print(NAMES[i], AGES[i])
    i += 1

for name in NAMES:
    print(name)

for name, age in zip(NAMES,AGES):
    print(f"{name}, {age}")

for name in reversed(NAMES):
    print(name)

for i in range(5):
    print(i)

for i, name in enumerate(NAMES):
    print(f"{i}. {name}")