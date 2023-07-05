import time
a = time.time()
print(a)

b = time.ctime()
print(b)

new = time.localtime()
print(new)

print(new.tm_year)
print(new.tm_min)
print(new.tm_hour)

import os
import time
time.sleep(5)
os.chdir("peth")
os.rename("old","new")