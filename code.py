# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
data=pd.read_csv(path)
data=data.rename(columns={"Total":"Total_Medals"})
data.head(10)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    


# --------------
#Code starts heredddx






data['Better_Event']=np.where(data.Total_Summer==data.Total_Winter,"Both",np.where(data.Total_Summer>data.Total_Winter,"Summer","Winter"))

better_event=data.Better_Event.value_counts().idxmax()

print(better_event)




# --------------
#Code starts here




def top_ten(df,name):
    k=df.nlargest(10,name)
    country_list=list(k['Country_Name'])
    return country_list


top_countries=data[['Country_Name','Total_Summer','Total_Winter','Total_Medals']]


top_countries=top_countries[:-1]

top_10_summer=top_ten(top_countries,'Total_Summer')
top_10_winter=top_ten(top_countries,'Total_Winter')
top_10=top_ten(top_countries,'Total_Medals')


common=[]

for i in range(10):
    k=top_10_summer[i]
    if k in top_10_winter and k in top_10:
        common.append(k)



print(common)



# --------------
#Code starts here


summer_df=data[data.Country_Name.isin(top_10_summer)]
winter_df=data[data.Country_Name.isin(top_10_winter)]
top_df=data[data.Country_Name.isin(top_10)]

plt.figure(figsize=(20,10))
plt.bar(summer_df.Country_Name,summer_df.Total_Summer)
# ax_1.set_title("bar chart between country_name and total summer medals")
plt.bar(winter_df.Country_Name,winter_df.Total_Winter)
# ax_2.set_title("bar chart between country_name and total winter medals")
plt.bar(top_df.Country_Name,top_df.Total_Medals)
# ax_3.set_title("bar chart between country_name and total medals")


plt.title("bar chart between country name and medal counts ")
plt.show()




# --------------
#Code starts here




summer_df['Golden_Ratio']=summer_df['Gold_Summer']/summer_df['Total_Summer']
# summer_country_gold=summer_df.Golden_Ratio.value_counts()
summer_max_ratio=summer_df.Golden_Ratio.max()

k=summer_df[summer_df['Golden_Ratio']==summer_max_ratio]
summer_country_gold=k['Country_Name'].tolist()[0]
print(summer_max_ratio)
# print(summer_country_gold,summer_max_ratio)
# print(type(summer_country_gold))


winter_df['Golden_Ratio']=winter_df['Gold_Winter']/winter_df['Total_Winter']
# summer_country_gold=summer_df.Golden_Ratio.value_counts()
winter_max_ratio=winter_df.Golden_Ratio.max()

l=winter_df[winter_df['Golden_Ratio']==winter_max_ratio]
winter_country_gold=l['Country_Name'].tolist()[0]
# print(summer_country_gold,summer_max_ratio)
# print(type(summer_country_gold))
print(winter_max_ratio)


top_df['Golden_Ratio']=top_df['Gold_Total']/top_df['Total_Medals']
# summer_country_gold=summer_df.Golden_Ratio.value_counts()
top_max_ratio=top_df.Golden_Ratio.max()

m=top_df[top_df['Golden_Ratio']==top_max_ratio]
top_country_gold=m['Country_Name'].tolist()[0]
# print(summer_country_gold,summer_max_ratio)
print(top_max_ratio)




# --------------
#Code starts here


data_1=data[:-1]

data_1['Total_Points']=data_1['Gold_Total']*3+data_1['Silver_Total']*2+data_1['Bronze_Total']

most_points=max(data_1.Total_Points)
best_country=data_1.loc[data_1.Total_Points.idxmax(),'Country_Name']



# --------------
#Code starts here


best=data[data['Country_Name']==best_country]


best=best[['Gold_Total','Silver_Total','Bronze_Total']]


best.plot.bar(stacked=True)

plt.xlabel('United States')
plt.ylabel('Medals Tally')

plt.xticks(rotation=45)

plt.show()


