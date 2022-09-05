
import random
import matplotlib.pyplot as plt

def p_sierpinski(p1, p2, p3):

    r0, r1 = sorted([random.random(), random.random()])
    x = r0 * p3[0] + (r1-r0)*p2[0] + (1-r1)*p1[0]
    y = r0 * p3[1] + (r1-r0)*p2[1] + (1-r1)*p1[1]

    return (x, y)

p1 = (0, 0)
p2 = (4, 0)
p3 = (p2[0]/2, p2[0]/4) # 0.5, 0.25

points = [p1, p2, p3]

points.append(p_sierpinski(p1, p2, p3))

mat = []
mat.append(((points[-1][0])/2 + p3[0], (points[-1][1])/2 + p3[1]))  # Point(p.x/2 + 0.25, p.y/2 + 0.5)

n = 0
i = 1

while n < 100000:
    mat.append(((mat[i-1][0] + p2[0]) / 2, (mat[i-1][1] + p2[1]) / 2))
    mat.append(((mat[i][0] + p1[0]) / 2, (mat[i][1] + p1[1]) / 2))
    mat.append(((mat[i+1][0] + p3[0]) / 2, (mat[i+1][1] + p3[1]) / 2))

    points.append(mat[i-1])
    points.append(mat[i])
    points.append(mat[i+1])

    i += 2
    n += 1

x, y = zip(*points)
plt.scatter(x, y, s=0.1)
plt.show()