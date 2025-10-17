import numpy as np
import matplotlib.pyplot as plt

# This code is used to analyse the gyrate.xvg file generated after the analysis of GROMACS trajectory file

plt.style.use('ggplot') # using ggplot style since its my favourite

# Filename
filename = 'gyrate.xvg'

# Lists to store data
time = []
rg = []
rg_x = []
rg_y = []
rg_z = []

with open(filename, 'r') as f:
    for line in f:
        # to skip '#' and '@' that are not useful for our analysis
        if line.startswith('#') or line.startswith('@'):
            continue

        data = line.split()
        print(data)
        if len(data) == 5:
            time.append(float(data[0]))
            rg.append(float(data[1]))
            rg_x.append(float(data[2]))
            rg_y.append(float(data[3]))
            rg_z.append(float(data[4]))
        
# Converting to numpy arrays
time = np.array(time)
rg = np.array(rg)
rg_x = np.array(rg_x)
rg_y = np.array(rg_y)
rg_z = np.array(rg_z)

print(f"Time range: {time[0]:.2f} - {time[-1]:.2f} ps")
print("\nRadius of Gyration Overview:")
print(f"Mean rg = {np.mean(rg):.4f}")
print(f"Std Dev = {np.std(rg):.4f}")
print(f"Min = {np.min(rg):.4f}")
print(f"Max = {np.max(rg):.4f}")

# Plotting
font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 14,
        }

plt.figure(figsize=(12,8))

plt.plot(time, rg, label='Rg', linewidth=1.5)
plt.plot(time, rg_x, label='RgX')
plt.plot(time, rg_y, label='RgY')
plt.plot(time, rg_z, label='RgZ')

plt.xlabel('Time (ps)', fontsize=14, fontdict=font)
plt.ylabel('Radius of Gyration (nm)', fontsize=14, fontdict=font)
plt.legend(loc='best', fontsize=12)
plt.title("Radius of Gyration of 3FYR for 1ns", fontweight='bold')
plt.grid(True)
plt.xticks(ticks=[x for x in range(0, 1001, 50)])
plt.tight_layout()

# Saving Figure

plt.savefig('gyration_analysis.png', dpi=300, bbox_inches='tight')

# Show the figure
plt.show()

# Note: Always write plt.show() after saving the figure. If you do so before, the saved image will be blank