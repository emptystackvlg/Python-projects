import matplotlib.pyplot as plt
x = [0.1,0.2,0.3,0.4,0.5,0.6]
y = [0.042,0.072,0.123,0.164,0.207,0.252]
plt.grid()
plt.plot (x,y, '-ro',markersize = 5)
plt.xticks(x)
plt.yticks(y)
plt.show()