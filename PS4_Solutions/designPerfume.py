import cvxpy as cp
#Exercise 3.2 to design a good smelling new perfume

#Scalar Variables
a = cp.Variable()     #Percentage of Blend 1
b = cp.Variable()     #Percentage of Blend 2
c = cp.Variable()     #Percentage of Blend 3
d = cp.Variable()     #Percentage of Blend 4

#Contraints
constraint = [a <= 25, a >= 10, 
               b <= 20, b >= 5, 
               c >= 30,
               ((35*a) + (60*b) + (35*c) + (40*d)) <= 50,
               ((15*a) + (5*b) + (20*c) + (10*d)) <= 13,
               ((15*a) + (5*b) + (20*c) + (10*d)) >= 8,
               ((30*a) + (20*b) + (40*c) + (20*d)) <= 35,
               ((20*a) + (15*b) + (5*c) + (30*d)) >= 19,
               a + b + c + d == 100
                ]

#Objective Function
obj = cp.Minimize((55*a) + (65*b) + (35*c) + (85*d))

#Problem solution
prob = cp.Problem(obj, constraint )
prob.solve()
print("Status:", prob.status)
print("optimal value", prob.value)
print("optimal var", a.value, b.value, c.value, d.value)