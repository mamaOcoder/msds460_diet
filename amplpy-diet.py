#!/usr/bin/env python
# -*- coding: utf-8 -*-
# drawing on documentation provided in 
#  https://buildmedia.readthedocs.org/media/pdf/amplpy/latest/amplpy.pdf
import sys
import os
from amplpy import AMPL, Environment

def main(argc, argv):

    ampl = AMPL(Environment('/Applications/AMPL'))

    ampl.setOption('solver', 'cplex')

    # Read the model and data files.
    model_directory = "/Users/lesles/Documents/NW Master's/MSDS 460- Decision Analytics/Assignments/Assignment1"
    ampl.read(os.path.join(model_directory, 'diet.mod'))
    ampl.read_data(os.path.join(model_directory, 'diet.dat'))

    # Solve
    ampl.solve()

    # Get objective entity by AMPL name
    totalcost = ampl.get_objective('Total_Cost')
    # Print it
    print('Objective is:', totalcost.value())

    # Update problem to require at least one serving of each meal
    meal_mins = ampl.get_parameter('f_min')
    min_serv = [1,1,1,1,1]
    meal_mins.set_values(min_serv)
    
    # Resolve and display objective
    ampl.solve()
    print('New objective value:', totalcost.value())

    # Get the values of the variable Buy in a dataframe object
    buy = ampl.get_variable('Buy')
    df = buy.get_values()
    # Print them
    print(df)

if __name__ == '__main__':
    try:
        main(len(sys.argv), sys.argv)
    except Exception as e:
        print(e)
        raise