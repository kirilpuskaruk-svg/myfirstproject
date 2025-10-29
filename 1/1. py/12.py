# Запитуємо дані у користувача
product = input("Введіть назву товару: ")
quantity = int(input("Введіть кількість товару: "))
price = float(input("Введіть ціну за одиницю: "))
card = input("Чи є знижкова картка? (так/ні): ").strip().lower()
# Обчислюємо суму
total = quantity * price
# Якщо є картка – знижка 5%
if card == "так":
    discount = total * 0.05
    total -= discount
# Виводимо чек
print("------ ЧЕК ------")
print(f"Товар: {product}")
print(f"Кількість: {quantity}")
print(f"Ціна за одиницю: {price:.1f} грн")
print(f"До сплати: {total:.2f} грн")