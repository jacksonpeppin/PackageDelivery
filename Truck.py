from ReadDistances import ReadDistances
from ReadPackages import Package
import datetime


class Truck:

    def __init__(self, truck_number, start_time):
        self.packages = []
        self.truck_number = truck_number
        self.start_time = start_time
        self.speed = 18
        self.location = "HUB"
        self.distance_traveled = 0
        self.rd = ReadDistances()

    def load_truck(self, packs):
        """
        A truck can hold 16 packages, this function tells the truck object which packages will be associated
        with this instance of truck
        :param packs:  array of packages
        """
        for p in packs:
            self.packages.append(p)

    def add_to_truck(self, package):
        """
        Add one package to be loaded on to the truck
        :param package:
        """
        self.packages.append(package)

    def update_location(self, new_location):
        """
        Trucks start at the hub and their location must be updated when they deliver a package
        :param new_location:
        """
        self.location = new_location

    def get_packages(self):
        """
        :return: all packages that are associated with the truck
        """
        return self.packages

    def deliver_packages(self):
        """
        This function delivers the packages on the truck
        """
        for p in self.packages:
            # distance_nextpackage: (distance traveled, next package to deliver)
            distance_nextpackage = self.rd.min_distance_from(self.location, self.packages)
            # update distance to reflect delivering a package
            self.distance_traveled += distance_nextpackage[0]
            # update location of truck to be the address of the last package delivered
            self.location = distance_nextpackage[1].get_address()
            self.update_time()
            distance_nextpackage[1].set_delivered(self.update_time())

        return self.distance_traveled

    def get_packages_at_time(self, time):
        """
        return all the packages with the status of their delivery at a given time
        if time < time truck start making delivery: all packages will be at hub
        if time > time truck start making delivery && time > time the package was delivered: package en route
        if time < time package was delivered: package delivered at xx:xx:xx
        :param time: what time the user would like to know the status of packages at
        :return: status of every package on the truck
        """
        packages_at_time = []
        for p in self.packages:
            p.reset_delivered()
            if time < self.start_time:
                p.set_at_hub()
                packages_at_time.append(p)
            elif p.get_delivery_time() <= time:
                packages_at_time.append(p)
            else:
                p.set_en_route()
                packages_at_time.append(p)
        return packages_at_time

    def get_package_at_time(self, time, package):
        """
        same as get_packages_at_time, but this function is used to retrieve info of a single package
        :param time:
        :param package:
        :return: package with appropriate delivery status
        """
        package.reset_delivered()
        if time < self.start_time:
            package.set_at_hub()
        elif package.get_delivery_time() <= time:
            return package
        else:
            package.set_en_route()
        return package

    def return_to_hub(self):
        """
        In this project there may be three trucks but only two drivers. this function is necessary because one driver
        must return to the hub to make deliveries on the truck and the distances must reflect that
        """
        self.distance_traveled += self.rd.get_distance(self.location, "HUB")
        self.location = "HUB"

    def get_distance(self):
        """
        return the distance traveled by the truck.
        :return:
        """
        return self.distance_traveled

    def update_time(self):
        """
        update the time associated with the truck as a function of the distance it has traveled.
        trucks travel at a constant speed of 18 miles per hour.
        :return: current_time
        """
        f = self.distance_traveled / 18
        hour = int(f)
        minute = int((f % 1) * 60)
        added_time = datetime.timedelta(hours=hour, minutes=minute, seconds=0)
        current_time = self.start_time + added_time
        return current_time
