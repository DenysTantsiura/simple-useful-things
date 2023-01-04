"""
Task: Create an automation for creating a subtitle file with two languages
"""
from multiprocessing.util import is_exiting
import sys
import pathlib


def fun_file_reader(file_entered):  # string with file-name
    """
    Simple read files.
    inn file_entered: string with file-name
    out (return): list of lines from file
    """
    with open(file_entered, encoding='utf-8') as fh:  # cp1251
        lines = fh.readlines()

    return lines  # list of lines from file


def fun_creater_header(lines):  # list with lines from file
    """
    Read lines from incoming list. Add new style above default (At the top of the screen) to header.
    inn lines: list with lines from file
    out (return): string of many lines from header in file (before starting dialogues)
    """
    sub_head = ''
    new_line = ''
    for line in lines:
        if new_line != '' and not line.startswith("Dialogue:"):
            sub_head += line
        elif line.startswith("Dialogue:"):
            break
        if not line.startswith("Style:") and new_line == '':
            sub_head += line
        elif line.startswith("Style:"):
            sub_head += line
            new_line = line.replace("Default", "Ustile")
            new_line = new_line.replace(",2,10,10,10,1", ",8,10,10,10,1")
            sub_head += new_line

    return sub_head  # string of many lines from header


def divider_for_translation(lines):  # list with lines from file
    """
    Read lines from incoming list. Add new style above default (At the top of the screen) to header.
    inn lines: list with lines from file
    out (return): 3 lists of strings from file
    """
    before_text_line_orig = []
    before_text_line_new = []
    text_lines = []
    for line in lines:
        if line.startswith("Dialogue:"):
            before_text_line_orig.append(line.split("Default,,0,0,0,,")[
                0]+"Default,,0,0,0,,")
            before_text_line_new.append(
                before_text_line_orig[-1].replace("Default", "Ustile"))
            text_lines.append(line.split("Default,,0,0,0,,")
                              [1].replace("\\N", " ").replace("<i>", "").replace("</i>", ""))

    # 3 lists of strings from file
    return before_text_line_orig, before_text_line_new, text_lines


# list with test-lines (strings) + string-file name
def file_creator(text_lines, new_filename):
    """
    Write file with only subtitle-text (for translate in future).
    inn file_entered: list with test-lines (strings)
    out (return): None
    """
    with open(new_filename, "w", encoding="utf-8") as fh:
        fh.writelines(text_lines)


def file_processing(file_entered):
    """
    Main file processing function.
    inn file_entered: string with file-name
    out (return): None
    """
    if not pathlib.Path(file_entered + "_Translated.txt").exists() or 'before_text_line_orig' not in locals():

        lines = fun_file_reader(file_entered)  # list of lines from file

        sub_head = fun_creater_header(lines)  # sub_head is Ok

        before_text_line_orig, before_text_line_new, text_lines = divider_for_translation(
            lines)
        # before_text_line_orig is Ok
        # before_text_line_new is Ok
        # text_lines is Ok

        file_creator(text_lines, file_entered + "_To_translate.txt")

    if pathlib.Path(file_entered + "_Translated.txt").exists() and before_text_line_orig:
        # new translated text in list of srtings
        text_lines_new = fun_file_reader(file_entered + "_Translated.txt")

        for num_line in range(len(before_text_line_orig)):
            sub_head += before_text_line_orig[num_line] + text_lines[num_line]
            sub_head += before_text_line_new[num_line] + \
                text_lines_new[num_line]

        file_creator(sub_head, file_entered + "=.ass")


def dir_clear(input_file):
    """
    clear the directory function.
    inn file_entered: string with dirr-name
    out (return): None
    """
    for fs_obj in pathlib.Path(input_file).iterdir():
        if fs_obj.is_file() and str(fs_obj)[-5:] != '=.ass':
            fs_obj.unlink()  # del file

    for fs_obj in pathlib.Path(input_file).iterdir():
        fs_obj.replace(str(fs_obj).replace(".ass=.ass", ".ass"))


def main():

    try:
        input_file = sys.args[1]
    except:
        input_file = 'D:\\projects\\sub'
    if pathlib.Path(input_file).is_file():
        if not pathlib.Path(input_file + "=.ass").exists():
            file_processing(input_file)
    elif pathlib.Path(input_file).is_dir():
        for fs_obj in pathlib.Path(input_file).iterdir():
            if fs_obj.is_file() and (fs_obj.suffix)[1:] == 'ass' and not pathlib.Path(input_file + "=.ass").exists():
                file_processing(str(fs_obj))
        answer_clean = input("Do You want to clear the directory? y?: ")
        if answer_clean == "y":
            dir_clear(input_file)
        # print(
        #     "Sorry, but '{input_file}' is NO file. Need subtitle file with 'ass' extensions.")
        # input("Press Enter for exit")


if __name__ == "__main__":
    main()
