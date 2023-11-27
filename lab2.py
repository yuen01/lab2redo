def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    input_str = input("Enter a list of temperatures separated by commas: ")
    temperatures = [float(temp) for temp in input_str.split(',')]
    return temperatures

def calc_average(temperature_list):
    if not temperature_list:
        return 0.0
    average = sum(temperature_list) / len(temperature_list)
    return average

def find_min_max(temperature_list):
    if not temperature_list:
        return [0.0, 0.0]
    min_temp = min(temperature_list)
    max_temp = max(temperature_list)
    return [min_temp, max_temp]

def sort_temperature(temperature_list):
    sorted_temps = sorted(temperature_list)
    return sorted_temps

def calc_median_temperature(temperature_list):
    sorted_temps = sorted(temperature_list)
    n = len(sorted_temps)
    if n % 2 == 0:
        median = (sorted_temps[n//2 - 1] + sorted_temps[n//2]) / 2
    else:
        median = sorted_temps[n//2]
    return median

def main():
    display_main_menu()
    temperatures = get_user_input()
    average = calc_average(temperatures)
    min_max = find_min_max(temperatures)
    sorted_temps = sort_temperature(temperatures)
    median = calc_median_temperature(temperatures)
    print("Temperatures:", temperatures)
    print("Average:", average)
    print("Min and Max:", min_max)
    print("Sorted Temperatures:", sorted_temps)
    print("Median Temperature:", median)

main()