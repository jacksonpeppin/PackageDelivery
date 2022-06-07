import csv
import Package

class ReadDistances:

    def __init__(self):
        with open('data/WGUPS_Distances.csv') as csvfile:
            """
            distances is a 2 dimensional array holding values for the distance between two addresses
            addresses is a dictionary: give it an address and it will have the index of the address in the distances
            2d array
            """
            read_distances = csv.reader(csvfile, delimiter=',')
            self.distances = []
            for row in read_distances:
                self.distances.append(row)

        with open('data/WGUPS_Addresses.csv') as csvfile:
            read_addresses = csv.reader(csvfile, delimiter=',')
            self.addresses = {}
            for row in read_addresses:
                self.addresses[row[2]] = row[0]

    def get_distance(self, address_one, address_two):
        """
        This function returns the distance between two addresses.
        to retrieve the distance from distances[x][y]
        x must be greater than y because distances 2d array has shape:
        []
        [][]
        [][][]
        [][][][]
        [][][][][]
        :param address_one:
        :param address_two:
        :return: distance between address one and two
        """
        x = int(self.addresses.get(address_one))
        y = int(self.addresses.get(address_two))
        if x > y:
            return float(self.distances[x][y])
        else:
            return float(self.distances[y][x])

    def min_distance_from(self, current_address, packages):
        """
        This algorithm delivers packages by finding the next closest address to deliver to
        :param current_address:
        :param packages:
        :return: the distance traveled and the next package to be delivered
        """
        minimum = 99.9
        for p in packages:
            if not p.get_delivered():
                d = self.get_distance(current_address, p.get_address())
                if d < minimum:
                    minimum = d
                    next_package = p
        # next_package.set_delivered()
        return [minimum, next_package]


