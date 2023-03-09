import csv
import matplotlib.pyplot as plt
import time

def points(csv_filename):
    with open(csv_filename, newline='') as csv_file:
        csv_reader = csv.reader(csv_file)

        # Skip the header row
        next(csv_reader)

        # Extract x and y values from each row and append to list
        data_list = []
        for row in csv_reader:
            x = float(row[2])
            y = float(row[3])
            data_list.append((x, y))
    
    return data_list

def scatter(data, hubs, title):
    x_values1 = [x for x, y in data]
    y_values1 = [y for x, y in data]
    x_values2 = [x for x, y in hubs]
    y_values2 = [y for x, y in hubs]

    # Create scatter plot
    plt.scatter(x_values1, y_values1, s=1)
    plt.scatter(x_values2, y_values2, color='red', s=100)

    # Add axis labels and title
    plt.title(title)

    # Display plot
    plt.show()

def preprocess(points):
    mapp = {}
    for point in points:
        int_pt = (int(point[0]), int(point[1]))
        if int_pt in mapp:
            mapp[int_pt] = mapp[int_pt] + 1
        else:
            mapp[int_pt] = 0
    
    return mapp

def density(query_point, mapp):
    int_pt = (int(query_point[0]), int(query_point[1]))
    if int_pt in mapp:
        return mapp[int_pt]
    return 0


def hubs(k, r, mapp):
    k_hubs = []
    while k > 0:
        # dpt is densest point
        dpt = max(mapp, key=lambda x:density(x, mapp))
        k_hubs.append(dpt)

        for point in list(mapp):
            if r >= euclid(dpt, point):
                del mapp[point]
        
        k = k-1
    
    return k_hubs

def euclid(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5

def main():
    filename = "geolife-cars-sixty-percent.csv"
    k = 10
    r = 8

    pts = points(filename)
    data = preprocess(pts)

    s = time.time()
    hhubs = hubs(k, r, data.copy())
    e = time.time()

    print('elapsed time: ' + str(e-s))

    #title = "100%"
    #scatter(data, hhubs, title)

    

if __name__ == "__main__":
    main()