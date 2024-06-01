import random
import sys
import csv
from gui import interface

def main ():
    print("test 1")
    hiragana_kana, katakana_kana = sort_csv_structure()
    print("test 2")
    interface(receive_selected_kana)
    global kana_selected
    global tab_selected
    print("test 3", kana_selected, tab_selected)
    # sort_selected_kana(selected_kana, tab_name)

def sort_csv_structure():
    hiragana_kana = create_populate_dictionary("csv/hiragana.csv")
    katakana_kana = create_populate_dictionary("csv/katakana.csv")
    return hiragana_kana, katakana_kana


def create_populate_dictionary(file_path):
    try:
        with open(file_path) as file:
            reader = csv.reader(file)
            dict_kana = {}
            new_list_bool = False
            for row in reader:
                if not row:
                    new_list_bool = True
                    continue
                if new_list_bool:
                    key = row[1]
                    dict_kana[key] = [row]
                    new_list_bool = False
                else:
                    dict_kana[key].append(row)

    except FileNotFoundError:
        sys.exit("CSV file not found")
    return dict_kana


def sort_selected_kana(selected_kana, tab_name):
    # if tab_name
    # for group in selected_kana:
    print(tab_name)
    pass

def function3():
    pass


def receive_selected_kana(selected_kana, tab_name):
    print("func select_list",selected_kana)
    print("func tabname",tab_name)
    global kana_selected
    global tab_selected
    kana_selected = selected_kana
    tab_selected = tab_name


if __name__ == "__main__":
    main()

