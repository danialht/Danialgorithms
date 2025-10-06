"""
An algorithm for the selection problem takes as input a collection of values, and a number 
k. It outputs the kth smallest of these values.

https://en.wikipedia.org/wiki/Selection_algorithm
"""

def selection(a, k):
    if len(a) == 0:
        raise ValueError("Length of the array can't be zero.")
    if len(a) <= 5:
        a = sorted(a)
        return a[k]
    medians = [selection(a[5*i:5*(i+1)], 2) for i in range(len(a)//5)]
    median_of_medians = selection(medians, len(medians)//2)
    greater_arr = [x for x in a if x > median_of_medians]
    greater = len(greater_arr)
    less_equal = len(a) - greater
    if less_equal >= k + 1:
        less_equal_arr = [x for x in a if x <= median_of_medians]
        return selection(less_equal_arr, k)
    else:
        return selection(greater_arr, k - less_equal)