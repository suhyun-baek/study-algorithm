def merge_the_tools(str_input_string, int_factor):
    # your code goes here
    int_input_string = len(str_input_string)
    int_count_subsegmnent = int_input_string // int_factor

    for index in range(int_count_subsegmnent):
        str_subsegment_string = str_input_string[index * int_factor : (index + 1) * int_factor]
        str_print = ""
        for index_02 in str_subsegment_string:
            if index_02 not in str_print:
                str_print += index_02
        print(str_print)



if __name__ == '__main__':
    # string, k = input(), int(input())
    string, k = "AABCAAADA", 3
    merge_the_tools(string, k)