from mwdgt import MaheshWindDataGettingThing
from mwdgt.MaheshWindDataGettingThing import MaheshWindDataGettingThing  # ✅ USE this
import numpy as np

# Initialize your wind data tool with start/end dates and folder path
m = MaheshWindDataGettingThing(
    '2019-12-19',
    '2019-12-31',
    data_dir=r"C:\Downloads\Dissertation\New folder\Wind data"
)

# Example particle locations (lon, lat)
locations = np.array([
    [145.0, -36.5],
    [146.0, -37.0],
    [144.5, -35.5]
])

# Get wind values at these locations
u, v = m.getWind(locations)

print("U component:", u)
print("V component:", v)
