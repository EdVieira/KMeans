from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import random, math, kmeans
print kmeans.KMeans

elements = []

# Random elements
for i in range(150):
	x = random.randint(0,255)
	y = random.randint(0,255)
	z = random.randint(0,255)
	elements.append([x,y,z])


km = kmeans.KMeans(3, elements)
Kcentroids = km.centroids
print 'Cluster list',Kcentroids

check_stop = True

while check_stop:
	check_stop = km.step()

	#plot points
	#plt.plot(kmeans.get_column_values(elements,0),kmeans.get_column_values(elements,1), 'bs')

	for kcluster in Kcentroids:
		print 'Centroid:', kcluster
		print 'Position: ',kcluster.position
		print 'Elements: ',kcluster.elements
		for element in kcluster.elements:
			plt.plot(element[0],element[1], c=kcluster.color ,marker='*')
		plt.plot(kcluster.position[0],kcluster.position[1], c=kcluster.color, marker='^')
	plt.xlabel('x')
	plt.ylabel('y')
	plt.legend()
	plt.show()
	###


print "Done centroid positioning"
z = raw_input()


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#ax.scatter(kmeans.get_column_values(elements,0), kmeans.get_column_values(elements,1), kmeans.get_column_values(elements,2), c='b', marker='s')

for kcluster in Kcentroids:
	print 'Centroid:', kcluster
	print 'Position: ',kcluster.position
	print 'Elements: ',kcluster.elements
	ax.scatter(kmeans.get_column_values(kcluster.elements,0), kmeans.get_column_values(kcluster.elements,1), kmeans.get_column_values(kcluster.elements,2), c=kcluster.color, marker='*')
	ax.scatter(kcluster.position[0], kcluster.position[1], kcluster.position[2], c=kcluster.color, marker='^')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()