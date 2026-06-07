import csv


def main():
    load('books.csv')


def load(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for line in reader:
            print(line)


main()