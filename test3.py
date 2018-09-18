from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import random, math, kmeans, copy

# Elements list
elements = []

# Open txt file containing brazillian DNS servers
f = open('ips.txt','r')
for i in f:
	# Split IPs by , (comma)
	l = i.split(',')
	for j in l:
		# Split IP by . (dot)
		c = j.split('.')
		for n in range(len(c)):
			# Convert string to float
			c[n] = float(c[n])
		elements.append(c)

# For choosing later
klist = []
# Testing K amount into dataset
errors = []
ki = []
for k in range(1,20):
	print "Training KMeans with K = ",k," centroids"
	kn = kmeans.KMeans(k, copy.deepcopy(elements))
	# Training it
	kn.train()
	# Measuring its error
	er = kn.error()
	print "Measured error: ", er
	errors.append(er)
	ki.append(k)
	# For choosing later
	klist.append(kn)

print "\n||||||||||||||||||||||||||||||||||||||||||||||||\n"
print "Check the graph to choose the best K value"
print "The K amount closest to the elbow is the better"
print "In this dataset the trained set with K = 4 centroids usually looks nice..."
print "The ideal K amount may vary according to your dataset..."

# Plot error decrease with Matplotlib
plt.plot(ki,errors, c='y' ,marker='s')
plt.xlabel('K amount')
plt.ylabel('Measured error')
plt.legend(["Error as K increase"])
plt.show()

print "Enter K amount (int):"
# Choose K
km = klist[int(raw_input())-1]
Kcentroids = km.centroids

print "Press Enter to plot 3D view from dimensions as each IP 1st, 2nd and 3rd Octet"
z = raw_input()

# Plot colored clusters with Matplotlib
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

legend = []
for kcluster in Kcentroids:
	legend.append('K'+str(Kcentroids.index(kcluster))+' Elements')
	legend.append('K'+str(Kcentroids.index(kcluster))+' Centroid')
	ax.scatter(kmeans.get_column_values(kcluster.elements,0), kmeans.get_column_values(kcluster.elements,1), kmeans.get_column_values(kcluster.elements,2), c=kcluster.color, marker='*')
	ax.scatter(kcluster.position[0], kcluster.position[1], kcluster.position[2], c=kcluster.color, marker='^')

ax.set_xlabel('A')
ax.set_ylabel('B')
ax.set_zlabel('C')
plt.legend(legend)
plt.show()

print "Press Enter to plot 3D view from dimensions as each IP 2nd, 3rd and 4th Octet"
z = raw_input()

# Plot colored clusters with Matplotlib
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for kcluster in Kcentroids:
	ax.scatter(kmeans.get_column_values(kcluster.elements,1), kmeans.get_column_values(kcluster.elements,2), kmeans.get_column_values(kcluster.elements,3), c=kcluster.color, marker='*')
	ax.scatter(kcluster.position[1], kcluster.position[2], kcluster.position[3], c=kcluster.color, marker='^')

ax.set_xlabel('B')
ax.set_ylabel('C')
ax.set_zlabel('D')
plt.legend(legend)
plt.show()
