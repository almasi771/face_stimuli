import csv
import pandas as pd
from pandas import DataFrame

#returns median number both for even or odd list
def median(time_list):
	time_list = [int(i) for i in time_list]
	sorts = sorted(time_list) #convert a list of str to floats or ints
	length = len(sorts)
	if not length%2:
		return (sorts[length/2] + sorts[length/2-1]) / float(2)
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
	matrix = [[0,0],[0,0]]

	for i in df_list:
		if i[0] == "j":
			if i[3] == fan and i[4] == age:
				if i[2] == i[5]:
					#TP
					matrix[0][0] += 1
					tp_time.append(i[1])
				else:
					#FP
					matrix[1][0] += 1
					fp_time.append(i[1])

		if i[0] == "k":
			if[3] == fan and i[4] == age:
				if i[2] == i[5]:
					#TN
					matrix[1][1] += 1
					tn_time.append(i[1])
				else:
					#FN
					matrix[0][1] += 1

	print "MATRIX",matrix[1][1]
	
	if fan == 'lf':
		if age == 'young':
			final = [
						float(matrix[0][0])/12,
						float(matrix[1][0])/12,
						median(tp_time),
						median(tn_time)
					]
		else:
			final = [
						float(matrix[0][0])/12,
						float(matrix[1][0])/12,
						median(tp_time),
						median(tn_time)
					]
	if fan == 'hf':
		if age == 'older':
			final = [
						float(matrix[0][0])/12,
						float(matrix[1][0])/12, 
						median(tp_time),
						median(tn_time)
					]
		else:
			final = [
						float(matrix[0][0])/12,
						float(matrix[1][0])/12,
						median(tp_time),
						median(tn_time)
					]	
	
	#final, TP, FP
	print "MATRIX",matrix[1][1]
	return final, matrix[0][0], matrix[1][0]

def main():
	#subject's data
	subject_data = list(csv.reader(open('/Users/almaskebekbayev/Dropbox/Exp 1 Face Fan Data/Face Fan Age/Data/s001RL.txt', 'rb'), delimiter='\t'))

	#master data
	master_test = DataFrame(pd.read_csv('/Users/almaskebekbayev/Dropbox/Exp 1 Face Fan Data/Face Fan Age/age-lists-3/s001/master-test.csv'))

	df_data = DataFrame(subject_data[584:775:2])

	df_data = df_data.drop([x for x in range(13) if x not in (7,11)], axis=1)
	cols = ['resp', 'time']
	df_data.columns = cols 

	#j -> yes, k -> no
	df_data['resp_cmp'] = [x.replace('j', 'old') for x in df_data['resp'].values.tolist()]
	df_data['resp_cmp'] = [x.replace('k', 'new') for x in df_data['resp_cmp'].values.tolist()]

	df_data['fan'] = master_test['fan']
	df_data['status'] = master_test['age']
	df_data['correct_test'] = master_test['test']


	#print df_data.values
	young_hf_data, young_hf_tp_total, young_hf_fp_total = confusion_matrix(df_list=df_data.values.tolist(), fan='hf', age='young')

	"""
	young_lf_data, young_lf_tp_total, young_lf_fp_total = confusion_matrix(df_list=df_data.values.tolist(), fan='lf', age='young')
	young_hf_data, young_hf_tp_total, young_hf_fp_total = confusion_matrix(df_list=df_data.values.tolist(), fan='hf', age='young')

	#print young_lf_data, young_lf_tp_total, young_lf_fp_total, young_lf_tn_total
	#print young_hf_data, young_hf_tp_total, young_hf_fp_total, young_hf_tn_total
	
	older_lf_data, older_lf_tp_total, older_lf_fp_total = confusion_matrix(df_list=df_data.values.tolist(), fan='lf', age='older')
	older_hf_data, older_hf_tp_total, older_hf_fp_total = confusion_matrix(df_list=df_data.values.tolist(), fan='hf', age='older')
	"""


	"""
	out = csv.writer(open('/Users/almaskebekbayev/Dropbox/stimuli_analysis/face_stimuli/output/s001RL.csv', 'w'), delimiter=',')
	
	out.writerow(
		sum(
			[young_lf_data, young_hf_data, older_lf_data, older_hf_data,
				[(young_lf_tp_total + young_hf_tp_total + older_lf_tp_total + older_hf_tp_total)/float(48)], #total TPs
				[(young_lf_fp_total + young_hf_fp_total + older_lf_fp_total + older_hf_fp_total)/float(48)]
			], [])
	) #total FPs
	"""
if __name__ == '__main__':
	main()
