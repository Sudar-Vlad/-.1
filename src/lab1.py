# Лабораторна робота №1. Основи Python
# Варіант: 5 варіант
# ПІБ: Міщенко Владислав

while True:
    try:
        length = float(input("Введіть довжину кімнати (м): "))
        width = float(input("Введіть ширину кімнати (м): "))
        height = float(input("Введіть висоту кімнати (м): "))
        volume=float(input("Введіть площу, яку буде покривати фарба на 1 літр:  "))
        cost=float(input("Введіть вартість фарби за літр (грн): "))
        if length<0 or cost<0 or width<0 or height<0:
            raise ValueError("Значення повинні бути більше нуля")
        break
    except ValueError as e:
        print(f"Помилка: {e}. Спробуйте ще раз.")

WallArea=2*(length+width)*height #Обчислює площу кімнати
Paint=WallArea/volume #Обчислює, скільки треба фарби
TotalCost=Paint*cost #Обчислює вартість роботи

print(f"Площа кімнати:{WallArea:.2f} ", )
print(f"Вартість фарбування:{TotalCost:.2f} ", )
print(f"Кількість фарби (літрів):{Paint:.2f}")

# Не забувайте форматувати вивід та додавати коментарі!
