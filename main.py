from PIL import Image, ImageDraw, ImageFont

print("Генератор мемов запущен!")
top_text = input("Введи верхний текст: ")
bottom_text = input("Введи нижний текст: ")

list_of_images = ["1. Кошка в очках ", "2. Собака с пистолетом"]
print("Список картинок: ")
for image_tittle in list_of_images:
    print(image_tittle)

user_image = input("Введите номер картинки: ")
if user_image == "1":
    image_file = "./images/Кошка в очках.png"
    print(image_file)
elif user_image == "2":
    image_file = "./images/Собака с пистолетом.png"
    print(image_file)

image = Image.open(image_file)
draw = ImageDraw.Draw(image)

google_font = "https://fonts.googleapis.com/css2?family=Luxurious+Script&display=swap"
font = ImageFont.truetype("arial.ttf", size=25)

draw.text((5, 0), top_text, font=font, fill="brown")
draw.text((5, 50), bottom_text, font=font, fill="brown")

image.save("new_image.png")




