import csv

from HashTable import HashTable
from Package import Package


class ReadPackages:

    # import package data from csv file in to hash table
    def __init__(self):
        self.packages = HashTable()
        with open('data/WGUPS_Packages.csv') as csvfile:
            read_packages = csv.reader(csvfile, delimiter=',')
            for row in read_packages:
                p = Package(int(row[0]), row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                self.packages.add(p.get_id(), p)

    def get_packages(self):
        """
        :return: a hashtable with every package imported from the csv contained within
        """
        return self.packages

    def print_packages(self):
        """
        print every package
        """
        self.packages._print()


