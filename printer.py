sep_map = [
[' '],
[' '],
['#'],
[' '],
['#'],
[' '],
[' ']
]

zero_map = [
[' ','#','#','#',' '],
['#',' ',' ',' ','#'],
['#',' ',' ',' ','#'],
['#',' ',' ',' ','#'],
['#',' ',' ',' ','#'],
['#',' ',' ',' ','#'],
[' ','#','#','#',' ']
]

one_map = [
[' ','#',' '],
['#','#',' '],
[' ','#',' '],
[' ','#',' '],
[' ','#',' '],
[' ','#',' '],
['#','#','#']
]

two_map = [
[' ','#','#','#',' '],
['#',' ',' ',' ','#'],
[' ',' ',' ',' ','#'],
[' ',' ',' ','#',' '],
[' ',' ','#',' ',' '],
[' ','#',' ',' ',' '],
['#','#','#','#','#']
]

three_map = [
['#','#','#','#','#'],
[' ',' ',' ','#',' '],
[' ',' ','#',' ',' '],
[' ',' ',' ','#',' '],
[' ',' ',' ',' ','#'],
['#',' ',' ',' ','#'],
[' ','#','#','#',' ']
]

four_map = [
[' ',' ',' ','#',' '],
[' ',' ','#','#',' '],
[' ','#',' ','#',' '],
['#',' ',' ','#',' '],
['#','#','#','#','#'],
[' ',' ',' ','#',' '],
[' ',' ',' ','#',' ']
]

five_map = [
['#','#','#','#','#'],
['#',' ',' ',' ',' '],
['#','#','#','#',' '],
[' ',' ',' ',' ','#'],
[' ',' ',' ',' ','#'],
['#',' ',' ',' ','#'],
[' ','#','#','#',' ']
]

six_map = [
[' ',' ','#','#',' '],
[' ','#',' ',' ',' '],
['#',' ',' ',' ',' '],
['#','#','#','#',' '],
['#',' ',' ',' ','#'],
['#',' ',' ',' ','#'],
[' ','#','#','#',' ']
]

seven_map = [
['#','#','#','#','#'],
[' ',' ',' ',' ','#'],
[' ',' ',' ','#',' '],
[' ',' ','#',' ',' '],
[' ','#',' ',' ',' '],
[' ','#',' ',' ',' '],
[' ','#',' ',' ',' ']
]

eight_map = [
[' ','#','#','#',' '],
['#',' ',' ',' ','#'],
['#',' ',' ',' ','#'],
[' ','#','#','#',' '],
['#',' ',' ',' ','#'],
['#',' ',' ',' ','#'],
[' ','#','#','#',' ']
]

nine_map = [
[' ','#','#','#',' '],
['#',' ',' ',' ','#'],
['#',' ',' ',' ','#'],
[' ','#','#','#','#'],
[' ',' ',' ',' ','#'],
[' ',' ',' ','#',' '],
[' ','#','#',' ',' ']
]

digits_maps = {':': sep_map,'0': zero_map, '1': one_map, '2': two_map, '3': three_map, '4': four_map, 
               '5': five_map, '6': six_map, '7': seven_map, '8':eight_map, '9': nine_map}

# gets time as string like '12:10:01' and print it
def print_time(time_string):
    total_map = [ [], [], [], [], [], [], [] ]
    for line_num in range(7):
        for time_digit in time_string:
            total_map[line_num].extend(digits_maps[time_digit][line_num])
            total_map[line_num].extend('  ')
    
    for line in total_map:
        for dig in line:
            print(dig, end='')
        print()
    
