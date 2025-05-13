"""
Author : Samarth Pandya
ASTR 340 GW
Imports: tkinter, matplotlib and numpy
Inputs: User input for M31 or milky Way
Outputs: Three figures -
1) Rotation curves (velocity vs radius)
2) Enclosed mass vs radius
3) Pie chart depicting baryonic mass vs dark matter mass
"""


import tkinter as tk
from tkinter import simpledialog
import matplotlib.pyplot as plt
import numpy as np

# Simulated  datasets (based on values from the spreadsheet- derived from Foothill Simulations)
galaxy_data = {
    "M31": {
        "radius_kpc": np.linspace(0.1, 40, 100),
        "velocity_kms": np.concatenate([
            np.linspace(0, 230, 30),
            np.full(70, 230)
        ]),
        "mass_enclosed": lambda r: 5e10 * np.log1p(r)
    },
    "Milky Way": {
        "radius_kpc": np.linspace(0.1, 30, 100),
        "velocity_kms": np.concatenate([
            np.linspace(0, 220, 30),
            np.full(70, 220)
        ]),
        "mass_enclosed": lambda r: 4e10 * np.log1p(r)
    }
}

# Cosmological parameters (Planck 2018) 
OMEGA_DM = 0.308
OMEGA_BARYON = 0.048

def plot_galaxy(galaxy):
    if galaxy not in galaxy_data:
        print("Galaxy not recognized.")
        return

    data = galaxy_data[galaxy]
    r = data["radius_kpc"]
    v = data["velocity_kms"]
    mass = data["mass_enclosed"](r)

    fig, axs = plt.subplots(1, 3, figsize=(18, 5))
    
    # Velocity vs Radius
    axs[0].plot(r, v, label="Observed Rotation Curve", color='blue')
    axs[0].set_title(f"{galaxy} Rotation Curve")
    axs[0].set_xlabel("Radius (kpc)")
    axs[0].set_ylabel("Orbital Velocity (km/s)")
    
    # Mass Enclosed vs Radius (logarithmic scale)
    axs[1].plot(r, mass, label="Mass Enclosed", color='green')
    axs[1].set_title(f"{galaxy} Mass Enclosed vs Radius")
    axs[1].set_xlabel("Radius (kpc)")
    axs[1].set_ylabel("Mass (solar masses)")
    axs[1].set_yscale("log")
    
    # Pie Chart of Matter Composition
    axs[2].pie(
        [OMEGA_DM, OMEGA_BARYON],
        labels=["Dark Matter", "Luminous Matter"],
        autopct="%1.1f%%",
        colors=["gray", "orange"]
    )
    axs[2].set_title("Matter Composition (Cosmological)")

    plt.tight_layout()
    plt.show()

# Tkinter GUI for input
root = tk.Tk()
root.withdraw()  # Hide main window
galaxy_choice = simpledialog.askstring("Galaxy Selection", "Enter galaxy (M31 or Milky Way):")
if galaxy_choice:
    galaxy_choice = galaxy_choice.strip()
    plot_galaxy(galaxy_choice)
