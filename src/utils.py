def read_file_lines(file_path, callback=lambda line: line.strip('\n')):
    lines = []
    with open(file_path) as f:
        for _, line in enumerate(f):
            lines.append(callback(line))
    return lines
