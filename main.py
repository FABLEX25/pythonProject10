import json

def zad2():
    with open("product_spisok.json", "r", encoding='utf-8 ') as myfile:
        data = json.load(myfile)

    new_product = {
        "name": input("Название продукта: "),
        "price": int(input("Цену продукта: ")),
        "weight": int(input("Введите вес продукта: ")),
        "available": input("Продукт в наличии? ")
    }

    data["products"].append(new_product)

    with open("product_spisok.json", "w", encoding='utf-8 ') as outfile:
        json.dump(data, outfile, indent=2)

    print("Содержимое файла:")
    for product in data["products"]:
        print("Название:", product["name"])
        print("Цена:", product["price"])
        print("Вес:", product["weight"])
        if product["available"]:
            print("В наличии")
        else:
            print("Нет в наличии!")
        print()

zad2()

en_ru = open("en-ru.txt", encoding='utf-8')
num1 = {}
num2 = {}
for stroka in en_ru.read().split("\n"):
    k = stroka.split(" - ")
    k[1] = list(k[1].split(", "))
    for i in k:
        i = k[0]
        num1[i] = k[1]
for znach in num1:
    s = num1[znach]
    for slovo in s:
        num2[slovo] = znach

ru_en = open("ru-en.txt", "w", encoding='utf-8')
for znach in sorted(num2):
    ru_en.write(znach+ " - " + num2[znach] + "\n")
ru_en.close()

