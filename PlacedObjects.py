#--------------Object oriented part------------#
#Going to need to be able to control lists of these, transform those lists into four CDSs for display

class PlacedObject(object):

    def __init__(self,x_coord, y_coord):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.type = None
        self.shape = None

    # Setting up the position

    def get_x_coord(self):
        return self.x_coord

    def get_y_coord(self):
        return self.y_coord

    # Setting up the type

    def set_source(self):
        self.type = "Source"

    def set_reflector(self):
        self.type = "Reflector"

    def set_type(self,in_type):
        self.type = in_type

    def get_type(self):
        return self.type

    # Setting up the shape

    def set_shape(self, in_shape):
        self.shape = in_shape

    def get_shape(self):
        return self.shape

class RectangularObject(PlacedObject):

    def __init__(self,x_coord, y_coord, width, height):
        super(RectangularObject, self).__init__(x_coord, y_coord)
        self.width = width
        self.height = height
        self.set_shape("Rectangle")

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height


class CircularObject(PlacedObject):

    def __init__(self,x_coord, y_coord, radius):
        super(CircularObject, self).__init__(x_coord, y_coord)
        self.radius = radius
        self.set_shape("Circle")

    def get_radius(self):
        return self.radius

class PolygonalObject(PlacedObject):

    def __init__(self):
        pass



# General Functionality Test
test1 = PlacedObject(1,2)
test2 = RectangularObject(1,2,3,4)
test3 = CircularObject(1,2,3)

test1.set_type("Source")
test2.set_type("Reflector")

print "General Object"
print "shape: {}, type: {}, x_coord: {}, y_coord: {}".format(test1.get_shape(),test1.get_type(),test1.get_x_coord(),test1.get_y_coord())

print "Rectangle Object"
print "shape: {}, type: {}, x_coord: {}, y_coord: {}, width: {}, height: {}".format(test2.get_shape(),test2.get_type(),test2.get_x_coord(),test2.get_y_coord(),test2.get_width(),test2.get_height())

print "Circular Object"
print "shape: {}, type: {}, x_coord: {}, y_coord: {}, radius: {}".format(test3.get_shape(),test3.get_type(),test3.get_x_coord(),test3.get_y_coord(), test3.get_radius())
