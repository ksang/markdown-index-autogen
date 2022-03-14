import argparse
import os

def get_section(data, anchor):
    start = end = -1
    for i, line in enumerate(data):
        if anchor in line:
            end = start = i+1
            continue
        if end >= 0:
            if len(line.strip()) != 0:
                end += 1
            else:
                break
    return start, end

def gen_index(level, dirpath, name):
    if name == "":
        name = os.path.basename(dirpath)
        return "{}- [{}]({})\n".format(level*'\t', name, dirpath.replace(" ", "%20"))
    return "{}- [{}]({})\n".format(level*'\t', name, os.path.join(dirpath, name).replace(" ", "%20"))

def get_index(path, extension):
    indexes = []
    for dirpath, subdirs, files in os.walk(path):
        num = 0
        for x in files:
            if x.endswith(extension):
                num += 1
                indexes.append(gen_index(1, dirpath, x))
        if num > 0:
            indexes.insert(-1*num, gen_index(0, dirpath, ""))
    return indexes

def autogen(filename, anchor, path, extension):
    data = []
    with open(filename,"r") as f:
        data = f.readlines()
    start, end = get_section(data, anchor)

    assert start > 0 and end > 0, \
        'can not find anchor "{}" in file: {}'.format(anchor, filename)
    new_index = get_index(path, extension)

    new_data = data[:start] + new_index + data[end:]

    with open(filename,"w") as f:
        f.writelines(new_data)

def main():
    parser = argparse.ArgumentParser(description='Generate / refresh a certian part of markdown file as index to reflect latest folder structre.')
    parser.add_argument('-f', '--file', type=str, default="README.md", help='Markdown file to modify.')
    parser.add_argument('-a', '--anchor', type=str, default="[comment]: # (markdown-index-autogen)", help='Comment anchor for indicate section to refresh.')
    parser.add_argument('-e', '--extension', type=str, default=".pdf", help='Extension of files to be indexed.')
    parser.add_argument('-p', '--path', type=str, default=".", help='Path for folder structure to generate.')
    parser.add_argument('args', nargs=argparse.REMAINDER)
    args = parser.parse_args()
    
    autogen(args.file, args.anchor, args.path, args.extension)

if __name__ == '__main__':
    main()