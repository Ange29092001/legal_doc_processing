import os


def predict_date(
    structured_press_release: list,
) -> str:
    """init a pipe if needed, then ask all questions and group all questions ans in a list sorted py accuracy """

    date = structured_press_release["date"]

    return date


if __name__ == "__main__":

    # import
    from legal_doc_processing.utils import *
    from legal_doc_processing.press_release.utils import *
    from legal_doc_processing.press_release.segmentation.structure import (
        structure_press_release,
    )

    # structured_press_release_list
    press_txt_list = load_press_release_text_list()
    structured_press_release_list = [structure_press_release(i) for i in press_txt_list]

    # test one
    structured_press_release = structured_press_release_list[0]

    ans = predict_date(structured_press_release)

    # test others
    ans_list = [predict_date(p) for p in structured_press_release_list]
