import os, platform

try:
    print("Generating Wheel File")
    if platform.system() == 'Windows':
        os.system("python setup.py sdist bdist_wheel")
    else:
        os.system("python3 setup.py sdist bdist_wheel")
        
    print("Uploading to PyPi")
    os.system("twine upload dist/*")
except Exception as e:
    print(e)
else:
    print("Upload completed. Clean up the unneeded resources")