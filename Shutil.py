import shutil
import os

source = '/Users/Owner/Desktop/A'

destination = '/Users/Owner/Desktop/B'
files = os.listdir(source)

for i in files:
    shutil.move(source+i, destination)
