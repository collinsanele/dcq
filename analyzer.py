import pandas as pd

class Analyzer:
    """
        A class that analyzes the quality of a given excel file.
        It checks the data uniformity per column, checks if there
        are duplicates, missing values and outliers.
    """

    def __init__(self,  path_to_file):
        self.path_to_file = path_to_file
        self.df = self.read_csv_file()
    
    def read_csv_file(self):
        '''
            Reads in a csv file using the provided path.
            RETURN:
                it returns a pandas dataframe object
        '''
        df = pd.read_csv(self.path_to_file)
        return df

    def convert_to_normal_types(self, df):
        '''
            Converts a pandas daataframe from pandas dtypes 
            to regular python types.
            ARGS:
                df: pandas dataframe object (A pandas dataframe object)
            RETURN:
                returns a converted pandas dataframe using 
                default python types
        '''
        df_convert = df.astype('object')
        return df_convert

    def check_col_data_format(self):
        '''
            Checks if datatype is the same accross all columns.
            RETURN:
                returns the result as a dict of column names and datatypes
        '''
        cols_data = {}
        df = self.df
        df = self.convert_to_normal_types(df=df)
        cols = df.columns
        for col_name in cols:
            cols_data[str(col_name).strip()] = type(df.loc[0, col_name])
        return cols_data

    def check_duplicate(self):
        '''
            Takes in a pandas dataframe and checks for 
            duplicates in the entire dataframe.
        
            RETURN:
                returns True if duplicate present or False if no
                duplicate in the dataframe
        '''
        df = self.df
        has_duplicate = df.duplicated().any()
        return has_duplicate

    def check_missing_values(self):
        '''
            Checks for missing values in the entire data (dataframe).
            RETURN:
                returns True if missing value or False if otherwise.
        '''
        df = self.df
        return df.isnull().values.any()

    def check_outliers(self):
        '''
             The outlier is calculated using 
             the statistical method called interquartile range 
             (IQR) instead of using Z-score.
             RETURN:
                returns a table of columns with True for
                columns with outliers and False for columns without outliers
        '''
        df = self.df
        q1=df.quantile(0.25)
        q3=df.quantile(0.75)
        IQR = q3-q1
        outliers = df[((df<(q1-1.5*IQR)) | (df>(q3+1.5*IQR)))]
        return outliers.notnull().any()

