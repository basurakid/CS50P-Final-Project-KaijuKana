import random
import csv
from class_gui import Window


def main():
    # Filtrar el csv en un diccionario con listas de kana
    hiragana_kana, katakana_kana = sort_csv_structure()
    # Crea gui con Window custom class
    window = Window()
    # Checkea si se pulsa start quiz o submit
    window.after(100, lambda: check_selection(window, hiragana_kana, katakana_kana))
    window.after(100, lambda: check_answers(window))
    # Inicia el mainloop
    window.mainloop()


def check_answers(window):
    """
    Checkea si se ha asignado respuestas al pulsar submit
    """
    if window.quiz_answers:
        quiz_results(window)
    # Si no se llama a si mismo para seguir checkeando
    else:
        window.after(100, lambda: check_answers(window))


def check_selection(window, hiragana_kana, katakana_kana):
    """
    Checkea si se ha seleccionado los kana para quiz con startquiz boton
    """
    if window.selected_kana and window.selected_tab:
        sort_selected_kana(hiragana_kana, katakana_kana, window)
    else:
        window.after(100, lambda: check_selection(window, hiragana_kana, katakana_kana))


def sort_csv_structure():
    """
    Inicia funcion create_populate_dictionary para ambos hiragana y katakana
    """
    hiragana_kana = create_populate_dictionary("csv/hiragana.csv")
    katakana_kana = create_populate_dictionary("csv/katakana.csv")
    return hiragana_kana, katakana_kana


def create_populate_dictionary(file_path):
    """
    Helper que abre y detecta espacios en blanco para crear keys:listas en un diccionario
    """
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
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
        raise FileNotFoundError
    return dict_kana


def quiz_results(window):
    """
    Checkea la respuesta contra el kana en quiz answers y aumenta score
    """
    wrong_answers = []
    score = 0
    for i in range(len(window.quiz_answers)):
        if window.quiz_answers[i] == window.quiz_kana[i][0]:
            score += 1
            wrong_answers.append("")
        else:
            wrong_answers.append("X")

    window.quiz_score = score
    window.wrong_answers = wrong_answers
    window.switch_frame(window.frame)


def sort_selected_kana(hiragana_kana, katakana_kana, window):
    """
    Crea una lista con los kana para los label de quiz kana, random shuffle para cambiar el orden
    """
    quiz_kana = []
    if window.selected_tab == "Hiragana":
        for group in window.selected_kana:
            group_key = group.split("/")[0]
            if group_key in hiragana_kana:
                quiz_kana += hiragana_kana[group_key]
    else:
        for group in window.selected_kana:
            if group == "Irregular":
                quiz_kana += katakana_kana["トゥ"]
            else:
                group_key = group.split("/")[0]
                if group_key in katakana_kana:
                    quiz_kana += katakana_kana[group_key]
    random.shuffle(quiz_kana)
    window.quiz_kana = quiz_kana
    window.switch_frame(window.frame)


if __name__ == "__main__":
    main()
