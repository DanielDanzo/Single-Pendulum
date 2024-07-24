import pygame
import math
import sys


class Ball:
    def __init__(self, x_position, y_position, velocity, mass):
        self.x_position = x_position
        self.y_position = y_position
        self.velocity = velocity
        self.mass = mass

    def getPositions(self):
        return self.x_position, self.y_position

    def updatePositions(self, angle, r):
        self.x_position = (r*math.sin(angle)) + 300
        self.y_position = (r*math.cos(angle))





# Initialise the pygame
pygame.init()

# Necessary variables for the pygame visualisation
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("A simple Pendulum")


# Any colors that are required for rendering on the screen
background_color = (0, 0, 0)
wedge_color = (0, 255, 255)
wedge_size = 50
ball_color = ( 255, 255, 255)
ball_radius = 14
line_color = ( 255, 255, 255)
line_width = 2


# Declare any necessary variable needed
g = 9.81 # Gravity constant
angle_0 = (math.pi)/4  # Angle from origin
r = int(sys.argv[1])  # Length of the rod
v_0 = 0
ball = Ball((r * math.sin(angle_0)) + 300, (r * math.cos(angle_0)), 2, int(sys.argv[2])) # The ball on the pendulum




# The running loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(background_color)

    # Updates on the pendulum system
    v_0 = v_0 - ((g/r)*math.sin(angle_0))
    #v_0 = v_0*0.99  # -----UNCOMMENT------: If you want to make the pendulum stop at some point in time
    angle_0 = angle_0 + v_0
    
    
    ball.updatePositions(angle_0, r) # The ball on the pendulum

    #print(f"New position: {ball.getPositions()}")

    # Draw the wedge
    pygame.draw.line( screen, wedge_color, (width//2 - 60, 0), (width//2+60, 0), wedge_size)

    # Draw rope leading to ball
    pygame.draw.line( screen, line_color, ( width//2, wedge_size//2), ball.getPositions(), line_width )

    # Draw the ball
    pygame.draw.circle( screen, (0, 0, 255),  ball.getPositions(), ball_radius + 3)
    pygame.draw.circle( screen, ball_color,  ball.getPositions(), ball_radius)

    

    # Updates the display of the screen
    pygame.display.flip()
    pygame.time.Clock().tick(20)




#Free anything that needs to be freed
pygame.quit()
sys.exit()