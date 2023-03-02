def reporting_student_improvement(df):
    #TODO: Remove space from column names
    #TODO: clean column names in de_utils
    df = df[["name","subject ","improvement"]]
    return df