# Grafica
from enum import Enum
import matplotlib.pyplot as plt
import numpy as np
import os

exit = True

# Set default values to be used
default_freq = 1000
default_cycle = 4

# Enum for options in menu
class option_list(Enum):
    FREQ = 1
    SAMPLE_FREQ = 2
    NUM_CYCLE_SHOWN = 3
    GRAPH = 4
    EXIT = 5


while (exit):
    print("""
    1) Set analog signal frequency (Hz)
    2) Set sample frequency
    3) Set number of cycles to graph for the signal
    4) Create graph of the signal
    5) Exit
    """)
    option = int(input("Select an option: "))
    os.system('clear')

    match option:
        case option_list.FREQ.value:
            check = True
            while check: 
                try: 
                    freq = float(eval(input("Input desired frequency for analog signal (Hz): ")))
                except:
                    print("ERROR: Could not convert value to float. Input a valid number")
                    continue
                if freq < 0:
                    print("ERROR: Frequency must be positive")
                else:
                    print(f"Setting frequency to: {freq}Hz")
                    check = False
    
        case option_list.SAMPLE_FREQ.value:
            check = True
            while check: 
                try: 
                    sample_freq = float(eval(input("Input desired sample frequency: ")))
                except:
                    print("ERROR: Could not convert value to float. Input a valid number")
                    continue
                if sample_freq < 0:
                    print("ERROR: Sample frequency must be positive")
                else:
                    print(f"Setting frequency to: {sample_freq}")
                    check = False

        case option_list.NUM_CYCLE_SHOWN.value:
            check = True
            while check: 
                try: 
                    num_cycle = int(input("Input number of cycles to display: "))
                except:
                    print("ERROR: Could not convert value to int. Input a valid number")
                    continue
                if num_cycle <= 0:
                    print("ERROR: Must display at least 1 cycle")
                else:
                    print(f"Setting number of cycles shown to: {num_cycle}")
                    check = False

        case option_list.GRAPH.value:
            # Avoid failing by using default values
            try:
                freq
            except NameError:
                print(f"Frequency was not set. Using default value {default_freq}Hz")
                freq = default_freq
            try:
                sample_freq
            except NameError:
                print(f"Sample frequency was not set. Setting value to analog frequency {freq}*2")
                sample_freq = freq * 2
            try:
                num_cycle
            except NameError:
                print(f"Number of displayed cycles was not set. Using default number of cycles: {default_cycle}")
                num_cycle = default_cycle

            # Sine wave
            time_shown = (1/freq) * num_cycle
            time = np.linspace(0, time_shown, 10000)
            y_sin = np.sin(2*np.pi*freq*time)

            # Sampled sine wave
            x_sin_sample =  np.arange(0, time_shown, 1/sample_freq)
            y_sin_sample = np.sin(2*np.pi*freq*x_sin_sample)

            # Check for aliased frequency
            norm_freq = freq/sample_freq
            plot_alias_freq = False
            if norm_freq > 0.5:
                alias_freq = 1000
                n = 1
                plot_alias_freq = True
                while(alias_freq > 0.5):
                    old_alias_freq = alias_freq
                    alias_freq = norm_freq - n
                    n = n + 1
                    if alias_freq < -0.5:
                        alias_freq = old_alias_freq
                        break
                alias_freq = alias_freq * sample_freq
                y_sin_alias = np.sin(2*np.pi*alias_freq*time)

            plt.plot(time, y_sin, label="x(t)", color="blue", linewidth=2)
            plt.scatter(x_sin_sample, y_sin_sample, label="x[n]", color="red")
            plt.vlines(x_sin_sample, ymin=0, ymax=y_sin_sample, colors='red', linestyles='dashed')
            if plot_alias_freq:
                plt.plot(time, y_sin_alias, label="x_alias(t)", color="orange", linewidth=2)

            plt.title("Tarea 1")
            plt.xlabel("t(s)")
            plt.ylabel("Amplitude")
            plt.legend()
            plt.grid(True)
            plt.show()

        case option_list.EXIT.value:
            print("Exiting.... ")
            exit = False
        case _:
            print("Invalid option. Select a number from 1-4")
