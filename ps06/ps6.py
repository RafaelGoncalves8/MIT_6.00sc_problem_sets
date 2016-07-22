# Problem Set 6: Simulating robots
# Name:
# Collaborators:
# Time: 15:23 - 20:29 (~5h)

import math
import random

import ps6_visualize
import pylab

# === Provided classes

class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: float representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

# === Problems 1

class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        self.tiles = []
        self.width = width
        self.height = height
        for i in range(width):
            self.tiles.append([])
            for e in range(height):
                self.tiles[i].append(0) #dirty == 0

    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        x = int(pos[0])
        y = int(pos[1])
        self.tiles[x][y] = 1

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        return self.tiles[int(m)][int(n)] == 1
    
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return self.width*self.height

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        clean = 0
        for i in range(self.width):
            for e in range(self.height):
                if self.tiles[i][e] == 1:
                    clean += 1
        return clean

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        return (random.random()*self.width, random.random()*self.height)


    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        if pos[0] <= self.width and pos[0] >= 0:
            if pos[1] <= self.height and pos[1] >= 0:
                return True
        return False


class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.room = room
        self.speed = speed
        self.position = room.getRandomPosition()
        self.direction = random.randint(0, 360)

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.position

    
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.direction

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.position = position

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.direction = direction

    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        raise NotImplementedError


# === Problem 2
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current direction; when
    it hits a wall, it chooses a new direction randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        direction = math.radians(self.direction)
        ndirection = self.direction
        nposition = (self.position[0]+math.sin(direction), \
                self.position[1] + math.cos(direction))
        if not self.room.isPositionInRoom(nposition):
            nposition = self.position
            ndirection = random.random()*360
        self.position = nposition
        self.direction = ndirection
        if not self.room.isTileCleaned(self.position[0], self.position[1]):
            self.room.cleanTileAtPosition(self.position)


# === Problem 3

def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. Robot or
                RandomWalkRobot)
    """
    sumSteps = 0
    trials = num_trials
    while num_trials > 0:
        robots = []
        Room = RectangularRoom(width, height)
        # anim = ps6_visualize.RobotVisualization(num_robots, width, height)
        numSteps = 0
        for i in range(num_robots):
            robots.append(robot_type(Room, speed))
        while (float(Room.getNumCleanedTiles())/float(Room.getNumTiles())) < min_coverage:
            for e in range(num_robots):
                robots[e].updatePositionAndClean()
                # anim.update(Room, robots)
            numSteps += 1
        num_trials -= 1
        sumSteps += numSteps
        # anim.done()
        
    return sumSteps/trials


# avg = runSimulation(1, 1.0, 5, 5, 0.75, 3, StandardRobot)
# avg = runSimulation(3, 0.8, 10, 10, 0.5, 2, StandardRobot)
# avg = runSimulation(8, 1.0, 20, 15, 0.8, 5, StandardRobot)
# 

# === Problem 4
# 
# 1) How long does it take to clean 80% of a 20x20 room with each of 1-10 robots?
# 2) How long does it take two robots to clean 80% of rooms with dimensions 
#          20x20, 25x16, 40x10, 50x8, 80x5, and 100x4?



def showPlot1():
    """
    Produces a plot showing dependence of cleaning time on number of robots.
    """ 
    ans=[]
    for i in range(10):
        num = i+1
        ans.append(runSimulation(num, 1.0, 20, 20, 0.8, 50, StandardRobot))
    pylab.plot(range(1,11), ans)


    pylab.title("1-10 robots comparison in cleaning 80% of a 20x20 room")
    pylab.xlabel('number of robots')
    pylab.ylabel('numer of steps')
    pylab.grid(True)
    pylab.savefig("Plot1.png")
    pylab.show()
#showPlot1()


def showPlot2():
    """
    Produces a plot showing dependence of cleaning time on room shape.
    """
    ans = []
    ratio = []
    for i,j in zip((20, 25, 40, 50, 80, 100), (20, 16, 10, 8, 5, 4)):
        ratio.append(i/j)
        ans.append(runSimulation(2, 1.0, i, j, 0.8, 50, StandardRobot))
    pylab.plot(ratio, ans)

    pylab.title("Number of steps taken for 2 robots to clean 80% of a 400 units of area in various shapes")
    pylab.xlabel('ratio (widith/height)')
    pylab.ylabel('number of steps')
    pylab.grid(True)
    pylab.savefig("Plot2.png")
    pylab.show()

#showPlot2()


# === Problem 5

class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random after each time-step.
    """
    def updatePositionAndClean(self):
        direction = math.radians(self.direction)
        ndirection = random.random()*360
        nposition = (self.position[0]+math.sin(direction), \
                self.position[1] + math.cos(direction))
        if not self.room.isPositionInRoom(nposition):
            nposition = self.position
            ndirection = random.random()*360
        self.position = nposition
        self.direction = ndirection
        if not self.room.isTileCleaned(self.position[0], self.position[1]):
            self.room.cleanTileAtPosition(self.position)


# avg = runSimulation(4, 1.0, 20, 10, 0.8, 2, RandomWalkRobot)



# === Problem 6

# For the parameters tested below (cleaning 80% of a 20x20 square room),
# RandomWalkRobots take approximately twice as long to clean the same room as
# StandardRobots do.
def showPlot3():
    """
    Produces a plot comparing the two robot strategies.
    """
    ans = []
    ans1 = []
    x = range(10, 110, 10)
    for i in range (10):
        ans.append(runSimulation(1, 1.0, 10, i+1, 0.8, 50, RandomWalkRobot))
    pylab.plot(x, ans, '-r', label='RandomWalk Robot')

    for i in range (10):
        ans1.append(runSimulation(1, 1.0, 10, i+1, 0.8, 50, StandardRobot))
    pylab.plot(x, ans1, '-b', label='Standard Robot')


    pylab.legend(loc = 'upper left')
    pylab.title("Comparison of Standard vs RandomWalk robots")
    pylab.xlabel('area')
    pylab.ylabel('number of steps')
    pylab.grid(True)
    pylab.savefig("Plot3.png")
    pylab.show()
    
showPlot3()
