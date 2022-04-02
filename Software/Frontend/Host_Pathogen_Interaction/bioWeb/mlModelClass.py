import pandas as pd
from sklearn.feature_selection import VarianceThreshold
class MlModelClass:
    def __init__(self,featureDf,labelDf,metaDf) -> None:
        self.originalFeatueDf=featureDf
        self.featureDf = featureDf
        self.labelDf = labelDf
        self.metaDf = metaDf
        print("Original File shape:", self.featureDf.shape)
        pass

    def filter(self, filterMethod='abundance', cutOff=0.001, type='original'):
        if(filterMethod=="abundance"):
            maxValuesObj = self.featureDf.max(axis=1)
            filt =maxValuesObj >= cutOff
            self.featureDf = self.featureDf[filt]
        elif(filterMethod == "variance"):
            filt = (self.featureDf.var(axis=1) < cutOff)
            self.featureDf = self.featureDf[filt]
            # print(selector)
            pass
        elif(filterMethod == "cum.abundance"):
            pass
        elif(filterMethod == "prevalence"):
            pass
        elif(filterMethod == "pass"):
            pass
        print("Filtered File shape:", self.featureDf.shape)
        if(filterMethod=="None" and cutOff==0.0):
            return self.originalFeatueDf
        return self.featureDf
        pass


    def getBoxChartValue(self,microName):

        feature_data = self.featureDf
        lable_data = self.labelDf
        if(microName=="None"):
            microName = list(feature_data['Unnamed: 0'])[0]
        row = feature_data.index[feature_data['Unnamed: 0']== microName].tolist()[0]
        print(row)
        featureSelectedMicro = self.originalFeatueDf.iloc[row]
        print(featureSelectedMicro)
        # concatannated_data = pd.concat(
        #     [feature_data.iloc[2], lable_data.iloc[1]], axis=1)
        featureSelectedMicro = featureSelectedMicro.to_frame(row)
        print(featureSelectedMicro)
        featureSelectedMicro["result"] = ["NaN"]+list(lable_data.iloc[1])
   
        pos = featureSelectedMicro.loc[featureSelectedMicro['result'] == '1', [
            True, False]]
        neg = featureSelectedMicro.loc[featureSelectedMicro['result']
                                    == '-1', [True, False]]
        print(feature_data.index[feature_data['Unnamed: 0'] == microName].tolist()[0])
        # print(pos)
        mi = 0
        ma = 0.01
        pos = list(pos[row])
        neg = list(neg[row])
        rangeOfPosList = max(pos)-min(pos)
        rangeOfNegList = max(neg)-min(neg)
        if(rangeOfPosList == 0):
            rangeOfPosList = 1
        if(rangeOfNegList == 0):
            rangeOfNegList = 1
        pos = [t*((ma-mi)/rangeOfPosList) for t in pos]
        neg = [t*((ma-mi)/rangeOfNegList) for t in neg]
        # print(pos)

        return pos, neg
if(__name__=="__main__"):
    import os
    csvFile=os.path.abspath("csvFiles/feat_crc_zeller_msb_mocat_specI.csv")
    # print(os.path.exists(csvFile))
    feature01=MlModelClass(csvFile)
    feature01.filter(filterMethod = "variance")
