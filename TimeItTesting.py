# the timeit module helps with tracking code execution and program duration
# it is helpful for code optimization and performance
import timeit


start_time = timeit.default_timer()
print('start_time: {}'.format(start_time))

# test code for analysis
for i in range(100_000_000):
    pass

# time calculation
end_time = timeit.default_timer()
print('end_time: {}'.format(end_time))
print('total_time: {}'.format(end_time - start_time))