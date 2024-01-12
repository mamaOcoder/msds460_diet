# Assignment 1: The Diet Problem

## Project Summary
This week we were asked construct a personalized diet using current recommended dietary allowances from the U.S. Food and Drug Administration. The goal was to build a linear programming model to minimize the cost of meals given the FDA constraints. 

### Setting up the Problem
Meals were selected based on items that were available in my pantry/refridgerator. To keep it simple, each meal consist of 2 items (except one which is a single frozen meal). Nutrition information was simply pulled from the item's label. To calculate the cost of each meal, the price- found from the online store where I purchased the items (WholeFoods)- was divided by the number of servings in the package.

| Meal                      | Price |  Sodium  |  Calories  |  Protein  |  VitaminD  | Calcium  |  Iron  |  Potassium  |
| ----------------------    | ------| -------- | ---------- | --------- | ---------- | -------- | ------ | ----------- |
| Oatmeal & Almond Butter   | 1.16  |  0       |  360       |  12       |  0         |  105     |  3.2   |  392        |
| Chicken & Rice            | 1.78  |  80      |  270       |  27       |  0         |  0       |  0.9   |  410        |
| Pasta                     | 0.82  |  400     |  260       |  8        |  0         |  50      |  1.3   |  580        |
| Salmon & Quinoa           | 4.13  |  90      |  310       |  31       |  15.9      |  0       |  2.2   |  700        |
| Enchilada                 | 5.49  |  890     |  450       |  20       |  0.8       |  390     |  2.3   |  430        |

**Objective Function:**  
Minimize: 1.16o + 1.78c + 0.82p + 4.13s + 5.49e

**Constraints:**  
To satisfy a weekly diet, the FDA recommended daily requirements were multiplied by 7.  
80c + 400p + 90s + 890e             <= 35000 	[sodium intake]  
360o + 270c + 260p + 310s + 450e    >= 14000	[energy/calorie intake]   
12o + 27c + 8p + 31s + 20e          >= 350		[protein intake]   
15.9s + 0.8e                        >= 140 		[vitamin D intake]   
105o + 50p + 390e                   >= 9100     [calcium intake]   
3.2o + 0.9c + 1.3p + 2.2s + 2.3e    >= 126		[iron intake]   
392o + 410c + 580p + 700s + 430e    >= 32900	[potassium intake]   

## AMPL
To solve this linear problem, I utilized the AMPL API for Python. In my initial code (assignment1_ampl.py), I followed an example in [Hands-On Optimization with AMPL in Python](https://ampl.com/mo-book/notebooks/01/production-planning-basic.html). After the sync-session on Thursday, I chose to rewrite the code following the example that Dr. Miller provided, which allows the AMPL model to be used across languages.

## Results
The minimum weekly cost for these meals given the nutritional constraints is $136.90. The breakdown of the meals is not very interesting- 86.7 servings of oatmeal and 8.8 servings of salmon.

A second run of the problem was conducted after adjusting the constraints to ensure at least one serving of each meal was included. The updated minimum weekly cost was $139.92. The breakdown of meals did not improve much- 82.5 servings of oatmeal, 8.8 servings of fish and 1 serving of all other meals. To make the weekly menu more interesting, we could add additional constraints such as capping the number of oatmeal servings we would be willing to eat. Additionally, if we were to alter the recipe for preparing the oatmeal to include salt (sodium), the results would likely change.

## Files
### *assignment1_ampl.py*
Initial attempt at running the linear program using the AMPL API. This followed the [Hands-On Optimization with AMPL in Python](https://ampl.com/mo-book/notebooks/01/production-planning-basic.html) book.

### *assignment1_pulp.py*
This file contained code for using the PuLP package. I did this to compare PuLP and AMPL results. Both approaches produced the same results.

### *amplpy-diet.py*
This file contains code to run the linear program using the AMPL API. This is an edited copy of the code provided by Dr. Miller.

### *diet.dat*
This is the data file for the linear programming problem. It follows the format described in [AMPL: A Modeling Language for Mathematical Programming](https://ampl.com/wp-content/uploads/BOOK.pdf).

### *diet.mod*
This is the model file for the linear programming problem. It follows the format described in [AMPL: A Modeling Language for Mathematical Programming](https://ampl.com/wp-content/uploads/BOOK.pdf).

### *images/*
This folder contains images of the food items and their nutritional label used for the assignment.

### *results/*
This folder contains text files of the outputs of the 4 runnings of the program.
