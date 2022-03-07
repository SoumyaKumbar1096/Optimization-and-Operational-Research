import cvxpy as cp
#Exercise 2.3 using log-barrier function

#Scalar Variables
x = cp.Variable()
y = cp.Variable()

#Contraints
constraints = [-x-y <= -4,
               x >= 0,
               y >= 0]

#Objective Functions
obj=cp.Minimize((x-2)**2 + (3*y))

#Problem solution
prob = cp.Problem(obj, constraints)
prob.solve()
print("Status:", prob.status)
print("optimal value", prob.value)
print("optimal var", x.value, y.value)