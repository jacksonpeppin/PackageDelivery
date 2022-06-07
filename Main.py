"""
Jackson Peppin
Student ID: #001338239
"""
import sys

from ReadPackages import ReadPackages
from ReadDistances import ReadDistances
from datetime import datetime, timedelta

from Truck import Truck


def find_package_on_truck(package, trucks):
    """
    This function finds the truck object with the desired package associated with it
    :param package: package you want to find the truck associated with
    :param trucks: List of all trucks with all packages spread across the trucks
    :return: truck with the package on it
    """
    for t in trucks:
        packs = t.get_packages()
        for p in packs:
            if p == package:
                return t
    return t


class Main:

    d = ReadDistances()
    rp = ReadPackages()
    packages = rp.get_packages()

    # initialize trucks with the time they will start making deliveries
    truck_one = Truck(1, timedelta(hours=8, minutes=0, seconds=0))
    truck_two = Truck(2, timedelta(hours=9, minutes=5, seconds=0))
    truck_three = Truck(3, timedelta(hours=10, minutes=2, seconds=0))

    truck_one_packages = [packages.get(13), packages.get(14), packages.get(15), packages.get(16), packages.get(19),
                          packages.get(20), packages.get(1), packages.get(25), packages.get(29), packages.get(30),
                          packages.get(31), packages.get(34), packages.get(32), packages.get(40), packages.get(26),
                          packages.get(21)]

    truck_two_packages = [packages.get(3), packages.get(36), packages.get(38), packages.get(6), packages.get(37),
                          packages.get(2), packages.get(4), packages.get(7), ]

    truck_three_packages = [packages.get(9), packages.get(8), packages.get(10), packages.get(11), packages.get(12),
                            packages.get(17), packages.get(18), packages.get(22), packages.get(23), packages.get(24),
                            packages.get(27), packages.get(28), packages.get(33), packages.get(35), packages.get(39),
                            packages.get(5), ]

    # put packages on trucks 1, 2 and 3
    truck_one.load_truck(truck_one_packages)
    truck_two.load_truck(truck_two_packages)
    truck_three.load_truck(truck_three_packages)
    # deliver packages on trucks 1, 2, return the driver of truck 2 back to the hub, then deliver the packages on 3
    truck_one.deliver_packages()
    truck_one.return_to_hub()
    truck_two.deliver_packages()
    truck_three.deliver_packages()
    trucks = [truck_one, truck_two, truck_three]

    print('_____________________')
    print('WGUPS Routing Program')
    print('_____________________')

    total_distance = truck_one.get_distance() + truck_two.get_distance() + truck_three.get_distance()
    print('Total distance traveled: ' + str(total_distance))

    user_input = raw_input("""
    Please select an option below to begin
    1. Get information of all packages at selected time.
    2. Get information of one package at selected time.
    3. Quit program.
    """)
    if user_input == '1':
        try:
            time_input = raw_input("""
    Please enter a time (Ex: 00:00:00 - 23:59:59):
            """)
            t = datetime.strptime(time_input, "%H:%M:%S")
            time = timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)
            for t in trucks:
                packs = t.get_packages_at_time(time)
            rp.print_packages()
        except ValueError:
            print("Please enter a valid time.")
    elif user_input == '2':
        try:
            package_input = input("""
    Enter package ID of package you would like to track:
            """)
            package = packages.get(package_input)

            time_input = raw_input("""
    Please enter a time (Ex: 00:00:00 - 23:59:59):
                        """)
            t = datetime.strptime(time_input, "%H:%M:%S")
            time = timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)
            truck_with_package = find_package_on_truck(package, trucks)
            print(truck_with_package.get_package_at_time(time, package))
        except ValueError:
            print("Please enter a valid time.")
        except AttributeError:
            print("Please enter a valid package ID.")
    elif user_input == '3':
        sys.exit()
    else:
        print('Please enter 1, 2, or 3.')

