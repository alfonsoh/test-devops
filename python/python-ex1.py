import os
system_uptime = os.po ('uptime -p') .read()[:1]
print (system_uptime)