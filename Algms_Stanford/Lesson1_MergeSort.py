import time

input_str = list('843184312348129')

# input_str = list('8431')

def mergesort(str_arg = input_str):
    
    ## length of input string
    n = len(str_arg)
    
    if n < 2:
        ## exit if n is a one-element list
        return str_arg
    else:
        n_left = n//2
        arr_left  = str_arg[:(n_left)]
        arr_right = str_arg[(n_left):]
        
        # print(arr_left, arr_right)
        
        ## if n is greater than 1, mergesort will run recursively to return the sorted list. 
        arr_left  = mergesort(arr_left)
        arr_right = mergesort(arr_right)
        
        ## Initiation of left array index and right array index
        i,j = 0, 0
        
        ## output array
        result = []
    
        for k in range(0,n):
            # print(k)
            while ((i < len(arr_left)) and (j < len(arr_right))):
                if (arr_left[i] <= arr_right[j]):
                    # print(arr_left)
                    result.append(arr_left[i]) 
                    i += 1
                else:
                    # print(arr_right)
                    result.append(arr_right[j])
                    j += 1
            
            ## if we have run out of arr_right:        
            while (i < len(arr_left)):
                    result.append(arr_left[i]) 
                    i += 1
            
            ## if we have run out of arr_left:
            while (j < len(arr_right)):
                    result.append(arr_right[j])
                    j += 1

        # print(result)
        return(result)

tic = time.time()
print(mergesort())
toc = time.time()

print(toc - tic)  

# if len(str) > 1, split into two 
