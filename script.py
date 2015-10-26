import sys
from solution import *

n = int(sys.argv[1])
gens = int(sys.argv[2])
x = generate_graph(n)
sol = Solution(n, x)
sol.solve(gens)
sol.random_solve(10000)