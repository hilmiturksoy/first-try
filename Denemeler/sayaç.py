#Zamanlayıcı saniye bazında geri sayıyor

import time


start_time=time.time()
zaman =int(input("please enter time: "))
time.sleep(zaman)
end_time=time.time()
elapsed_time=end_time-start_time
print(elapsed_time)