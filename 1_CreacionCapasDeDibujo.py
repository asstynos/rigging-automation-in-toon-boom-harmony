from Library.TimeSleepPrint import time_sleep
from Library.rigging import Rigging
from Puppet import puppet

if __name__ == '__main__':
    time_sleep(3)
    print("RIGGING")
    rigging = Rigging(puppet)
    rigging.main()
