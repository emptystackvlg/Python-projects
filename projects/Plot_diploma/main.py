import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

x_data, y_data = [], []
fig, ax = plt.subplots()
line, = ax.plot(x_data, y_data, 'r-')  # Создаем пустой линейный график

def update(frame):
    x_data.append(frame)
    y_data.append(np.sin(frame))       # Здесь могут быть ваши реальные данные
    line.set_data(x_data, y_data)      # Обновляем данные графика
    ax.relim(); ax.autoscale_view()    # Автоматически масштабируем оси
    return line,

ani = animation.FuncAnimation(fig, update, interval=100, blit=True)
plt.show()