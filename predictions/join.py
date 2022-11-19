import pandas as pd 

pred_base = "/Users/danakenneylillej/Documents/Developer/nlpLawFall22/LJPFall22/predictions/predictions_TEST_baseBERT_ILDC.csv"
base = pd.read_csv(pred_base)

pred_legal = "/Users/danakenneylillej/Documents/Developer/nlpLawFall22/LJPFall22/predictions/predictions_TEST_legalBERT_ILDC.csv"
legal = pd.read_csv(pred_legal)

file_test = "/Users/danakenneylillej/Documents/Developer/nlpLawFall22/LJPFall22/predictions/TEST.csv"
test = pd.read_csv(file_test)

newfile = test.join(legal).join(base, on='index', how='left', lsuffix='_legal', rsuffix='_base').to_csv("/Users/danakenneylillej/Documents/Developer/nlpLawFall22/LJPFall22/predictions/compare.csv", index = False)
