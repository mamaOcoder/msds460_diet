from pulp import LpVariable, LpProblem, LpMaximize, LpStatus, value, LpMinimize

# define decision variables
o = LpVariable("oatmeal", 0, None)
c = LpVariable("chicken", 0, None)
p = LpVariable("pasta", 0, None) 
s = LpVariable("salmon", 0, None) 
e = LpVariable("enchilada", 0, None) 

# defines the problem
prob = LpProblem("problem", LpMinimize)

# define constraints
prob += 80*c + 400*p + 90*s + 890*e <= 35000    #sodium
prob += 360*o + 270*c + 260*p + 310*s + 450*e >= 14000  #calories
prob += 12*o + 27*c + 8*p + 31*s + 20*e >= 350  #protein
prob += 15.9*s + 0.8*e >= 140   #vitamin d
prob += 105*o + 50*p + 390*e >= 9100    #calcium
prob += 3.2*o + 0.9*c + 1.3*p + 2.2*s + 2.3*e >= 126    #iron
prob += 392*o + 410*c + 580*p + 700*s + 430*e >= 32900  #potassium

# define objective function
prob += 1.16*o + 1.78*c + 0.82*p + 4.13*s + 5.49*e

# solve the problem
status = prob.solve()
print(f"Problem")
print(f"status={LpStatus[status]}")

# print the results
for variable in prob.variables():
    print(f"{variable.name} = {variable.varValue}")
    
print(f"Objective = {value(prob.objective)}")
print(f"")