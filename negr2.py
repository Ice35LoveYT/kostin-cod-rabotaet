var1 = "Камінь"
var2 = "Ножиці"
var3 = "Папір"


def end(a, x):
    if a == x:
        print("Нічия!")
    elif (a == "Камінь" and x == "Ножиці") or (a == "Ножиці" and x == "Папір") or (a == "Папір" and x == "Камінь"):
        print("Гравець перший, переміг")
    else:
        print("Гравець другий, переміг")


def start(game):
    while game not in (var1, var2, var3):
        input("Bиберіть Камінь, Ножиці або Папір: ")


game1 = input('Гравець перший, оберить Камінь, Ножиці або Папір: ')
start(game1)
game2 = input('Гравець другий, оберить Камінь, Ножиці або Папір: ')
start(game2)


print(f"Гравець перший вибрав: {game1}")
print(f"Гравець другий вибрав: {game2}")

end(game1, game2)
