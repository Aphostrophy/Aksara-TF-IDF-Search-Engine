import os
from filtering import Cleaningkata

directory = r'C:\tubes\Algeo02-19079\src\backend\static'
multFiles = []
for filenames in os.listdir(directory):
    if filenames.endswith(".txt"):
        joinpath = os.path.join(directory, filenames)
        file = open(joinpath).read()
        multFiles.append(file)
    else:
        continue

for i in multFiles:
    print(i)
