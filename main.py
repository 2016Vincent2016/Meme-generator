print("Генератор мемов запущен!")
top_text = input("Введи верхний текст: ")
bottom_text = input("Введи нижний текст: ")

list_of_images = ["1. Кошка в очках ", "2. Собака с пистолетом"]
print("Список картинок: ")
for image_tittle in list_of_images:
    print(image_tittle)

user_image = input("Введите номер картинки: ")
if user_image == "1":
    image = "./images/Кошка в очках.png"
    print(image)
elif user_image == "2":
    image = "./images/Собака с пистолетом.png"
    print(image)
