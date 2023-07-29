import time
import random
def random_generator(size):
    return [random.randint(1, 99) for _ in range(size)]
array20 =random_generator(20)
array40 =random_generator(40)
array80 =random_generator(80)
array160 =random_generator(160)
array320=random_generator(320)
def merge_sort(array):
    if len(array) <= 1:
        return array
    middle = len(array) // 2
    left_half = array[:middle]
    right_half = array[middle:]
    
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    sorted_array = []
    i = j = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            sorted_array.append(left_half[i])
            i += 1
        else:
            sorted_array.append(right_half[j])
            j += 1
    sorted_array += left_half[i:]
    sorted_array += right_half[j:]

    return sorted_array
starttime20=time.time_ns()
sorted_array20 = merge_sort(array20)
endtime20=time.time_ns()
print("20",endtime20-starttime20)

starttime40=time.time_ns()
sorted_array40 = merge_sort(array40)
endtime40=time.time_ns()
print("40",endtime40-starttime40)

starttime80=time.time_ns()
sorted_array80 = merge_sort(array80)
endtime80=time.time_ns()
print("80",endtime80-starttime80)

starttime160=time.time_ns()
sorted_array160 = merge_sort(array160)
endtime160=time.time_ns()
print("160",endtime160-starttime160)

starttime320=time.time_ns()
sorted_array320 = merge_sort(array320)
endtime320=time.time_ns()
print("320",endtime320-starttime320)