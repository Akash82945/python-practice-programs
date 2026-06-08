import numpy as np


# Modify the original data with slicing
# original = np.array([1,2,3,4,5])
# my_view = original[:3]
# my_view[0] = 99
# print(f"Original Data : {original}")
# print(f"My view : {my_view}")




# Modify the data but not affect the origin value using .copy()
# original = [1,2,3,4,5]
# my_view = original[:3].copy()
# my_view[0] = 99
# print(f"Original Data : {original}")
# print(f"My view : {my_view}")





# Sensor Calibrations
calibrations = np.array([10.5, 20.2, 30.8, 40.1])
safe_calibrations = calibrations[:3].copy()
safe_calibrations[0] = 0
print(f"Original data : {calibrations}")
print(f"Copy My view : {safe_calibrations}")