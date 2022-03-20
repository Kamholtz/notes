import os
import re
import sys
import shutil

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

def replace_end_line_comments_in_line(line):
    result_arr = []
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

    return result_arr


def write_out(src, out):
    with open(src, 'w') as res_file:
        res_file.write(out)


def add_missing_suffix(line:str, cmd:str, suffix_re, suffix:str):
    stripped = line.strip()

    if stripped.startswith(cmd) and suffix_re.search(stripped) == None:
        return stripped + " " + suffix

    return line


def replace_acceleration(line:str):
    result = re.sub('G1 Z([\d\.]*) F4800', r'G1 Z\1 F420', line, flags = re.M)
    return result

def process_lines(src, out):
    suffix_re = re.compile("T\d$")

    print("src: " + src + ", out: " + out)
    with open(src) as infile, open(out, 'w') as outfile:
        for line in infile:

            lines0 = replace_end_line_comments_in_line(line.strip())
            lines1 = [add_missing_suffix(x, "M104", suffix_re, "T0") for x in lines0]
            lines2 = [add_missing_suffix(x, "M140", suffix_re, "T0") for x in lines1]
            lines3 = [add_missing_suffix(x, "M109", suffix_re, "T0") for x in lines2]
            lines4 = [add_missing_suffix(x, "M190", suffix_re, "T0") for x in lines3]
            # lines5 = [replace_acceleration(x) for x in lines4]

            outlines = [x + "\n" for x in lines4]

            outfile.writelines(outlines)

def run (src):

    src_file_parts = os.path.splitext(src)

    # if src_file_parts[1] == '.gcode':
    #     src_old = src
    #     src = src_file_parts[0] + '.g'
    #     os.rename(src_old, src)

    # # Uncomment if you would like to create a backup file before processing
    # bkp = src+'.bkp'
    # shutil.copyfile(src, bkp)




    # result = replace_acc(src)
    # result_without_end_line_comments = replace_end_line_comments(result)

    out_name = src_file_parts[0] + '-out.g'
    # write_out(out_name, result_without_end_line_comments)

    process_lines(src, out_name)


src = sys.argv[1]
run(src)
print("done")


# if __name__ == "__main__":

#     run("C:\\Users\\carlk\\Downloads\\temp_calibration.g")
