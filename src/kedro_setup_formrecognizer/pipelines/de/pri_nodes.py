import numpy as np


def pri_clean_student_perf(df):
    df["term_1"] = np.where(df["term_1"] <20, 20, df["term_1"])
    df["term_1"] = np.where(df["term_1"] >100, 100, df["term_1"])
    df["term_2"] = np.where(df["term_2"] <20, 20, df["term_2"])
    df["term_2"] = np.where(df["term_2"] >100, 100, df["term_2"])
    
    return df