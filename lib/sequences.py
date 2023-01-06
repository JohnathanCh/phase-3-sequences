import pdb
#!/usr/bin/env python3

def print_fibonacci(length):
    my_list = list(range(0,length))
    # pdb.set_trace()
    if (length == 0):
        print(my_list)
    else:
        new_list = []
        # print(my_list)
        for num in my_list:
            if (my_list.index(num) == 0 or my_list.index(num) == 1):
                new_list.append(num)
            else:
                # pdb.set_trace()
                first = new_list[num - 2]
                second = new_list[num - 1]
                final = first + second
                new_list.append(final)
                # pdb.set_trace()
                # new_list.append(0)
                # pdb.set_trace()

        print(new_list)
        
        

# [0,1,2,3,4]