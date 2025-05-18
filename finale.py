import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# Costanti
N = 3  #n° lati
rho = 1 #lunghezza raggio
frames_per_k = 90  # 3 secondi a 30 fps, la si puo accorcercare per velocizzare la costruzione
total_frames = N * frames_per_k

# Funzione che calcola il vettore β
def beta_vector(k, alpha, N):
    angle1 = 2 * np.pi * (k + 1) / N
    angle2 = 2 * np.pi * k / N
    sin2 = np.sin(alpha)**2
    cos2 = 1 - sin2

    x = np.cos(angle1) * sin2 + np.cos(angle2) * cos2
    y = np.sin(angle1) * sin2 + np.sin(angle2) * cos2
    return rho * x, rho * y

# Setup grafico
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.grid(True)

quiver = ax.quiver(0, 0, 0, 0, angles='xy', scale_units='xy', scale=1, color='blue')
trajectory_line, = ax.plot([], [], 'r-', lw=1)  # linea rossa della traiettoria

# Lista per salvare la traiettoria
trajectory_x = []
trajectory_y = []

def update(frame):
    k = frame // frames_per_k
    alpha = (frame % frames_per_k) / frames_per_k * (np.pi / 2)

    x, y = beta_vector(k, alpha, N)

    # aggiorna la freccia
    quiver.set_UVC(x, y)

    # aggiorna la traiettoria
    trajectory_x.append(x)
    trajectory_y.append(y)
    trajectory_line.set_data(trajectory_x, trajectory_y)

    ax.set_title(f"k = {k}, α = {alpha:.2f} rad")
    return quiver, trajectory_line

# Animazione
ani = FuncAnimation(fig, update, frames=total_frames, interval=1000/30, blit=False)

# Salva .gif
ani.save(f"poligono_{N}_lati.gif", writer=PillowWriter(fps=30))

plt.show()
