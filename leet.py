def check_weather_distribution_is_clockwise_or_anticlockwise(index_of_first_name,index_of_second_name):
    difference_in_indeces = index_of_first_name - index_of_second_name
    if (difference_in_indeces < 0):
        return "Clockwise"
    else:
        return "AntiClockwise"
    
def check_index_value(index):
    if index == len(no_of_people)-1:
        index = 0
        return index
    else:
        index += 1
        return index
        
    
def upload_data_in_dictionary(to_store_the_count_of_chocolates,no_of_people,no_of_chocolates,index):
    no_of_chocolates = no_of_chocolates - len(to_store_the_count_of_chocolates)
    for i in range(no_of_chocolates):
        access_name = no_of_people[index]
        if access_name in to_store_the_count_of_chocolates:
            to_store_the_count_of_chocolates[access_name] += 1 
            index = check_index_value(index)
        else:
            to_store_the_count_of_chocolates[access_name] = 1
            index = check_index_value(index)
    for (key,value) in to_store_the_count_of_chocolates.items():
        output_format = "{}-{}".format(key,value)
        print(output_format)
    print(no_of_people[index])

def distribute_the_chocolates(no_of_chocolates,no_of_people,first_name,second_name,second_name_index):
    to_store_the_count_of_chocolates = {}
    to_store_the_count_of_chocolates[first_name] = 1 
    to_store_the_count_of_chocolates[second_name] = 1
    index = 0
    if second_name_index == len(no_of_people)-1:
        index = 0
        data_result = upload_data_in_dictionary(to_store_the_count_of_chocolates,no_of_people,no_of_chocolates,index)
    else:
        index = second_name_index
        data_result = upload_data_in_dictionary(to_store_the_count_of_chocolates,no_of_people,no_of_chocolates,index)
    return data_result
                

no_of_people = ["jane","jack","dane","sane","danny"]
no_of_chocolates = 5
first_name = "jack"
second_name = "sane"
first_name_index = no_of_people.index(first_name)
second_name_index = no_of_people.index(second_name)
rotation_result = check_weather_distribution_is_clockwise_or_anticlockwise(first_name_index,second_name_index)
print(rotation_result)
result = distribute_the_chocolates(no_of_chocolates,no_of_people,first_name,second_name,second_name_index)


