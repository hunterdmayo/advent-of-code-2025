import math

'''
Take input, strip leading 0 (if any); split in half; if first half === second half --> invalid (add to list)
'''
def find_invalid_ids(ranges: list[str]) -> list[str]:
    invalid_ids = []

    # Each item in the list is a range 1111-1122
    # Need to get first num, second num; that creates the range
    for r in ranges:
        first, second = r.split('-')
        for id in range(int(first), int(second) + 1):
            string_id = str(id)
            if string_id[0] == 0:
                string_id = string_id[1:]
            length = len(string_id)
            half = math.ceil(length / 2)
            first_half = string_id[0:half]
            second_half = string_id[half:]

            if first_half == second_half:
                invalid_ids.append(id)

    return invalid_ids

def sum_invalild_ids(invalid_id_list: list[str]) -> int:
    sum = 0

    for id in invalid_id_list:
        sum = sum + int(id)
    
    return sum

if __name__ == '__main__':
    is_done = False
    while not is_done:
        file_name = input('Enter File Name: ')
        try:
            with open(file_name, 'r', encoding = 'utf8') as source_data_fh:
                source_text = source_data_fh.read()
                invalids = find_invalid_ids(source_text.split(','))
                id_sum = sum_invalild_ids(invalids)
                print(id_sum)
                is_done = True
        except FileNotFoundError:
            print("FILE NOT FOUND")