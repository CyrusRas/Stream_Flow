import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np

with open('June-2021-Provo-River-Streamflow-Rates.csv', 'r') as f:
    lines = f.read().splitlines()[1:]

data = np.array([line.split(',') for line in lines])

x = data[:, 0].astype('datetime64[m]')
y_1 = data[:, 1].astype(float)
y_2 = data[:, 2].astype(float)
y_3 = data[:, 3].astype(float)
y_4 = data[:, 4].astype(float)
y_5 = data[:, 5].astype(float)

plt.figure(figsize=(8, 6))

plt.plot(x, y_1, color='purple', label='10163000')
plt.plot(x, y_2, color='teal', label='10155200')
plt.plot(x, y_3, color='green', label='10155500')
plt.plot(x, y_4, color='orange', label='10154200')
plt.plot(x, y_5, color='orangered', label='10155000')

plt.title('Provo River Streamflow Data (June 2021)')
plt.ylabel('Flowrate (cfs)')
plt.xlabel('Date')
plt.legend(title='Site Numbers', loc='upper right')
plt.grid(True, linestyle='-', alpha=0.5)

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
