#Done: practice creating a Function, calling the function, and passing a variable to the function.

def my_function(my_list = [1, 2, 3, 4, 5]):
    pass

#DONE: set an Optional Argument List5 for the function

    #DONE: Loop through the Arguement List
    
    # DONE: Using the Library datetime, print out the current date and time
    
    import datetime
    
    now = datetime.datetime.now()
    print(now)
    
    
    #DONE: Using the library datetime, override the existing date
    
    new_date = datetime.date(1996, 12, 11)
    print(new_date)
    
    #TODO: Using the time module, print out the current time
    
    import time
    time_now = time.time()
    print(time_now)

# convert what the time gives you and convert it to be readable 
    
    #DONE: Using the time module, pause the script for 5 seconds
    
    time.sleep(5)
    print('Did I sleep for 5 seconds')
    
    #DONE: Using the OS module, ping the localhost 2 times
    
    import os
    
    result = os.system{'ping localhost -c 2'}
    
    if __name__ == "__main__":
        my_variable = [1, 2, 3, 4, 5]
        