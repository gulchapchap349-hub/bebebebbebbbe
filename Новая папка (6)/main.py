import turtle
import colorsys

screen = turtle.Screen()
screen.bgcolor("#0a0f1d")  # Глубокий темно-синий
screen.title("Сакральная Мандала")

t = turtle.Turtle()
t.speed(0)
turtle.tracer(15, 0)  # Максимальное ускорение отрисовки
t.width(1)

n = 210  # Количество элементов
for i in range(n):
    # Создаем градиент от неоново-розового до фиолетового и синего
    hue = 0.7 + (i / n) * 0.2
    color = colorsys.hsv_to_rgb(hue, 0.9, 1)
    t.pencolor(color)
    
    # Рисуем основу узора
    t.forward(i * 2.5)
    t.right(144.5)  # Тот самый магический угол
    
    # Дополнительные декоративные петли
    t.circle(i * 0.2, 90)
    t.forward(i)
    t.right(45)

turtle.done()
