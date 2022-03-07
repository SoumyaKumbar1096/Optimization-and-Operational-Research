import cvxpy as cp
#Exercise 3.1 Water resource

#Scalar Variables
x = cp.Variable() #1000 Litres of water from stream per day
y = cp.Variable() #1000 Litres of water from reservoir per day

#Constraints
constraints = [y <= 100,                    #At most 100,000 litres of water can be taken from the stream
               x/500 + y/500 <= 100,        #Pollutants in the water served to the city can not exceed 100ppm
               x + y == 500                 #City needs 500,000 litres of water per day
               ]

#Objective function
obj = cp.Minimize(100*x + 50*y)             #Cost per 1000 Litres of water.

#Problem solution
prob = cp.Problem(obj, constraints)
prob.solve()
print("Status:", prob.status)
print("optimal value", prob.value)
print("optimal var", x.value*1000, y.value*1000)