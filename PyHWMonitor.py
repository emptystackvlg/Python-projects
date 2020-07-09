import platform
import wmi
import psutil
import easygui as g
computer = wmi.WMI()
os_info = computer.Win32_OperatingSystem()[0]
system_ram = int(os_info.TotalVisibleMemorySize) / 1048576  
gpu_info = computer.Win32_VideoController()[0]
proc_info = computer.Win32_Processor()[0]
proc_freq = float(computer.Win32_Processor()[0].MaxClockSpeed) /1000 
count = psutil.cpu_count(logical=False)
count1 = psutil.cpu_count(logical=True)
uname = platform.uname()
g .msgbox(title = "Информация о системе" ,msg=f"ОС: {uname.system} {uname.release} (version: {uname.version})" + "\n" +f"Имя компьютера: {uname.node}"
+ "\n" +'ЦП: {0}'.format(proc_info.Name) + "\n" + "Частота ЦП: {0}".format(proc_freq) + " ГГц" + "\n" +"Ядер/Потоков ЦП: " + str(count) + "/" + str(count1) + "\n" +'ОЗУ: {0} GB'.format(system_ram)
+ "\n" + 'Видеокарта: {0}'.format(gpu_info.Name))
