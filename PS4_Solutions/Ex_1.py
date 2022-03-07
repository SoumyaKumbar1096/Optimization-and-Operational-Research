import cvxpy as cp
#Exercise 1 using CVXPY

#Create scalar Optimization Variables
x=cp.Variable()
y=cp.Variable()

#Create constraints
constraints = [x+y == 1,
               x-y >= 1]

#Form Objective
obj = cp.Minimize((x-y)**2)

#Form and solve problem.
prob = cp.Problem(obj, constraints)
prob.solve()
print("Status:", prob.status)
print("optimal value", prob.value)
print("optimal var", x.value, y.value)

"""# Unconstrained optimization"""