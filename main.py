import pandas as pd

# Enter in the CSVs you want to process:
df_primary = pd.read_csv('TEST_dryer_profile_611_1.csv', header=None)
df_secondary = pd.read_csv('converted0_MDF_EV.csv', header=None)

# Adding a new empty column to the primary (dryer) dataframe to merge it with the secondary's (EV) dataframe:
df_primary['newcol'] = ""

# Filling the third empty column of the primary with the power values from the second column in the secondary dataframe:
df_primary.iloc[:,2]= df_secondary.iloc[:,1]
df_primary_and_secondary = df_primary

#Labeling the primary and secondary columns (will remove the labels at the end):
df_primary_and_secondary.columns = ['Time', 'Power_1', 'Power_2']


# Creating a new dataframe for the switched output:
df_switching_output = pd.DataFrame() # Create empty dateframe

# Set first columns equal to the same ones of the primary & secondary merged dataframe, zero out the power col:
df_switching_output['Time'] = df_primary_and_secondary.iloc[:,0]
df_switching_output['Power'] = df_primary_and_secondary.iloc[:,1]
df_switching_output['Power'] = 0


# Double check that everything is working as it should:
#print(df_primary_and_secondary)
#print(df_switching_output)

# How do you get to a specific entry in a df with if you have dimensions?
#print(df_primary_and_secondary.iloc[0,1])

# Comparison process:
# We want to first check if the primary is over 100 W, if it is, then we automatically turn it on
# and whatever value that is is written into its corresponding df_switching_output index. If the primary is
# lower than that, we can look at the secondary and see if it's above 100. If it is, then the corresponding
# df_switching_output index is equal to the secondary.

count = 0
for i in range(len(df_primary_and_secondary)):

    if df_primary_and_secondary.iloc[i,df_primary_and_secondary.columns.get_loc('Power_1')] > 100:
        df_switching_output.iloc[i,1] = df_primary_and_secondary.iloc[i,df_primary_and_secondary.columns.get_loc('Power_1')]

    elif df_primary_and_secondary.iloc[i,df_primary_and_secondary.columns.get_loc('Power_2')] > 100:
        df_switching_output.iloc[i,1] = df_primary_and_secondary.iloc[i,df_primary_and_secondary.columns.get_loc('Power_2')]

# else don't change anything (if both are below threshold of 100)

'''
    if count == 100:
        print('made it to 100')
    if count % 10000 == 0:
        print('made it to '+str(count))
    count += 1
    #print('this is count ' + str(count))
    #print(df_switching_output.iloc[i])
'''
# printing to see if it worked, but we still won't be able to tell till we see the CSV:
print(df_switching_output)

# Printing out the final output CSV: :D
df_switching_output.to_csv('switched_output.csv', index=False)

#import matplotlib.pyplot as plt
#df_switching_output.plot()
#plt.show()
#print(df_primary_and_secondary.iloc[0,df_primary_and_secondary.columns.get_loc('Power_1')])
#df3 = df_primary_and_secondary[df_primary_and_secondary['Power_1'] > 100]
#print(df3)









# Removing column labels for easier gridlabbing (might do this at the very end instead if it's easier for python):
#df_primary_and_secondary.columns = [''] * len(df_primary_and_secondary.columns)
#print (df_primary_and_secondary)