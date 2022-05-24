from analyzer import Analyzer

def check_duplicate():
    return analyzer.check_duplicate()

def check_col_data_format():
    return analyzer.check_col_data_format()

def check_missing_values():
    return analyzer.check_missing_values()

def check_outliers():
    return analyzer.check_outliers()
    

def main():
    '''
        You can check the return values for 
        each variables below by printing it.
        outliers is an example below
    '''
    cols_format = check_col_data_format()
    has_duplicates = check_duplicate()
    has_missing_vals = check_missing_values()
    has_outliers = check_outliers()
    print("Outliers:\n")
    print(has_outliers)

if __name__ == "__main__":
    analyzer = Analyzer(path_to_file="./data/data.csv")
    main()