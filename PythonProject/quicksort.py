#This code here is for qs
#Will have qs, partition, and swap
#Author: Liwei Meng
#iteration 1: implementing quicksort
#iteration 2: counting the iterations
#iteration #3: randomize qs

"""quicksort method
array = array, p = first element, r = last element
"""
def quicksort(array, p, r):
    count = 0 #implementing count
    if (p < r): #if first element less than last
        q = partition (array, p, r) #partition with q
        count += quicksort(array, p, q-1) #qs method(array, first element, partition-1 which is last element)
        count += quicksort(array, q+1, r) #qs method(array, partition+1 which is first plus one, last element )
        return count


"""randomizing the quicksort with a random partition
"""
def randompartition(array, p,r):
    randompivot = random.randrange(p,r) #generating random numb between starting index/ending index of array

    array[p], array[randompivot] = array[randompivot], array [p] # swapping starting elements of array and pivot

    return partition (array, p, r)


"""partion method, rearranges the subarray in place
"""
def partition(array, p, r):
    count = 0 #implementing count
    x = array[r] #x is the last element of r
    i = p - 1 #i is first element - 1
    for j in range(p,r):
        count += 1
        if array[j] <= x:
            i = i+1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[r] = array [r], array [i+1]
    return (i+1), count


""" count method to count iteration that goes through quicksort
"""
count = quicksort(x)
print (i, count)
