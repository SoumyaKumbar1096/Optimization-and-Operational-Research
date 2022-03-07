from numpy import log
import cvxpy as cp
#Exercise 3.3 to Maximize Roadway expenses

#Scalar Variables
x = cp.Variable()  #Amount spent on Rural project in Millions
y = cp.Variable()  #Amount spent on Urban projects in Millions

#Contraints
constraint = [x + y <= 200]

#Objective Function
obj = cp.Maximize( (7000*cp.log(1+x)) + (5000*cp.log(1+y)) - x - y )

#Problem solution
prob = cp.Problem(obj, constraint)
prob.solve()
print("Status:", prob.status)
print("optimal value", prob.value)
print("optimal var", x.value, y.value)