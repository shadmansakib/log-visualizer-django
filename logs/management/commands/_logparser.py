import re


def _read_log(file):
    with open(file, 'r') as logfile:
        for line in logfile:
            yield line


def _parser(line):
    regex = r'^(\w+\s\d{2}\s\d{2}:\d{2}:\d{2})\s([\w-]+)\s(([_\.a-zA-Z-]*)(\[[_a-zA-Z-]+\])*)[\[\d*\]]*:(.*)$'

    pattern = re.compile(regex)
    match = pattern.search(line.strip())

    return match.group(1), match.group(3), match.group(6)


def parse(file):
    lines = _read_log(file)

    for line in lines:
        yield _parser(line)
