
print("before import")
import math

print("before function_a")
def function_a():
    print("Function A")                                 

print("before function_b")
def function_b():
    print("Function B {}".format(math.sqrt(100)))       
print("before __name__ guard")


function_a()
function_b()


