__all__ = ["ein2ncon", "ncon2ein"]

def ein2ncon(einstring):
    left, right = einstring.split('->')
    left_parts = left.split(',')
    parsed_lists = [list(part) for part in left_parts + [right]]

    if not parsed_lists:
        return []

    # map
    char_to_num = {char: -i for i, char in enumerate(parsed_lists[-1], start=1)}

    # counter
    positive_counter = 1

    # transform all lists
    transformed_lists = []
    for sublist in parsed_lists:
        transformed_sublist = []
        for char in sublist:
            if char in char_to_num:
                transformed_sublist.append(char_to_num[char])
            else:
                if char not in char_to_num:
                    char_to_num[char] = positive_counter
                    positive_counter += 1
                transformed_sublist.append(char_to_num[char])
        transformed_lists.append(transformed_sublist)

    return transformed_lists

def ncon2ein(number_lists):
    if not number_lists:
        return ""

    # Fun: number to string
    num_to_char = {}
    negative_chars = 'abcdefghzyxwvutsrqponmlkji'
    positive_chars = 'ijklmnopqrstuvwxyzabcdefgh'  # 从 i 开始的字母序列

    # Minus
    negative_nums = sorted(set(num for num in number_lists[-1] if num < 0), reverse=True)
    for i, num in enumerate(negative_nums):
        num_to_char[num] = negative_chars[i]

    # Positive
    positive_nums = sorted(set(num for sublist in number_lists for num in sublist if num > 0))
    for i, num in enumerate(positive_nums):
        num_to_char[num] = positive_chars[i]

    # Number to string
    char_lists = []
    for sublist in number_lists:
        char_list = ''.join(num_to_char[num] for num in sublist)
        char_lists.append(char_list)

    # Construct final einstring
    left_part = ','.join(char_lists[:-1])
    right_part = char_lists[-1]
    einstring = f"{left_part}->{right_part}"

    return einstring
