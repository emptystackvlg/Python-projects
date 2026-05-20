import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt, firwin, lfilter

# Параметры моделирования
fs = 1e6  # Частота дискретизации (1 МГц)
t_max = 0.01  # Общее время моделирования (10 мс)
t = np.arange(0, t_max, 1/fs)  # Временная ось

# Полезный сигнал (импульсный сигнал)
def create_signal(t):
    signal = np.zeros_like(t)
    signal[(t >= 1e-3) & (t <= 1.1e-3)] = 1  # Импульс длительностью 0.1 мс
    return signal

# Добавление синхронных и асинхронных помех
def add_noise(signal, t):
    # Синхронная помеха (например, наводка от сети 50 Гц)
    sync_noise = 0.5 * np.sin(2 * np.pi * 50 * t)
    
    # Асинхронная помеха (случайный шум)
    async_noise = 0.2 * np.random.normal(0, 1, t.shape)
    
    # Суммарный сигнал с помехами
    noisy_signal = signal + sync_noise + async_noise
    return noisy_signal

# Аналоговая фильтрация (низкочастотный фильтр)
def analog_filter(signal, cutoff, fs, order=2):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    filtered_signal = filtfilt(b, a, signal)
    return filtered_signal

# Синхронное детектирование (подавление синхронных помех)
def sync_detection(signal, t, interference_freq):
    # Генерация опорного сигнала
    reference_signal = np.sin(2 * np.pi * interference_freq * t)
    
    # Умножение сигнала на опорный сигнал
    multiplied_signal = signal * reference_signal
    
    # Фильтрация низких частот
    filtered_signal = analog_filter(multiplied_signal, 10, fs)
    return filtered_signal

# Цифровая фильтрация (адаптивный фильтр)
def adaptive_filter(signal, desired_signal, filter_order=32):
    # Использование адаптивного фильтра (например, LMS)
    mu = 0.01  # Шаг адаптации
    w = np.zeros(filter_order)  # Инициализация весов фильтра
    output_signal = np.zeros_like(signal)
    
    for i in range(filter_order, len(signal)):
        x = signal[i - filter_order:i]
        output_signal[i] = np.dot(w, x)
        e = desired_signal[i] - output_signal[i]
        w += mu * e * x
    
    return output_signal

# Настройки модели
signal = create_signal(t)  # Полезный сигнал
noisy_signal = add_noise(signal, t)  # Сигнал с помехами

# Аналоговая фильтрация
cutoff_frequency = 1e3  # Частота среза фильтра (1 кГц)
analog_filtered_signal = analog_filter(noisy_signal, cutoff_frequency, fs)

# Синхронное детектирование
interference_freq = 50  # Частота синхронной помехи (50 Гц)
sync_filtered_signal = sync_detection(analog_filtered_signal, t, interference_freq)

# Цифровая фильтрация (адаптивный фильтр)
desired_signal = signal  # Ожидаемый полезный сигнал
adaptive_filtered_signal = adaptive_filter(sync_filtered_signal, desired_signal)

# Визуализация результатов
plt.figure(figsize=(12, 8))

# Исходный сигнал с помехами
plt.subplot(4, 1, 1)
plt.plot(t, noisy_signal, label='Сигнал с помехами')
plt.title('Сигнал с помехами')
plt.xlabel('Время (с)')
plt.ylabel('Амплитуда')
plt.grid()
plt.legend()

# Аналоговый фильтр
plt.subplot(4, 1, 2)
plt.plot(t, analog_filtered_signal, label='Аналоговая фильтрация', color='orange')
plt.title('Аналоговая фильтрация')
plt.xlabel('Время (с)')
plt.ylabel('Амплитуда')
plt.grid()
plt.legend()

# Синхронное детектирование
plt.subplot(4, 1, 3)
plt.plot(t, sync_filtered_signal, label='Синхронное детектирование', color='green')
plt.title('Синхронное детектирование')
plt.xlabel('Время (с)')
plt.ylabel('Амплитуда')
plt.grid()
plt.legend()

# Адаптивная фильтрация
plt.subplot(4, 1, 4)
plt.plot(t, adaptive_filtered_signal, label='Адаптивная фильтрация', color='red')
plt.title('Адаптивная фильтрация')
plt.xlabel('Время (с)')
plt.ylabel('Амплитуда')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()