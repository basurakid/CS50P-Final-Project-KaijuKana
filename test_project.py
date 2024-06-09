from project import create_populate_dictionary, quiz_results, sort_selected_kana
import csv
import pytest


class MockWindow():
    def __init__(self):
        self.quiz_kana = None
        self.quiz_answers = None
        self.quiz_score = None
        self.selected_tab = None
        self.selected_kana = None

        self.frame = None

    def switch_frame(self, frame):
        pass  # This is a dummy method that doesn't do anything

def test_create_populate_dictionary():
    with pytest.raises(FileNotFoundError):
        create_populate_dictionary("bad filepath")


def test_quiz_results():
    quiz_window = MockWindow()
    quiz_window.quiz_kana = [['gu', 'ぐ'], ['ga', 'が'], ['ge', 'げ'], ['go', 'ご'], ['gi', 'ぎ']]
    quiz_window.quiz_answers = ['gu','ga','wrong','go','wrong']

    quiz_results(quiz_window)
    assert quiz_window.quiz_score == 3, "Score is not as expected with incorrect answers"


def test_sort_selected_kana():
    katakana_kana = create_populate_dictionary("csv/katakana.csv")
    placeholder_list = []

    sort_window = MockWindow()
    sort_window.selected_tab = "Katakana"
    sort_window.selected_kana = ["Irregular"]
    test_irregular_kana = [['thi', 'ティ'], ['dhi', 'ディ'], ['dwu', 'ドゥ'], ['twu', 'トゥ']]

    sort_selected_kana(placeholder_list, katakana_kana, sort_window)
    assert sorted(sort_window.quiz_kana) == sorted(test_irregular_kana)
