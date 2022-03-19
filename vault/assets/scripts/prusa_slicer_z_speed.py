import os
import re
import sys
import shutil

src = sys.argv[1]
src_file_parts = os.path.splitext(src)

if src_file_parts[1] == '.gcode':
    src_old = src
    src = src_file_parts[0] + '.g'
    os.rename(src_old, src)

# Uncomment if you would like to create a backup file before processing
bkp = src+'.bkp'
shutil.copyfile(src, bkp)

def replace_acc(src):
    with open(src, 'r') as src_file:
        content = src_file.read()
        result = re.sub('G1 Z([\d\.]*) F4800', r'G1 Z\1 F420', content, flags = re.M)

        return result

def replace_end_line_comments(lines):
    result_arr = []
    for line in lines.splitlines():
        # Check if the first non-whitespace character is ';'
        pos = line.strip().find(";")

        if pos == -1 or pos == 0:
            # no comment OR comment at beginning
            result_arr.append(line)
        else:
            # Comment at the end of the line
            # Place comment before the gcode line
            split_line = line.split(";")
            result_arr.append("; " + split_line[1].strip())
            result_arr.append(split_line[0])

    result_str = "\n".join(result_arr)
    return result_str


def write_out(src, out):
    with open(src, 'w') as res_file:
        res_file.write(out)


result = replace_acc(src)
result_without_end_line_comments = replace_end_line_comments(result)
write_out(src, result_without_end_line_comments)

print("done")


# if __name__ == "__main__":

#     result = replace_acc("C:\\Users\\carlk\\Downloads\\Temperature calibration.g")

#     replace_end_line_comments(result)
