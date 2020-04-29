import time

def transmissionrate(dev, direction, timestep):
    path = "/sys/class/net/{}/statistics/{}_bytes".format(dev, direction)
    f = open(path, "r")
    bytes_before = int(f.read())
    f.close()
    time.sleep(timestep)
    f = open(path, "r")
    bytes_after = int(f.read())
    f.close()
    return (bytes_after-bytes_before)/timestep

devname = "ens33"
timestep = 2 # in seconds
threshold = 80 #in bytes

while True:
    if (transmissionrate(devname, "rx", timestep)) > threshold:
       print("ALERT! High amount of data recieved!")
