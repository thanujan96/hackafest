import pandas as pd
class MlModelClass:
    def __init__(self,CSVFile) -> None:
        self.df=pd.read_csv(CSVFile)
        print("Original File shape:",self.df.shape)
        pass

    def filter(self, filterMethod='abundance', cutOff=0.001):
        self.df=self.df
        if(filterMethod=="abundance"):
            maxValuesObj = self.df.max(axis=1)
            filt =maxValuesObj >= cutOff
            self.df=self.df[filt]
        elif(filterMethod == "cum.abundance"):
            pass
        print("Filtered File shape:", self.df.shape)
        pass


import os
csvFile=os.path.abspath("csvFiles/feat_crc_zeller_msb_mocat_specI.csv")
# print(os.path.exists(csvFile))
feature01=MlModelClass(csvFile)
feature01.filter()
