from pathlib import Path

# Create path object
path = Path('data.txt')
print(path.exists())


# Check full file name / only name / show extenstion
path = Path('data.txt')
print(path.name)
print(path.stem)
print(path.suffix)




# Show Extenstion
path2 = Path('09 OOPs/81.create_student_class.py')
print(path2.name)
print(path2.stem)
print(path2.suffix)