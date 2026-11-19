import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import csv


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
    plt.savefig("provo_streamflow.png", dpi=150, bbox_inches="tight")
    plt.show()


def summarize(dates, flows, sites):
    # Excel check for gauge 10163000: maximum = 131.0 cfs; average = 56.9523611111 cfs.
    print(f"{'Gauge':<12}{'Max (cfs)':>10}{'Date of max':>22}{'Min (cfs)':>12}{'Avg (cfs)':>12}")

    rows = []
    for gauge_index, site in enumerate(sites):
        gauge_flows = flows[:, gauge_index]
        maximum = np.max(gauge_flows)
        minimum = np.min(gauge_flows)
        average = np.mean(gauge_flows)
        maximum_index = np.argmax(gauge_flows)
        date_of_maximum = str(dates[maximum_index]).replace('T', ' ')

        print(
            f"{site:<12}"
            f"{maximum:10.1f}"
            f"{date_of_maximum:>22}"
            f"{minimum:12.1f}"
            f"{average:12.1f}"
        )
        rows.append([
            site,
            f"{maximum:.1f}",
            date_of_maximum,
            f"{minimum:.1f}",
            f"{average:.1f}",
        ])

    with open('streamflow_summary.csv', 'w', newline='') as summary_file:
        writer = csv.writer(summary_file)
        writer.writerow(['Gauge', 'Max (cfs)', 'Date of max', 'Min (cfs)', 'Avg (cfs)'])
        writer.writerows(rows)


def main():
    filename = 'June-2021-Provo-River-Streamflow-Rates.csv'
    x, flows = load_streamflow_data(filename)
    sites = ['10163000', '10155200', '10155500', '10154200', '10155000']
    summarize(x, flows, sites)

    threshold = float(input('Enter flow threshold (cfs): '))
    print(f'Hours above {threshold:g} cfs:')
    # Each reading above the threshold represents 15 minutes, or 0.25 hours.
    for gauge_index, site in enumerate(sites):
        hours_above_threshold = np.sum(flows[:, gauge_index] > threshold) * 0.25
        print(f'{site}: {hours_above_threshold:.2f} hours')

    plot_streamflow(x, flows)


if __name__ == '__main__':
    main()