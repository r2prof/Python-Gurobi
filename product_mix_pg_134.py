# Import Gurobi
import gurobipy as gp 

# Import Gurobi's optimization methods
from gurobipy import GRB 

# Create a new model
model = gp.Model()

# Add decision variables
x1 = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="x1")
x2 = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="x2")
x3 = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="x3")
x4 = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="x4")

# Set objective function
model.setObjective(90*x1 + 125*x2 + 45*x3 + 65*x4, sense=GRB.MAXIMIZE)

# Add constraints
model.addConstr(0.1*x1 + 0.25*x2 + 0.08*x3 + 0.21*x4 <= 72)
model.addConstr(3*x1 + 3*x2 + x3 + x4 <= 1200)
model.addConstr(36*x1 + 48*x2 + 25*x3 + 35*x4 <= 25000)
model.addConstr(x1 + x2 <= 500)
model.addConstr(x3 + x4 <= 500)

# Optimize model
model.optimize()

# Print optimal solution
print("Optimal solution:")
print("x1 =", x1.x)
print("x2 =", x2.x)
print("x3 =", x3.x)
print("x4 =", x4.x)
print("Objective value =", model.objVal)

# python 1.py > output.txt
