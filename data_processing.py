import numpy as np
import pandas as pd
import os

    # the reason I think we should make a class of this would be to be able
    # to easily call these function and try different things. Maybe this isn't
    # the best way, let me know what you think

class Data:
    def __init__(self, csvFilePath):
        self.dfRaw   = pd.read_csv(csvFilePath)
        self.df      = pd.read_csv(csvFilePath)

    def one_hot_encoding(self, columnName, removeEncoding=None):
        """
        Takes a column of categorical data and transforms it into a one

        Input
            columnName (str)                : column to be one hot encoded
            removeEncoding (array of str)   : one hot encoding to not include

        Output
            None
        """

        self.df = pd.get_dummies(self.df, columns=columnName
                                        , prefix={columnName : columnName}
                                        , dtype=float)

        if removeEncoding not None:
            for i, category in enumerate( removeEncoding ):
                removeEncoding[i] = columnName + '_' + category

            self.df.drop(columns=removeEncoding) # removes these columns

        return 0

    def convert_quality(self, columnName, NAvector=False):
        """
        Converts the column data from the categorical quality to a numerical
        one. Sometimes there is a NA, need to decide what to do with that.

        Input
            columnName (str)    : column whose data needs to be converted
            NAvector (bool)     : whether or not to create a vector from N/A
        """

        if NAvector:
            #TODO make a vector if NA wants to be separate than 0
        mapping = {'NA' : 0.0, 'Po' : 0.0, 'Fa' : 0.25, 'TA' : 0.5, 'Gd' : 0.75
                    , 'Ex' : 1.0 }

        self.df[columnName] = self.df[columnName].map( mapping )

        return 0


    def preprocess1(self, columnDelete=None):
        #
        columnDelete = ['MSSubClass', 'MSZoning', 'LotFrontage', 'LotArea'
                        , 'Street', 'Alley']
        self.df.drop(columns=columnDelete)

        return 0

    def preprocess2(self):
        self.df = 0

        return 0

    def split_data(self, frac_train):
        self.xtrain = 0; self.ytrain = 0
        self.xtest = 0; self.ytest = 0

if __name__ == "__main__":
    filename = "train.csv"
    data = Data("data" + os.sep + filename)
    columnDelete = []
    data.preprocess1(columnDelete)

    print(data.df.columns)
