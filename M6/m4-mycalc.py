import pandas as pd
df = pd.read_csv (r'A:\New folder')

# block 1 - simple stats
mean1 = df['Value1'].mean()
sum1 = df['Value1'].sum()
max1 = df['Value1'].max()
min1 = df['Value1'].min()
count1 = df['Value1'].count()
median1 = df['Value1'].median()
std1 = df['Value1'].std()
var1 = df['Value1'].var()

# block 2 - group by
groupby_sum1 = df.groupby(['Result']).sum()
groupby_count1 = df.groupby(['Result']).count()

# print block 1
print ('Mean Value1: ' + str(mean1))
print ('Sum of Value1: ' + str(sum1))
print ('Max Value1: ' + str(max1))
print ('Min Value1: ' + str(min1))
print ('Count of Value1: ' + str(count1))
print ('Median Value1: ' + str(median1))
print ('Std of values: ' + str(std1))
print ('Var of values: ' + str(var1))

# print block 2
print ('Sum of values, grouped by the Value2: ' + str(groupby_sum1))
print ('Count of values, grouped by the Value2: ' + str(groupby_count1))
