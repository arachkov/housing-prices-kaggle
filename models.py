import numpy as np
from data_processing import Data

class Models:
    def __init__(self, dataFilepath, preprocess_fcn, ):
        self.dataLoader = Data(dataFilepath)
        self.dataLoader.preprocess_fcn()

    def model1(self):
        print("model1")
        return 0

    def model2(self):
        print("model2")
        return 0

if __name__ == "__main__":
    print("Still a lot to do")
