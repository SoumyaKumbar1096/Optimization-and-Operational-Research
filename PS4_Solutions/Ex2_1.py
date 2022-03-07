import cvxpy as cp
#Exercise 2.1 

#Scalar Variables
x = cp.Variable()
y = cp.Variable()

#Constraints
constraints = [x >= 0,
               y >= 0]

#Form Objective
obj = cp.Minimize((x-4)**2 + 7*((y-4)**2) + 4*y)

#Form and solve problem
prob = cp.Problem(obj, constraints)
prob.solve()
print("Status:", prob.status)
print("Optimal value:", prob.value)
print("optimal var:", x.value, y.value)