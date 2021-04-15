import time


def manipulate(filename, split_count=None, shaped=False, start_line=0, end_line=None, **enumerations):
    """
    :param filename: name of the file to be handled
    :type filename: string
    :param split_count: split line for certain no. of chars if it's one string
    :type split_count: int
    :param shaped:  if True, return the whole list at once instead of yielding each element
    :type shaped: bool
    :param start_line: the line you want to start manipulation with
    :type start_line: int
    :param end_line: the line you want to end manipulation with
    :type end_line: int
    :param enumerations: the key is the chars you want to replace with the value
    :return: elements at each iterations or whole list regarding start and end
    """
    final_shape = list()
    with open(filename) as file:
        for line_no, line in enumerate(file.readlines()):
            line_contents = list()
            if line_no < start_line:
                continue
            elif line_no == end_line:
                break
            else:
                line_elements = line.split()
                if line_elements:
                    for element in line_elements:
                        try:
                            if shaped:
                                line_contents.append(int(element))
                            else:
                                yield int(element)
                        except ValueError:
                            if split_count:
                                for step in range(len(element)):
                                    chars_slice = element[step: step+split_count]
                                    if enumerations:
                                        for target, replacer in enumerations.items():
                                            if chars_slice == target:
                                                chars_slice = replacer
                                    if shaped:
                                        line_contents.append(chars_slice)
                                    else:
                                        yield chars_slice
                            else:
                                if shaped:
                                    line_contents.append(element)
                                else:
                                    yield element
            if shaped:
                final_shape.append(line_contents)
            else:
                yield False
    if shaped:
        yield final_shape


if __name__ == '__main__':
    name1 = "small.in"
    name2 = "me_at_the_zoo.in"

    items = manipulate(name1, split_count=1, shaped=True, start_line=0, T=1, M=-1)
    # for i in range(10):
    #     item = next(items)
    #     print(item, type(item))
    #     time.sleep(0.25)

    # for item in items:
    #     print(item, type(item))
    #     time.sleep(0.25)

    # data = next(items)
    # print(data, type(data))

    items2 = manipulate(name2, split_count=1, shaped=True, start_line=0, end_line=2)
    for item2 in items2:
        print(item2)
        time.sleep(0.25)
