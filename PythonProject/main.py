#Main method to run code for the qs method


"""
method to call something for if __name__ == '__main__':
    main()
    let's python execute code in file, whatever if written in this method will be called

"""
if __name__ == '__main__':
    main()
import quicksort
quicksort.main()



""" read file function that should read the file and use qs to implement"""
def readFile(quicksort):
    file = open(quicksort)
    quicksort.readline()
    for line in file:
        print(line)
        value = int(line)
        print("the value is ", value)
        ##
"""write file function that will write to quicksort
"""
def writeFile(quicksort):
    file = read(quicksort) #read from text from command line
    #put into main
    #read values from file
    #file from values
    #print results out 

    quicksort.close()
""" code to test """
array = [5,8,3,7,9]
n = len(array)
quicksort(array, 0,n-1)
print("sorted array is: ")
for i in range(n):
    print("%d" % array[i])
