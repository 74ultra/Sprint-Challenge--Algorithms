'''
PLANNING:
- Strategy
    - sort a list of unknown size without storing more than a single value at a time. 
    - use a modified cocktail sort (modified bubble sort) to move left to right in the list, then move right to left.
    - we are not permitted to know/use the length of the list or store more than a single value at a time, so this method accommodates that rule.
- PHASE I: initial sort using a while loop
    - move from first element using a while loop (left to right)
        - if the card held is smaller than the card at the index position being examined, swap the card
        - this will move the largest value to the end of the list
        - when 'can_move_right()' returns False, the loop is ended
    - move from last element using while loop (right to left)
        - if the card held is larger than the card at the index position being examined, swap the card
        - this will move the smallest value to the front of the list
        - when 'can_move_left()' returns False, the loop is ended
- PHASE II: Check to see if the list is sorted correctly
    - move through the list, picking up each item and comparing its value to the following one
    - In the case that a value is larger than a following one, the light is set to 'on', indicating that the while loop must continue

'''


class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"

    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"

    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        # light on is the condition for continuing loop
        self.set_light_on()
        while self.light_is_on():
            # turn light off initially
            self.set_light_off()
            self.swap_item()  # take first item

            # left to right
            while self.can_move_right():
                if self.compare_item() == -1:  # if held item is smaller than list item, swap
                    self.swap_item()
                self.move_right()
            # right to left
            while self.can_move_left():
                if self.compare_item() == 1:  # if held item is larger than list item, swap
                    self.swap_item()
                self.move_left()
            # check to see if list is sorted by comparing pairs of values
            while self.can_move_right():
                self.move_right()
                if self.compare_item() == 1:
                    # if list is not sorted, the light is set to 'on' and the loop will continue
                    self.set_light_on()
                self.move_left()
                self.swap_item()
                self.move_right()
                self.swap_item()
            self.swap_item()  # place last held item back in list
            # check to see if values were found out of order (is the light on?)
            # if the list is not completely sorted, the loop will continue so the robot needs to move back to the left side of the list
            if self.light_is_on():
                while self.can_move_left():
                    self.move_left()


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1,
         45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    o = [3, 10, 4, 7, 1, -1, 6, 8]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)
