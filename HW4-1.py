
from sys import argv

def salary():
    try:
        time, rate, bonus = map(float, argv[1:])
        print(f"salary - {time*rate+bonus}")
    except ValueError:
        print("ВВедите только 3 числа без дополнительных знаков")


salary()