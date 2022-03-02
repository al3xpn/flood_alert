import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import numpy as np


def plot_water_levels(stations, dates, levels):

    # Plot
    plt.plot(dates, levels)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(stations.name)

    plt.plot(dates, np.full(len(dates), stations.typical_range[0]).tolist(), label = "typical low level")
    plt.plot(dates, np.full(len(dates), stations.typical_range[1]).tolist(), label = "typical high level")


    plt.show()

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    
    