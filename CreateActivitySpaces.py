import csv
import random

# execfile("create_act_spaces.py")
list_point_x = []
list_point_y = []
home = []
work = []
rec1 = []
rec2 = []
reader = csv.reader(open("nodes_ftl.csv", "rb"), delimiter=",")
for row in reader:
    list_point_x.append(row[14])
    list_point_y.append(row[15])
print len(list_point_x)
print len(list_point_y)
for agent in range(0, 1500, 1):
    temp = []
    rng_h = random.randint(1, 7000)
    rng_work = random.randint(1, 7000)
    rng_rec1 = random.randint(1, 7000)
    rng_rec2 = random.randint(1, 7000)
    writer = csv.writer(open("a"+str(agent)+".csv", "wb"))
    writer.writerow(["id", "point_x", "point_y"])
    writer.writerow([rng_h, list_point_x[rng_h], list_point_y[rng_h]])
    writer.writerow([rng_work, list_point_x[rng_work], list_point_y[rng_work]])
    writer.writerow([rng_rec1, list_point_x[rng_rec1], list_point_y[rng_rec1]])
    writer.writerow([rng_rec2, list_point_x[rng_rec2], list_point_y[rng_rec2]])
raw_input()
