def fe_student_improvement(df):
    df["improvement"] = df["term_2"]- df["term_1"] 
    return df