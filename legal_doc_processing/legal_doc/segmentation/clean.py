from cleantext import clean
from legal_doc_processing import utils


from legal_doc_processing.legal_doc.segmentation.utils import *


def clean_doc(file_text):
    """ """

    pages = []
    for page in file_text.split("\x0c"):

        # clen text
        page_meta = [
            {
                "text": clean(
                    para,
                    lower=False,
                ).replace("_", "")
            }
            for para in page.split("\n")
        ]

        clean_page = []
        previous_line = {}
        text = ""

        # add meta data
        for line in page_meta:
            line["is_section_num"] = is_section_num(line["text"])
            line["is_title"] = is_title(line["text"])
            line["ends_with_ponc"] = ends_with_ponc(line["text"])
            line["is_alpha"] = sum(c.isalpha() for c in line["text"])
            line["start_with_upper"] = starts_with_upper(line["text"])

            # not relevant line
            if not line["is_alpha"]:
                continue
            if not same_sentence(previous_line, line):
                if text:
                    clean_page.append(text)
                    text = ""
            previous_line = line
            text = " ".join([text, line["text"]])

        if len(clean_page):
            pages.append(clean_page)

    return pages
