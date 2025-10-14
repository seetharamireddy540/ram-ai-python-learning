from fileinput import filename
import os
import time


filedir= os.path.dirname(__file__);
print(f"filedir {filedir}")
filename = os.path.join(os.path.dirname(__file__), 'graph.py')
print("...........")
print(filename)
print("...........")
# with open(filename, 'r') as f:
#     print(f.read())
    
    
if os.path.exists(filename):
    print("file exists")
    size = os.path.getsize(filename)
    print(f"file size {size} bytes")
    mod_time = os.path.getmtime(filename)
    print(f"file last modified {mod_time}")
    print(f"Last modified: {time.ctime(mod_time)}")
