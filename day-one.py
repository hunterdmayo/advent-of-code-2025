'''
If first letter L, subtract that number from current
If first letter R, add that number to current
Convert to mod 100 scale
'''
def turn_dial(rotations:list) -> int:
    count = 0
    current = 50
    for rotation in rotations:
        direction = rotation[0]
        number = int(rotation[1:])
        if direction == 'L':
            current = current - number
        elif direction == 'R':
            current = current + number
        current = current % 100
        if current == 0:
            count += 1
    return count

if __name__ == '__main__':
    is_done = False
    while not is_done:
        file_name = input('Please enter the name of a file: ')
        try:
            with open(file_name, 'r', encoding='utf8') as source_data_fh:
                source_text = source_data_fh.read()
                print('Number of Rotations: ' , len(source_text.split()))
                print('Number of times dial hits 0: ', turn_dial(source_text.split()))
                is_done = True
        except FileNotFoundError:
            print('Cannot find that file!')