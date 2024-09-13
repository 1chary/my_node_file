def get_the_amount_rain_water_stored(height,second_max_number,index_of_second_max_number):
    rain_water_count = 0
    if height[0] == 0:
        height.remove(0)
    length_of_array = len(height)
    for i in range(length_of_array):
        if i < length_of_array:
            current_value = height[i]
            if i != length_of_array-1:
                next_value = height[i+1]
                if current_value > next_value:
                    if next_value == 0:
                        find_index_of_zero = i+1
                        if find_index_of_zero < index_of_second_max_number:
                            rain_water_count += current_value
                        else:
                            rain_water_count += second_max_number
                    else:
                        rain_water_count += current_value - next_value
                else:
                    continue
            else:
                break
    print(rain_water_count)
            
height = [0,1,0,2,1,0,1,3,2,1,2,1]
sorted_list = sorted(height)
second_max_number = sorted_list[-2]
index_of_second_max_number = height.index(second_max_number)
get_the_amount_rain_water_stored(height,second_max_number,index_of_second_max_number)