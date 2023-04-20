
import gurobipy as gp
m = gp.Model("test")
x = m.addVar()
m.setObjective(x)
m.optimize()
