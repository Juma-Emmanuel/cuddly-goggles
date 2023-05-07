import time
from datetime import datetime
import random
def random_generator(size):
    return [random.randint(1, 99) for _ in range(size)]
array20 =random_generator(20)
array40 =random_generator(40)
array80 =random_generator(80)
array160 =random_generator(160)
array320=random_generator(320)


def bubble_sort(array):
    n = len(array)
    
    
    for i in range(n):
              
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array
starttime20=time.time_ns()
sorted_array20 = bubble_sort(array20)
endtime20=time.time_ns()
print("20",endtime20-starttime20)

starttime40=time.time_ns()
sorted_array40 = bubble_sort(array40)
endtime40=time.time_ns()
print("40",endtime40-starttime40)

starttime80=time.time_ns()
sorted_array80 = bubble_sort(array80)
endtime80=time.time_ns()
print("80",endtime80-starttime80)

starttime160=time.time_ns()
sorted_array160 = bubble_sort(array160)
endtime160=time.time_ns()
print("160",endtime160-starttime160)

starttime320=time.time_ns()
sorted_array320 = bubble_sort(array320)
endtime320=time.time_ns()
print("320",endtime320-starttime320)
