from PIL import Image, ImageDraw, ImageFont
print("Генератор мемов запущен!")
top_text = input("Введи короткий верхний текст: ")
bottom_text = input("Введи короткий нижний текст: ")

list_of_images = ["1. Выдры", "2. Пингвины"]
print("Список картинок: ")
for image_tittle in list_of_images:
    print(image_tittle)

user_image = input("Введите номер картинки: ")
if user_image == "1":
    image_file = "./images/Пингвины.png"
    print(image_file)
elif user_image == "2":
    image_file = "./images/Выдры.png"
    print(image_file)

image = Image.open(image_file)
draw = ImageDraw.Draw(image)


width, height = image.size

font = ImageFont.truetype("arial.ttf", size=100)

text = draw.textbbox((0, 0), top_text, font)
text_width = text[2]
draw.text(((width - text_width) / 2, 10), top_text, font=font, fill="brown")
text = draw.textbbox((0, 0), bottom_text, font)

text_width = text[2]
text_height = text[3]
draw.text(((width - text_width) / 2, height - text_height - 10), bottom_text, font=font, fill="brown")
text = draw.textbbox((0, 0), top_text, font)

image.save("new_image.png")
print("Ваш мем сохранён как 'new_image.png'")





