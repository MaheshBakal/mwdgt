# mwdgt/core.py

import os
import xarray as xr
import numpy as np
from datetime import datetime, timedelta
from scipy.interpolate import RegularGridInterpolator

class MaheshWindDataGettingThing:
    def __init__(self, start_date, end_date, data_dir):
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.end_date = datetime.strptime(end_date, "%Y-%m-%d")
        self.data_dir = data_dir
        self.files = self._collect_files()

    def _collect_files(self):
        files = []
        date = self.start_date
        while date <= self.end_date:
            fname = f"MERRA2_400.tavg3_3d_asm_Nv.{date.strftime('%Y%m%d')}.SUB.nc"
            full_path = os.path.join(self.data_dir, fname)
            if os.path.exists(full_path):
                files.append(full_path)
            else:
                print(f"File not found for {date.strftime('%Y-%m-%d')}")
            date += timedelta(days=1)
        return files

    def getWind(self, locations):
        """
        For each file (day), interpolate wind U and V at given locations.
        Returns U and V arrays of shape (n_days, n_locations)
        """
        u_list = []
        v_list = []

        for file in self.files:
            print("Processing file:", file)
            try:
                ds = xr.open_dataset(file)
                u_data = ds['U'].sel(lev=1).isel(time=0)
                v_data = ds['V'].sel(lev=1).isel(time=0)
                lons = ds['lon'].values
                lats = ds['lat'].values

                u_interp = RegularGridInterpolator((lats, lons), u_data.values)
                v_interp = RegularGridInterpolator((lats, lons), v_data.values)

                points = [(lat, lon) for lon, lat in locations]
                u_vals = u_interp(points)
                v_vals = v_interp(points)

                u_list.append(u_vals)
                v_list.append(v_vals)

            except Exception as e:
                print(f"Skipping {file} due to error: {e}")
                continue

        if not u_list:
            raise RuntimeError("No valid data found in any of the files.")

        U = np.vstack(u_list)  # shape: (n_days, n_locations)
        V = np.vstack(v_list)

        print("Shape of U:", U.shape)
        print("Shape of V:", V.shape)
        return U, V