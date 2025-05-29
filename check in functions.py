def multiply(x, y, z):
    print(x*y*z)


def print_list(first, second):
    for i in range(len(list1)):
        print(list1[i], list2[i])
        
def return_data(thing):
    return type(thing)

def main():
    list1 = ["computer", "charger", "pencil"]
    list2 = ["0", "1", "2"]
    multiply(4,3,7)
    print_list(list1, list2)
    print(return_data(False))
main()
