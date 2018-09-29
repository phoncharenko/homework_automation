
while True:
    x = input("Пожалуйста, введите число:\n")  # type:
    try:
        x = float(x)
    except Exception:
        print("try again")
    else:
        break
print('exit')
