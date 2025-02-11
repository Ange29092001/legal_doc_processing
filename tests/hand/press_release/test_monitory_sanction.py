from legal_doc_processing.press_release.press_release import press_release_df
    
    
def test_string_method():
    """
    test if montetary sanction predict return only string
    """

    df=press_release_df(
        "cftc",

        sample=0.25,
    )

    df["monetary_sanction"]= df.pr.apply(lambda i: i.predict('monetary_sanction'))
    for i in range(len(df["monetary_sanction"])):
        if df["monetary_sanction"][i][0] is tuple:
            if df["monetary_sanction"][i][0][0] is not str:
                raise AssertionError
        


