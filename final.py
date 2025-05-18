import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# constants
N = 3  # number of sides
rho = 1  # radius length
frames_per_k = 90  # 3 seconds at 30 fps, can be shortened to speed up the animation
total_frames = N * frames_per_k

# Function that calculates the β vector
def beta_vector(k, alpha, N):
    angle1 = 2 * np.pi * (k + 1) / N
    angle2 = 2 * np.pi * k / N
    sin2 = np.sin(alpha)**2
    cos2 = 1 - sin2

    x = np.cos(angle1) * sin2 + np.cos(angle2) * cos2
    y = np.sin(angle1) * sin2 + np.sin(angle2) * cos2
    return rho * x, rho * y

# Plot setup
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.grid(True)

quiver = ax.quiver(0, 0, 0, 0, angles='xy', scale_units='xy', scale=1, color='blue')
trajectory_line, = ax.plot([], [], 'r-', lw=1)  # red line representing the trajectory

# Lists to store the trajectory points
trajectory_x = []
trajectory_y = []

def update(frame):
    k = frame // frames_per_k
    alpha = (frame % frames_per_k) / frames_per_k * (np.pi / 2)

    x, y = beta_vector(k, alpha, N)

    # update vector
    quiver.set_UVC(x, y)

    # update trajectory
    trajectory_x.append(x)
    trajectory_y.append(y)
    trajectory_line.set_data(trajectory_x, trajectory_y)

    ax.set_title(f"k = {k}, α = {alpha:.2f} rad")
    return quiver, trajectory_line

# Animation
ani = FuncAnimation(fig, update, frames=total_frames, interval=1000/30, blit=False)

# Save .gif
#ani.save(f"polygon_{N}_sides.gif", writer=PillowWriter(fps=30))
plt.show()
