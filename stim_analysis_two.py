import csv
import pandas as pd
from pandas import DataFrame

def median(time_list):
	sorts = sorted(time_list)
	length = len(sorts)
	if not length%2:
		return (sorts[length/2]+sorts[length/2-1])/float(2)
	return sorts[length/2]

def confusion_matrix(df_list, fan, age):
	# applied confusion matrix to given termins
	#  ------------------------
	# | TP -> hits |    FN     |
	#  ------------------------
	# | FP -> Fas  | TN -> CRs |
	#  ------------------------

	# structure of 2d list
	#[[TP, FN],[FP, TN]]

	tp_time = []
	fp_time = []
	tn_time = []

	return 0, 1, 2, 3

def main():
	#subject's data
	subject_data = list(csv.reader(open('/Users/almaskebekbayev/Dropbox/Exp 1 Face Fan Data/Face Fan Age/Data/s000LH.txt', 'rb'), delimiter='\t'))

	#master data
	master_test = DataFrame(pd.read_csv('/Users/almaskebekbayev/Dropbox/Exp 1 Face Fan Data/Face Fan Age/age-lists-3/s000/master-test.csv'))

	df_data = DataFrame(subject_data[586:775:2])

	df_data = df_data.drop([x for x in range(13) if x not in (7,11)], axis=1)
	cols = ['resp', 'time']
	df_data.columns = cols 

	df_data['resp_cmp'] = [x.replace('j', 'old') for x in df_data['resp'].values.tolist()]
	df_data['resp_cmp'] = [x.replace('k', 'new') for x in df_data['resp_cmp'].values.tolist()]

	df_data['fan'] = master_test['fan']
	df_data['status'] = master_test['age']
	df_data['correct_test'] = master_test['test']

	young_lf_data, young_tp_total, young_fp_total, young_tn_total = confusion_matrix(df_list=df_data.values.tolist(), fan='lf', age='young')

	
if __name__ == '__main__':
	main()
