if __name__=="__main__":
    int_input_data = int(input())

    if (int_input_data % 2) == 1:
        print("Weird")
    elif int_input_data >= 2 and int_input_data <= 5:
        print("Not Weird")
    elif int_input_data >= 6 and int_input_data <= 20:
        print("Weird")
    elif int_input_data > 20:
        print("Not Weird")