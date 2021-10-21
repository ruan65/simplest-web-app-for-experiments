import os
for i in range(4):
    os.system(f"python -m http.server 800{i} &")

