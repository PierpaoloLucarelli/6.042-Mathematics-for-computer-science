import numpy as np
N = 5

boys = []
girls = []

def random_preferences():
	return np.random.permutation(N).tolist()



def mating_algorithm(n, boys, girls):
	balconies = [[] for i in range(N)]
	# morning
	while(terminating_condition(balconies) == False):
		for i in range(n): # each boy
			if len(boys[i]) != 0:
				pref = boys[i][0]
				if(i not in balconies[pref]):
					balconies[pref].append(i)
		# afternoon
		for i in range(n):
			if(len(balconies[i]) >= 2):
				choice, rejects = get_girl_preference(balconies[i], i)
				balconies[i] = [choice]
				# evening (remove girl from list of preferences)
				for i in range(len(rejects)):
					boys[rejects[i]].pop(0)
	return balconies

def get_girl_preference(balc, girl):
	g_pref = girls[girl]
	for i in range(N):
		for j in range(len(balc)):
			if(g_pref[i] == balc[j]):
				choice = balc[j]
				balc.pop(j)
				return choice, balc

def terminating_condition(balconies):
	for i in range(len(balconies)):
		if(len(balconies[i]) != 1):
			return False
	return True

for i in range(N):
	boys.append(random_preferences())
	girls.append(random_preferences())

matches = mating_algorithm(N, boys, girls)
print(matches)



