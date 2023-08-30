import polib

def main():
    po_path = "locales/zh_Hant/LC_MESSAGES/messages.po"
    po_content = polib.pofile(po_path)
    for entry in po_content:
        msgid = entry.msgid
        msgstr = entry.msgstr

        occurrences = entry.occurrences
        for location in occurrences:
            file_path, line_number = location

            # 讀取檔案
            lines = read_file(file_path)

            # 取代文字
            line_content = lines[int(line_number) - 1]
            lines[int(line_number) - 1] = line_content.replace(msgid, msgstr)

            # 寫回檔案
            write_file(file_path, lines)


def read_file(path):
    lines = {}
    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()
    return lines

def write_file(path, lines):
    with open(path, "w", encoding="utf-8") as fp:
        fp.writelines(lines)

if __name__ == '__main__':
    main()