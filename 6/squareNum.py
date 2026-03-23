# squre num = root * root = original num
# runs in O(1) time complexity, as it performs a constant number of operations regardless of the input size.
def is_squre_num(num):
    if num <0:
        return False
    root =  int(num** 0.5)
    if (root*root == num):
        return True
    else:
        return False



try:
    user_input = input("enter a number to check: ")
    num = int(user_input)
    if (is_squre_num(num)):
        print(f"{user_input} is a squre number")
    else:
        print(f"{user_input} is not a squre number")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
