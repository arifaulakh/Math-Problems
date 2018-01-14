import math

def strict_floor(x):
	return(-1-math.floor(-x))

def strict_ceil(x):
	return(1-math.ceil(-x))

def gengraph(n):
	G = {}
	for i in range(1,n+1):
		min = strict_ceil(math.sqrt(i))
		max = strict_floor(math.sqrt(2*i))
		G[i] = []
		for j in range(min, max+1):
			G[i].append(j**2-i)
			G[j**2-i].append(i)
	return(G)

def hamilton(G, size, pt, path=None):
	if path == None:
		path = []
	if pt not in set(path):
		path.append(pt)
		if len(path)==size:
			return path
		for pt_next in G.get(pt, []):
			res_path = [i for i in path]
			candidate = hamilton(G, size, pt_next, res_path)
			if candidate is not None:  # skip loop or dead end
				return candidate
    # loop or dead end, None is implicitly returned

def find_ham(n):
	G = gengraph(n)
	for p in G:
		return(hamilton(G,n,p))

print(find_ham(15))