import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np


def load_streamflow_data(filename):
    with open(filename, 'r') as f:
        lines = f.read().splitlines()[1:]

    data = np.array([line.split(',') for line in lines])

    x = data[:, 0].astype('datetime64[m]')
    flows = data[:, 1:6].astype(float)
    return x, flows


def plot_streamflow(x, flows):
    plt.figure(figsize=(8, 6))

    series = [
        ('10163000', 'purple'),
        ('10155200', 'teal'),
        ('10155500', 'green'),
        ('10154200', 'orange'),
        ('10155000', 'orangered'),
    ]

    for gauge_index, (site, color) in enumerate(series):
        plt.plot(x, flows[:, gauge_index], color=color, label=site)

    plt.title('Provo River Streamflow Data (June 2021)')
    plt.ylabel('Flowrate (cfs)')
    plt.xlabel('Date')
    plt.legend(title='Site Numbers', loc='upper right')
    plt.grid(True, linestyle='-', alpha=0.5)

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()


def main():
    filename = 'June-2021-Provo-River-Streamflow-Rates.csv'
    x, flows = load_streamflow_data(filename)
    plot_streamflow(x, flows)


if __name__ == '__main__':
    main()
plt.savefig("provo_streamflow.png", dpi=150, bbox_inches="tight")