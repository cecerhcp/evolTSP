from random import *

def generate_graph(n):
	seed()
	graph = []
	for i in range(n):
		line = []
		for j in range(n):
			if i == j: line.append(0)
			else : line.append(randint(1, 10))
		graph.append(line)
	return graph

class Solution:
	n = 4
	graph = {}
	population_costs = []
	population = []

	def __init__(self, n, adj, population_size = 100): 
		seed()
		self.n = n
		self.read_graph(n, adj)
		self.generate_population(population_size)
		self.population_size = population_size

	def read_graph(self, n, adj):
		for i in range(n):
			line = adj[i]
			for j in range(n):
				self.graph[(i, j)] = line[j]

	def generate_population(self, size):
		for i in range(size):
			path = list(range(1, self.n))
			shuffle(path)
			self.population.append([0] + path + [0])
		self.renew_population_costs()

	def solve(self, gens = 100):
		for i in range(gens):
			self.fit_function()
			self.mutate_population()
		print(self.graph)
		#print(self.population)
		print("minimum evolved: " + str(min(self.population_costs)))

	def random_solve(self, number):
		self.population = []
		self.population_costs = []
		self.generate_population(number)
		print("minimum random: " + str(min(self.population_costs)))

	def fit_function(self):
		new_population = []
		y = max(self.population_costs) * 2
		lim = int(self.population_size / 2)
		for i in range(lim):
			x = self.population_costs.index(min(self.population_costs))
			new_population.append(self.population[x])
			self.population_costs[x] = y
		self.population = new_population
		self.renew_population_costs()

	def renew_population_costs(self):
		x = len(self.population)
		self.population_costs = [None] * len(self.population)
		for i in range(x):
			self.population_costs[i] = self.get_population_cost(self.population[i])

	def get_population_cost(self, path):
		cost = 0
		for i in range(self.n):
			edge = (path[i], path[i+1])
			cost = cost + self.graph[edge]
		return cost

	def mutate_population(self):
		newpaths = []
		for path in self.population:
			mutate = randint(1, 100)
			if mutate <= 20:
				x = randint(1, self.n - 1)
				y = randint(1, self.n - 1)
				path[x], path[y] = path[y], path[x]
			newpath = path[:]
			newpaths.append(newpath)
		self.population = self.population + newpaths
		self.renew_population_costs()

n = 20
gens = 100
x = generate_graph(n)
sol = Solution(n, x)
sol.solve(gens)
sol.random_solve(5000)
