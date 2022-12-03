def line_iterator(file_name):
    with open(file_name) as f:
        for line in f:
            yield line.strip()


def read_all(file_name):
    with open(file_name) as f:
        return [line.strip() for line in f.readlines()]