import datetime


class Package:
    def __init__(self, id, address, city, state, zip, deadline, mass, notes):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.mass = mass
        self.notes = notes
        self.status = "At Hub"
        self.delivered = False
        self.delivery_time = datetime.timedelta(hours=0, minutes=0, seconds= 0)

    def get_id(self):
        """
        get the package id of a package
        :return: Package ID
        """
        return self.id

    def get_address(self):
        """
        Get address of package
        :return: Package's delivery address
        """
        return self.address

    def update_status(self, new_status):
        """
        Change the delivery status of a package
        :param new_status: delivery status
        """
        self.status = new_status

    def set_delivered(self, time):
        """
        Update the status of a package to it's delivered state with delivery time. Different from reset_delivered
        because this function is used to aid the function responsible for delivering packages.
        :param time: time of completed delivery
        """
        self.delivery_time = time
        self.delivered = True
        self.status = "Delivered at: " + str(self.delivery_time)

    def reset_delivered(self):
        """
        Update the status of a package to it's delivered state with delivery time
        :param time: time of completed delivery
        """
        self.status = "Delivered at: " + str(self.delivery_time)

    def set_at_hub(self):
        """
        Set the status to at hub. A package will be at the the hub if the time is before it's delivery truck starts
        delivering packages
        """
        self.status = "At Hub"

    def set_en_route(self):
        """
        Set the status to en route. A package will be en route if the time is after it's delivery truck starts
        delivering packages but before it's delivered time
        :return:
        """
        self.status = "En Route"

    def get_delivered(self):
        """
        get if package has been delivered or nor
        :return: boolean delivered, has this package been delivered in the delivering algorithm?
        """
        return self.delivered

    def get_delivery_time(self):
        """

        :return: time of delivery
        """
        return self.delivery_time

    def __repr__(self):
        """
        represent the package as a string
        :return: ex: "Package ID: xx Address: xxx Delivery Status: xxxx
        """
        return \
            "Package ID: " + str(self.id) + " Address: " + self.address + ", " + self.city + ", " \
            + self.state + ", " + self.zip + " Delivery Status: " + self.status