from win10toast import ToastNotifier as TN
from psutil import virtual_memory


def meminfo () :
    memoryUse = virtual_memory()[4]/2.**30
    mem = float('{:.2f}'.format(memoryUse))
    toast = TN () 
    toast.show_toast ("Свободно памяти",
    str (mem)+ " GB" , duration=8)
    
meminfo () 
 
    
        

