# Switch n should have DPID of n
import sys
import math

# Due to the way mininet works, switch numbering is done from left-most nodes to right-most.
# Thus there is a jump in switch number every two hosts of varying sizes. This function
# accounts for those jumps so that a correct host list is generated.
def jump_list(num_edges, depth):
    j_list = [1] * (num_edges/2)
    edges = num_edges
    jump = 1
    while edges != 2:
        edges /= 2
        j_list[edges-1] = depth - jump
        jump += 1
    return j_list

IP_ADDRESS = "10.0.0."

# Accepts: python gen_host_list.py [depth] > [target file]

# Depth of tree is equal to the number of switch layers. Also equal
# to the depth of the tree minus one.
# depth_of_tree = 4
depth_of_tree = int(sys.argv[1])

number_of_hosts = int(math.pow(2,depth_of_tree))
number_of_edge_switches = int(number_of_hosts/2)

if depth_of_tree == 1:
    print IP_ADDRESS + "1,1,1"
    print IP_ADDRESS + "2,1,2"
else:
    add_to_switch_num = jump_list(number_of_edge_switches, depth_of_tree)
    add_to_switch_num_index = 0

    print IP_ADDRESS + "1" + "," + str(depth_of_tree) + ",1"
    print IP_ADDRESS + "2" + "," + str(depth_of_tree) + ",2"
    switch_index = depth_of_tree
    for host_num in range(3, number_of_hosts+1, 2):
        switch_index += add_to_switch_num[add_to_switch_num_index]
        print IP_ADDRESS + str(host_num) + "," + str(switch_index) + ",1"
        print IP_ADDRESS + str(host_num+1) + "," + str(switch_index) + ",2"

        add_to_switch_num_index += 1
        if add_to_switch_num_index == len(add_to_switch_num):
            add_to_switch_num_index = 0