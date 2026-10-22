import matplotlib.pyplot as plt
import numpy as np
from pupupu import step, line_width
from math import *

def graf(exp, xmax):
    try:
        xmax = int(xmax)

        if xmax <= 0:
            return "Диапазон X должен быть больше 0"

        xlist = np.arange(-xmax, xmax + step, step)
        y_list = []

        for x in xlist:
            try:
                y = eval(exp)

                if np.isfinite(y):
                    y_list.append(y)
                else:
                    y_list.append(np.nan)

            except (ZeroDivisionError, ValueError, OverflowError):
                y_list.append(np.nan)

            except Exception:
                return "Ошибка в выражении"

        fig, ax = plt.subplots()

        ax.plot(xlist, y_list, color="green")
        ax.axhline(0, color="black", linewidth=line_width)
        ax.axvline(0, color="black", linewidth=line_width)

        ax.set_xticks(np.arange(-xmax, xmax + 1, 1))
        ax.set_yticks(np.arange(min(y_list), max(y_list) + 1, 1))

        ax.grid(True)
        ax.set_aspect("equal", adjustable="box")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_xlim(-xmax, xmax)

        plt.show()
        return None

    except Exception as e:
        return f"Ошибка: {e}"
