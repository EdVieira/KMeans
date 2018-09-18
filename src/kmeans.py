import random, math

def get_column_values(mat,col):
	# get column values from matrix
	res = []
	for i in mat:
		res.append(i[col])
	return res

def random_color():
	# generate random HEX color string
	r = str(hex(random.randint(0,0xFF))).split('x')[1]
	g = str(hex(random.randint(0,0xFF))).split('x')[1]
	b = str(hex(random.randint(0,0xFF))).split('x')[1]
	rgb = r.join(g).join(b)
	color = rgb
	c = ''
	for i in color:
		c += chr(ord(i.upper()))
	while len(c)<6:
		c ='0'+c
	c = '#'+c
	return c

def euclideanNdist(element, centroid):
		#Euclidean distance by N dimensions
		rad = 0
		#print element, centroid.position
		for dimension in range(len(element)):
			rad += (element[dimension]-centroid.position[dimension])**2
		return math.pow(rad, 2)

class KCentroid(object):
	"""docstring for KCentroid
		Its position must be the mean of its elements
		on all of its dimensions.
	"""
	def __init__(self, position = None, color = None):
		super(KCentroid, self).__init__()
		if position == None:
			self.position = [] # N Dimensional coordinates
		else:
			self.position = position
		if color == None:
			self.color = '#FF0000'
		else:
			self.color = color
		self.elements = []
	
	def checkIfChanged(self):
		# Check if the mean on it set of elements of N dimension have changed
		# If so, change centroid position to the new mean coordinates
		if len(self.elements) < 1:
			# False if it have no elements
			return False
		dimensions = []
		# Get each dimension values
		for dimension in range(len(self.elements[0])):
			dimensions.append(get_column_values(self.elements, dimension))
		# Calculate each dimension mean
		for i in range(len(dimensions)):
			dimensions[i] = sum(dimensions[i])/len(dimensions[i])
		# If calculated means are the same as its position
		if self.position == dimensions:
			# So it have no changes
			return False
		else:
			# Else, it changes the centroid position to the new coordinates
			self.position = dimensions
			return True

	def error(self):
		# Return K centroid error
		error = .0
		for n in self.elements:
			error += euclideanNdist(n,self)**2
		return error

class KMeans(object):
	"""docstring for KMeans
		KMeans is a set of centroids N dimensionals
	"""
	def __init__(self, nKcentroids = None, elements = None):
		super(KMeans, self).__init__()
		if nKcentroids != None or elements != None:
			if nKcentroids < 1: nKcentroids = 1
			self.centroids = self.setKCentroids(nKcentroids,elements)
			self.elements = elements
			self.elements.sort()
		else:
			self.centroids = []
			self.elements = []
		
	def setKCentroids(self, nKcentroids, elements):
		res = []
		for i in range(nKcentroids):
			position = []
			minx, maxx = 0, 0
			for p in range(len(elements[0])):
				# Set new element coordinates for its N dimensions
				signal = random.random()
				if signal < 0.1: signal = -1
				else: signal = 1
				column = get_column_values(elements,p)
				minx, maxx = min(column), max(column)
				amp = abs(maxx-minx)
				mean = sum(column)/len(column)
				# Around the elements mean
				p = mean + amp*0.1*signal
				position.append(p)
			kCentroid = KCentroid(position, random_color())
			res.append(kCentroid)
		return res

	def train(self):
		check_stop = True
		while check_stop:
			check_stop = self.step()
		return self.centroids

	def step(self):
		#Clear centroids elements
		for k in self.centroids:
			k.elements = []
		# Assigns centroid elements
		for i in range(len(self.elements)):
			self.predict(self.elements[i])
		return self.checkStop()

	def predict(self, element):
		# Attach element to the closest centroid
		# Return centroid
		distance = float('inf')
		centroid = None
		for K in self.centroids:
			#Euclidean distance by N dimensions
			KijDistance = euclideanNdist(element,K)
			###
			if KijDistance <= distance:
				distance = KijDistance
				centroid = K
		# Attach element to centroid
		centroid.elements.append(element)
		return centroid

	def checkStop(self):
		# Check if no centroid have changed
		check_stop = []
		i = 0
		while i != len(self.centroids):
			check_stop.append(self.centroids[i].checkIfChanged())
			i += 1
		return any(check_stop)

	def error(self):
		# Return K set error
		error = .0
		for k in self.centroids:
			error += k.error()
		return error