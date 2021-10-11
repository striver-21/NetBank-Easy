def maxOnesIndex(arr,n):

     

    # for maximum number of 1 around a zero

    max_count = 0

 

    # for storing result 

    max_index =0 

 

    # index of previous zero

    prev_zero = -1 

 

    # index of previous to previous zero

    prev_prev_zero = -1

  

    # Traverse the input array

    for curr in range(n):

     

        # If current element is 0,

        # then calculate the difference

        # between curr and prev_prev_zero

        if (arr[curr] == 0):

         

            # Update result if count of

            # 1s around prev_zero is more

            if (curr - prev_prev_zero > max_count):

             

                max_count = curr - prev_prev_zero

                max_index = prev_zero

             

  

            # Update for next iteration

            prev_prev_zero = prev_zero

            prev_zero = curr

  

    # Check for the last encountered zero

    if (n-prev_prev_zero > max_count):

        max_index = prev_zero

  

    return max_index
