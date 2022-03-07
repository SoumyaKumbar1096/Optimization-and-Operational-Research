import cvxpy as cp
#Exercise 2.2

#Scalar Variables
x = cp.Variable()
y = cp.Variable()
z = cp.Variable()

#COntraints
constraints = [x >= 0,
              y >= 0]
#Form objective
obj=cp.Minimize((x**3)+((y-z)**2)+(z**3)+2)

prob=cp.Problem(obj, constraints)
prob.solve()
print("Status:", prob.status)
print("Optimal value:", prob.value)
print("optimal var:", x.value, y.value, z.value)