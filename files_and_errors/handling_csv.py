import csv

# scores = []
# with open("some_data.csv") as csvfile:
#     csvreader = csv.reader(csvfile)
#     headers = list(map(str.lstrip, next(csvreader)))

#     for row in csvreader:
#         scores.append(int(row[-1]))

# print(headers)
# print(scores)

# scores = []
# with open("some_data.csv") as csvfile:
#     csvreader = csv.reader(csvfile)
#     print(list(csvreader))  # list of lists


# data_to_write = [["David", 5], ["Paula", 6], ["Nish", 7]]

# with open("new_data.csv", "w") as csvfile:
#     csv_writer = csv.writer(csvfile)
#     csv_writer.writerows(data_to_write)


def iris_reader(filename):
    with open(filename, "r") as csvfile:
        csvreader = list(csv.reader(csvfile))
    return csvreader


def column_mean(filename, csvreader):
    csvreader = csvreader[1:]
    column_means = []
    for x in range(4):
        sum = 0
        for row in csvreader:
            sum += float(row[x])
        mean = sum / len(list(csvreader))
        column_means.append(mean)
    return column_means


iris_means = column_mean("iris.csv", iris_reader("iris.csv"))

print(iris_means)  

iris_means_with_headers = f"sepal_length, {iris_means[0]}, \nsepal_width, {iris_means[1]}, \npetal_length, {iris_means[2]}, \npetal_width, {iris_means[3]}"

with open("iris_mean.csv", "a") as opened_csv:
     opened_csv.write(iris_means_with_headers)
