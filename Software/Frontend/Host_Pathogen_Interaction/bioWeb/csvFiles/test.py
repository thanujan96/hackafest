def getBoxChartValue(microName):

    feature_data = pd.read_csv("./feat_crc_zeller_msb_mocat_specI.csv")
    lable_data = pd.read_csv("./label_crc_zeller_msb_mocat_specI.csv")

    row = feature_data.index[feature_data['Unnamed: 0'] == microName].tolist()[
        0]
    print(row)
    featureSelectedMicro = feature_data.iloc[[row]]
    print(featureSelectedMicro)
    # concatannated_data = pd.concat(
    #     [feature_data.iloc[2], lable_data.iloc[1]], axis=1)
    # featureSelectedMicro = featureSelectedMicro.to_frame(row)
    print(featureSelectedMicro)
    featureSelectedMicro["result"] = ["NaN"]+list(lable_data.iloc[1])

    pos = featureSelectedMicro.loc[featureSelectedMicro['result'] == '1', [
        True, False]]
    neg = featureSelectedMicro.loc[featureSelectedMicro['result']
                                    == '-1', [True, False]]
    print(
        feature_data.index[feature_data['Unnamed: 0'] == microName].tolist()[0])
    # print(pos)
    mi = 0
    ma = 0.1
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


pos, neg = getBoxChartValue("Methanoculleus marisnigri [h:1]")
print
