from PyQt5 import QtWidgets, uic, QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.image as mpimg
import sys
import numpy as np
import math
import images
import icons


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi(r'F:\project3-2\sports\Final_Project\project_ui.ui', self)
        # Load the image
        self.img = mpimg.imread(r'Project_Rana\Images\area.png')

        # Create a FigureCanvas with your figure, and add it to your widget
        fig = Figure()
        fig.patch.set_alpha(0.0)
        self.canvas = FigureCanvas(fig)
        self.canvas.setStyleSheet("background:transparent;")
        layout = QtWidgets.QVBoxLayout(self.plotWidget)
        # Add the FigureCanvas to the layout
        layout.addWidget(self.canvas)
        # Get the axes from the figure, and plot your simulation
        self.ax = fig.add_subplot(111)

        # Make the axes background transparent
        self.ax.patch.set_alpha(0.0)

        # Set the plot limits
        self.ax.set_xlim(0, 170)  # Set x-limit
        self.ax.set_ylim(0, 133)  # Set y-limit

        # Adjust slider of the launching speed (m/s)
        self.horizontalSlider_launching_speed.setMinimum(5)
        self.horizontalSlider_launching_speed.setMaximum(40)
        self.horizontalSlider_launching_speed.setValue(30)
        self.horizontalSlider_launching_speed.valueChanged.connect(self.update_speed)   # Update speed

        # Adjust slider of the firing angle
        self.horizontalSlider_firing_angle.setMinimum(30)
        self.horizontalSlider_firing_angle.setMaximum(90)
        self.horizontalSlider_firing_angle.setValue(36)
        self.horizontalSlider_firing_angle.valueChanged.connect(self.update_angle)  # Update angle

        # Adjust slider of the motion display speed
        self.horizontalSlider_display_speed.setMinimum(1)
        self.horizontalSlider_display_speed.setMaximum(10)
        self.horizontalSlider_display_speed.setValue(5)
        self.horizontalSlider_display_speed.valueChanged.connect(self.update_motion_speed)

        # Default speed
        self.animation_speed = 5

        # Adjust play and restart button
        self.pushButton_play_pause.clicked.connect(self.play_pause)
        self.pushButton_restart.clicked.connect(self.restart)

        # Initial conditions
        self.v = 27  # initial speed (m/s)
        self.prev_v = self.v  # store the previous speed
        self.label_launching_speed.setText(f'{self.v}')
        self.theta = math.radians(36)  # launch angle (converted to radians)
        self.prev_theta = self.theta  # store the previous angle
        self.label_firing_angle.setText(f'{36}')
        self.g = 9.81  # acceleration due to gravity (m/s^2)

        # Initial position and velocity
        self.x, self.y = 0, 0  # start at origin
        self.vx = self.v * math.cos(self.theta)
        self.vy = self.v * math.sin(self.theta)
        
        # Maximum height
        self.max_height = 0

        # Time step (change as needed)
        self.dt = 0.1

        # Lists to store x and y values
        self.x_vals = []
        self.y_vals = []

        # Calculate the maximum distance using the range equation
        self.d_max = (self.v**2 * np.sin(2*self.theta)) / self.g

        # Create a timer for animation
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.draw_frame)
        self.timer.start(20)  # interval in milliseconds
        self.show()
        
    def play_pause(self):
        new_v = self.horizontalSlider_launching_speed.value()
        new_theta = math.radians(self.horizontalSlider_firing_angle.value())
        if self.timer.isActive():
            self.timer.stop()
        else:
            if new_v != self.prev_v or new_theta != self.prev_theta:
                self.restart()  # Reset the simulation with the new values
                self.prev_v = new_v  # update the previous speed
                self.prev_theta = new_theta  # update the previous angle
            else:
                self.timer.start(20)  # interval in milliseconds
        self.show()

    def restart(self):
        # Reset initial conditions
        self.x, self.y = 0, 0  # start at origin
        self.vx = self.v * math.cos(self.theta)
        self.vy = self.v * math.sin(self.theta)
        self.x_vals = []
        self.y_vals = []
        self.d_max = (self.v**2 * np.sin(2*self.theta)) / self.g
        
        self.max_height = 0

        # Start the timer
        self.timer.start(20)  # interval in milliseconds
        self.show()

    def draw_frame(self):
        # Modify timer interval based on animation speed
        timer_interval = int(1000 / self.animation_speed)
        self.timer.setInterval(timer_interval)
        # Update position and velocity
        self.x += self.vx * self.dt
        self.y += self.vy * self.dt  # subtract because Pygame's y-coordinates increase going down
        self.vy -= self.g * self.dt  # accelerate downwards due to gravity

        # Add current position to trajectory points
        self.x_vals.append(self.x)
        self.y_vals.append(self.y)

        # Update the distance, time and max. height labels
        self.label_throwing_distance.setText(f'{self.x:.2f} m')
        self.label_throwing_time.setText(f'{len(self.x_vals) * self.dt:.2f} s')
        # self.label_max_hight.setText(f'{self.y:.2f} m')
        
        # Update the maximum height
        if self.y > self.max_height:
            self.max_height = self.y
            self.label_max_height.setText(f'{self.max_height:.2f} m')

        # Clear the current plot
        self.ax.clear()

        # Set the background image
        self.ax.imshow(self.img, extent=[0, 170, 0, 133])

        # Draw the trajectory
        if len(self.x_vals) > 1:
            self.ax.plot(self.x_vals, self.y_vals, color='blue')

        # Draw the ball
        # self.ax.plot(self.x, self.y, 'ro')
        self.ax.plot(self.x, self.y, marker=(3, 1, math.degrees(self.theta) + 90), markersize=15, color='red')

        # Set the color, size, and weight of the title and labels
        self.ax.set_xlabel('Distance (m)', fontsize=14, fontweight='bold', color='white')
        self.ax.set_ylabel('Height (m)', fontsize=14, fontweight='bold', color='white')
        self.ax.set_title('Javelin Trajectory', fontsize=24, fontweight='bold', color='black')
        self.ax.tick_params(color='white', size=10, labelsize=13, labelcolor='white')
        # Show the grid
        self.ax.grid(True, linestyle='-', color='white', linewidth=0.5)

        # End simulation if ball hits the ground or reaches maximum distance
        if self.y < 0 or self.x > self.d_max:
            self.timer.stop()
        # Draw the plot
        self.canvas.draw()

    def update_speed(self, value):
        self.v = value
        self.label_launching_speed.setText(f'{self.v}')

    def update_angle(self, value):
        self.theta = math.radians(value)
        self.label_firing_angle.setText(f'{value}')

    def update_motion_speed(self, value):
        # Update animation speed based on slider value
        self.animation_speed = value


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()