str1 = "abcd"
str2 = "a"
if str2 in str1:
    print True
else:
    print False

import time

a = time.time()
print a

b = time.localtime(a)
print b

c = time.asctime(b)
print c

print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())