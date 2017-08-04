class SpaceShip:
    def __init__(self, company, country, launch_time, ):
        self.country = country
        self.launch_time = launch_time
        self.company = company

    def description(self):
        return "We are {} from the {} and we are launching in {}".format(self.company, self.country, self.launch_time)

    def launch(self):
        if launch:
            print "We are ready for lift offf"
        else:
            print "We are experiencing technical difficulties"

NASA = SpaceShip("Nasa", "USA", "10 Seconds", True)
SpaceX = SpaceShip("SpaceX", "USA", "30 Seconds", False)

print NASA.description()
print SpaceX.description()
print NASA.launch()
print SpaceX.launch()
