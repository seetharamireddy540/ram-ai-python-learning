import os
import time


filedir = os.path.dirname(__file__)
print(f"filedir {filedir}")
filepath = os.path.join(os.path.dirname(__file__), 'graph.py')
print("...........")
print(filepath)
print("...........")
# with open(filepath, 'r') as f:
#     print(f.read())
    
    
if os.path.exists(filepath):
    print("file exists")
    size = os.path.getsize(filepath)
    print(f"file size {size} bytes")
    mod_time = os.path.getmtime(filepath)
    print(f"file last modified {mod_time}")
    print(f"Last modified: {time.ctime(mod_time)}")
