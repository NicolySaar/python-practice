while True:
    percent = input("Fraction: ")
    values = percent.split("/")
    try:
        x, y = map(int, values)

        if x < 0 or y <= 0 or x > y:
            continue

        break


    except (ValueError, ZeroDivisionError):
        continue

fuel = round (x/y * 100)
if fuel <= 1:
    print("E")
elif fuel >= 99:
    print("F")
else: 
    print(f"{fuel}%")