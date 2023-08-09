import os
import polib

def main():
    # content = {}
    # with open(file_path, "r", encoding="utf-8") as file:
    #     content = file.read()

    po_path = "locales/zh_Hant/LC_MESSAGES/messages.po"
    po_content = polib.pofile(po_path)
    for entry in po_content:
        msgid = entry.msgid
        msgstr = entry.msgstr

        occurrences = entry.occurrences
        for location in occurrences:
            file_path, line_number = location
            # 讀去檔案
            with open(file_path, "r", encoding="utf-8") as fp:
                lines = fp.readlines()

            # 取代文字
            line_content = lines[int(line_number) - 1]
            lines[int(line_number) - 1] = line_content.replace(msgid, msgstr)

            # 寫回檔案
            with open(file_path, "w", encoding="utf-8") as fp:
                fp.writelines(lines)






        # print(entry.msgid, entry.msgstr)


def read_file(path):
    content = {}
    with open(path, "r", encoding="utf-8") as file:
        content = file.read()
    return content

if __name__ == '__main__':
    main()