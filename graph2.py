import fit_black_box as bb
import math

filename = 'graph2.txt'
x, y, xerr, yerr = bb.load_data(filename)



def linear (m, x, b):
    return m * x + b

init_guess = (0, 1)
font_size = 20
xlabel = "Current [mA]"
ylabel = "Voltage [V]"
title = "Relationship between Voltage [V] and Current [mA]"


bb.plot_fit(linear, x, y, xerr, yerr, init_guess=init_guess, font_size=font_size, title=title,
            xlabel=xlabel, ylabel=ylabel)
