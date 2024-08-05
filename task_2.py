def merge_files(file_list, output_file):
    """
    Merges multiple files into one, sorted by number of lines.

    Args:
        file_list (list): List of input file names.
        output_file (str): Name of the output file.
    Returns:
        None
    """
    file_info = []
    for name in file_list:
        with open(name, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            line_count = len(lines)
            file_info.append((name, line_count, lines))

    file_info.sort(key=lambda x: x[1])

    with open(output_file, 'w', encoding='utf-8') as outfile:
        for name, line_count, lines in file_info:
            outfile.write(f'{name}\n')
            outfile.write(f'{line_count}\n')
            outfile.writelines(lines)


input_file = ['1.txt', '2.txt']
output_file_name = 'result.txt'
merge_files(input_file, output_file_name)
