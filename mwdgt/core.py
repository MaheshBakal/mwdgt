# mwdgt/core.py

import os
import xarray as xr
import numpy as np
from datetime import datetime, timedelta

class MaheshWindDataGettingThing:
    def __init__(self, start_date, end_date, data_dir):
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.end_date = datetime.strptime(end_date, "%Y-%m-%d")
        self.data_dir = data_dir
        self.files = self._collect_files()

    def _collect_files(self):
        # Collect files based on date range
        files = []
        date = self.start_date
        while date <= self.end_date:
            fname = f"MERRA2_UV_{date.strftime('%Y%m%d')}.nc"
            full_path = os.path.join(self.data_dir, fname)
            if os.path.exists(full_path):
                files.append(full_path)
            date += timedelta(days=1)
        return files

    def getWind(self, locations):
        """
        Given a set of (lon, lat) coordinates, return the corresponding
        interpolated U and V wind component arrays.
        """
        # Just a placeholder: fill this in based on your actual wind interpolation logic
        U = np.zeros(len(locations))
        V = np.zeros(len(locations))
        return U, V
