
'''
For each bank:
-Iterate through entire row; keep track of highest digit you hit (and location)
-- Can stop early if you hit '9'
-- Highest digit can't be last in the bank
-- Then, for the second digit, start at the next position and find the next
-- highest number.
'''
def find_max_joltages(banks:list[str]) -> list[int]:
    maximum_joltages = []


    for bank in banks:
        length = len(bank)
        first_index = 0
        current_highest_first = 0
        current_highest_second = 0
        # Find the highest number for first digit
        for i in range(length - 1):
            if bank[i] == '9':
                first_index = i
                current_highest_first = 9
                break
            if int(bank[i]) > current_highest_first:
                current_highest_first = int(bank[i])
                first_index = i
        # Find the highest number for second digit
        for j in range(first_index+1, length):
            if int(bank[j]) > current_highest_second:
                current_highest_second = int(bank[j])
        
        # Add highest number to my list
        highest_joltage = str(current_highest_first) + str(current_highest_second)
        maximum_joltages.append(int(highest_joltage))

    print(maximum_joltages)
    return maximum_joltages


if __name__ == '__main__':
    is_done = False
    while not is_done:
        file_name = input('Please enter the name of a file: ')
        try:
            with open(file_name, 'r', encoding='utf8') as source_data_fh:
                source_text = source_data_fh.read()
                print(source_text)
                max_joltages = find_max_joltages(source_text.split('\n'))
                
                print('Total Output Joltage: ' , sum(max_joltages))
                is_done = True
        except FileNotFoundError:
            print('Cannot find that file!')