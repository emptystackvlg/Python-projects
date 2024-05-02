import matplotlib.pyplot as plt
def first_plot():
    fig, ax = plt.subplots()  
    ax.plot([0,452,0,1130], [1538,1500,1538,0])  
    plt.xticks([0,452,0,1130,452,452])
    plt.yticks([1538,1500,1538,0,0,923])
    plt.title("Механическая характеристика")
    plt.xlabel(r'$М,H*м$')
    plt.ylabel(r'$n,об/мин$')
    plt.grid(axis='x')
    plt.grid(axis='y')
    plt.show()
def second_plot():
    fig, ax = plt.subplots()  
    ax.plot([0,452], [1538,1500])  
    plt.xticks([0,452],fontsize = 40)
    plt.yticks([1500,1538],fontsize = 40)
    plt.title("Механическая характеристика",fontsize = 40)
    plt.xlabel(r'$М,H*м$',fontdict= 40)
    plt.ylabel(r'$n,об/мин$',fontsize = 40)
    plt.grid(axis='x')
    plt.grid(axis='y')
    plt.show()


first_plot()