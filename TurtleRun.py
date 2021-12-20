import turtle as t
import random
import time
# Tạo và quy định dài rộng của đường đua và các tham số
screen = t.Screen()
screen.setup(height=500, width=600)

# Hiển thị cửa sổ cho phép người dùng đoán con rùa màu nào thắng cuộc
guess = screen.textinput(prompt="Dự đoán con rùa nào chiến thắng?", title="Nhập vào màu rùa (đỏ, nâu, xanh dương, xanh lá cây, cam, hồng)")

# List lưu lại màu của các con rùa
colors = ["red", "brown", "blue", "green", "orange", "pink"]
# Vị trí ban đầu theo trục y của các con rùa
y_position = [0, -30, 30, -60, 60, 90]

# List lưu lại vận tốc của các con rùa
# các giá trị này sẽ được chọn một cách ngẫu nhiên
turtle_speed = [10, 15, 20, 25, 30, 5]

# Tạo một list để lưu các con rùa
all_turtles = []
run = True

# Xây dựng hàm để tạo và thiết đặt vị trí ban
# đầu, màu cho các con rùa và lưu vào list
for turtle in range(0, 6):
    turtles = t.Turtle(shape="turtle")
    turtles.penup()
    turtles.goto(x=-250, y=y_position[turtle])
    turtles.color(colors[turtle])
    # Lưu vào list
    all_turtles.append(turtles)

def random_walk(turtles):
    global run
    for turtle in turtles:
        turtle.forward(random.choice(turtle_speed))
        # Kiểm tra điều kiện cán đích
        # Khi 1 con cán đích thì dừng lại
        if turtle.xcor() > 250:
            print("Turtle "+str(turtle.color())+ "won")
            run = False

while run:
    random_walk(all_turtles)

screen.exitonclick()