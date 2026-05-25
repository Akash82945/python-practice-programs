from pathlib import Path


# Check file exist or not
path = Path("data.txt")
print(path.exists())



# Check another dictonary
target_path = r"C:\Users\LENOVO\Desktop\Practice set"
path = Path(target_path)
print(path.exists())