import pandas as pd

feature_data = pd.read_csv("./feat_crc_zeller_msb_mocat_specI.csv")
lable_data = pd.read_csv("./label_crc_zeller_msb_mocat_specI.csv")

print(feature_data['Unnamed: 0'].tolist().index("UNMAPPED"))
