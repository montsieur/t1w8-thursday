def function_a():
    print("Function A Started")
    function_b()
    print("Function A ended")

def function_b():
    print("Function B Started")
    function_c()
    print("Function B ended")

def function_c():
    print("Function C Started")
    # Intentional Error
    # result = 10 / 0
    # Debug it
    result = 10 / 1
    print("Function C ended")

# Call the inital function
function_a()