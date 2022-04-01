import pandas as pd
from sklearn.feature_selection import VarianceThreshold
class MlModelClass:
    def __init__(self,CSVFile) -> None:
        self.df=CSVFile
        print("Original File shape:",self.df.shape)
        pass

    def filter(self, filterMethod='abundance', cutOff=0.001, type='original'):
        if(filterMethod=="abundance"):
            maxValuesObj = self.df.max(axis=1)
            filt =maxValuesObj >= cutOff
            self.df=self.df[filt]
        elif(filterMethod == "variance"):
            filt=(self.df.var(axis=1)<cutOff)
            self.df = self.df[filt]
            # print(selector)
            pass
        elif(filterMethod == "cum.abundance"):
            pass
        elif(filterMethod == "prevalence"):
            pass
        elif(filterMethod == "pass"):
            pass
        print("Filtered File shape:", self.df.shape)
        return self.df
        pass

if(__name__=="__main__"):
    import os
    csvFile=os.path.abspath("csvFiles/feat_crc_zeller_msb_mocat_specI.csv")
    # print(os.path.exists(csvFile))
    feature01=MlModelClass(csvFile)
    feature01.filter(filterMethod = "variance")
