import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter, FuncFormatter

# Load the CSV file
file_path = 'C:/Users/ipek/Documents/youtubeguncel12.csv'
data = pd.read_csv(file_path)

# Convert 'Time' from seconds to timedelta
data['Time'] = pd.to_timedelta(data['Time'], unit='s')

# Set 'Time' as the index
data.set_index('Time', inplace=True)

# Resample the data to 1-second intervals, summing the packet counts
data_1s = data['No.'].resample('1S').count()

# Plot the results
plt.figure(figsize=(12, 6))
plt.plot(data_1s.index, data_1s.values, marker='o', linestyle='-')
plt.xlabel('Time (seconds)')
plt.ylabel('Packet Count')
plt.title('Packet Count in 1-Second Intervals')
plt.grid(True)

# Disable scientific notation on the y-axis
ax = plt.gca()
ax.yaxis.set_major_formatter(ScalarFormatter(useOffset=False))
ax.ticklabel_format(style='plain', axis='y')

# Alternatively, force plain formatting by using FuncFormatter
def plain_formatter(x, pos):
    return '%1.0f' % x

ax.yaxis.set_major_formatter(FuncFormatter(plain_formatter))

plt.show()
