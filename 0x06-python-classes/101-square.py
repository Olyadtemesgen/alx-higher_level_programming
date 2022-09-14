class Square:
    """
    it is working but i do not know why it is not happening
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    @property
    def position(self):
        return self.__position
    @position.setter
    def position(self, position):
        if len(position) != 2 or type(position) is not tuple \
            or not all(ints >= 0 for ints in position):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = position
    def area(self):
        return self.__position ** 2
    def my_print(self):
        if self.size == 0:
            print("")
        print(self.__size * " " + self.__position[0] * "#")
    def __repr__(self):
        if self.size == 0:
            return ""
        st = ""
        x = self.position[1]
        while x != 0:
            st += '\n'
            x -= 1
        for x in range(self.__size):
            st += self.position[0] * " " + self.size * "#"
            if x < self.__size - 1:
                st += '\n'
        return st
