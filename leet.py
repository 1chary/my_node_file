dictionary_to_store_start_values = {}
dungeon = [[0]]
length_of_dungeon = len(dungeon)


def calculate_the_start_and_final_value(number,row_length, column_length,final_value):
    delta_value = final_value - number
    start_value = max(1,delta_value)
    dictionary_to_store_start_values[row_length,column_length] = start_value


for i in range(1,length_of_dungeon+1):
    row_access_number = length_of_dungeon - i
    access_row = dungeon[row_access_number]
    column_length = len(access_row)
    for j in range(1,column_length+1): 
        reverse_the_row_numbers = column_length - j 
        value_from_dungeon = dungeon[row_access_number][reverse_the_row_numbers]
        if (row_access_number == length_of_dungeon-1 and column_length - j == column_length-1):
            final_value = 1
            calculate_the_start_and_final_value(value_from_dungeon,row_access_number,reverse_the_row_numbers,final_value)
        elif (row_access_number == length_of_dungeon - 1):
            value_from_dungeon = dungeon[row_access_number][reverse_the_row_numbers]
            add_one_access_the_final_value_from_dict = reverse_the_row_numbers + 1
            final_value = dictionary_to_store_start_values[row_access_number,add_one_access_the_final_value_from_dict]
            calculate_the_start_and_final_value(value_from_dungeon,row_access_number,reverse_the_row_numbers,final_value)
        else:
            if (reverse_the_row_numbers == column_length - 1):
                value_from_dungeon = dungeon[row_access_number][reverse_the_row_numbers]
                access_the_value_from_next_row_index = row_access_number + 1
                get_the_next_row_start_value_from_storage = dictionary_to_store_start_values[access_the_value_from_next_row_index,reverse_the_row_numbers]
                calculate_the_start_and_final_value(value_from_dungeon,row_access_number,reverse_the_row_numbers,get_the_next_row_start_value_from_storage)
            else:
                access_the_value_from_next_row_index = row_access_number + 1
                access_the_value_from_next_column_index = reverse_the_row_numbers + 1
                get_the_row_value = dictionary_to_store_start_values[access_the_value_from_next_row_index,reverse_the_row_numbers]
                get_the_column_value = dictionary_to_store_start_values[row_access_number,access_the_value_from_next_column_index]
                filter_by_minimum = min(get_the_column_value,get_the_row_value)
                value_from_dungeon = dungeon[row_access_number][reverse_the_row_numbers]
                calculate_the_start_and_final_value(value_from_dungeon,row_access_number,reverse_the_row_numbers,filter_by_minimum)
                

print(dictionary_to_store_start_values[0,0]) 

