class Point:
  
  # dunder
  
  def __new__(cls, x, y):
    return cls(x, y)
  
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
  def __str__(self):
    return "Point(x={}, y={})".format(self.x, self.y)
  
  def __repr__(self):
    return "Point(x={}, y={})".format(self.x, self.y)
  
  def __eq__(self, other):
    return self.x == other.x and self.y == other.y
  
  def __ne__(self, other):
    return not self.__eq__(other)
    
  @classmethod
  def create_from_pair(cls, pair):
    'tuple -> Point'
    x = pair[0]
    y = pair[1]
    x, y = pair
    return Point(x, y)
  
  @classmethod
  def create_from_pair_static(cls, pair):
    'tuple -> Point'
    x = pair[0]
    y = pair[1]
    x, y = pair
    return Point(x, y)
  
  def __len__(self):
    return 2
  
  def __iter__(self):
    return self
  
  def __next__(self, *args):
    raise StopIteration
  
  def sum_coords(self):
    return self.x + self.y
  
  def __call__(self, z):
    return Point(self.x + z, self.y)

  def __add__(self, other):
    return Point(x=self.x + other.x, y=self.y + other.y)

  def __sub__(self, other):
    return Point(x=self.x - other.x, y=self.y - other.y)

  def __or__(self, other):
        return "Point x = "+self.x + "and point y =" + self.y


point = Point(x=3, y=3)
point2 = Point(x=2, y=2)
point3 = point+point2
point5 = point-point2
point4 = Point(x=5, y=5)
print point3
print point5
assert point4 == point3

# Homework
#point + point2
#point - point
#"point is awesome today" | point # this will print string with point information