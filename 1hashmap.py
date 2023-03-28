# Open the two files for reading
import time
with open('L2.txt', 'r') as sravan, open('L3.txt', 'r') as f2:
    start_time = time.time()
    # Read the content of both files into two separate lists
    list1 = sravan.readlines()
    list2 = f2.readlines()
    hash_map = {}
    for item in list1:
        hash_map[item] = True
    for item2 in list2:
        hash_map[item2] = True
        if item2 not in hash_map:
            hash_map[item2] = True

            print(hash_map)

    with open("L7.txt", "w") as f5:
        for i in hash_map:
            f5.write(str(i) + '\n')
            end_time = time.time()
            print(end_time - start_time)




