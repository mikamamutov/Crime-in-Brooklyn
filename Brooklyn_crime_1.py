import requests
import pandas as pd
import matplotlib.pyplot as plt
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import streamlit as st


#apis from 1 until 52 for 2023, week 36 from 2023 is missing
#apis from 1 until 52 for 2022, week 27 is missing
#apis for 2024

api_urls_1 = [
'https://data.dathere.com/api/3/action/datastore_search?resource_id=d90815a9-bdad-4bd1-8eff-2df26e115424&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=6b5b81fa-3012-4868-bd8a-3004f8386f79&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=7a549b4e-041b-4a5c-b4b9-87244d3ebc68&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=43877205-9aa0-4c3e-9070-da9342891e51&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=126ef53f-7f9a-4525-ab8c-1ca058d845bd&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=9eff94e9-501e-43c7-a296-80af3ae7b228&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=93cc0ddc-6b66-48dc-a9f4-c8efb731530b&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=2f27ddd0-7eff-44ac-8e1f-02c9261b1b73&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=63bcd8b1-7059-40b7-bd3f-35c26a75f70b&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=150db8df-2842-4217-b5fc-4a003139b475&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=29b410dd-d895-42b3-9dd7-9ae89e908b97&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=6472e946-1489-49ef-91c1-541e346d5b03&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=81be5587-e4a6-4ea9-9024-1d1e5052744d&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=b095080a-88f9-47da-8151-3bcf777a353e&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=305bd897-2bd9-4670-a5e7-218fc14a1375&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=2da95030-f8e4-4439-a3ec-a4001a4cbb43&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=38ee57ca-f863-476d-a625-00ec42225e6a&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=f446e018-c395-400b-b136-7d71a76df7b4&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=6eb338ef-cc78-4c90-af96-8930030af90c&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=6161ad9f-63e5-4d6e-8158-82bac9197542&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=cb80e157-2912-4262-b6cc-50ae6877dcdf&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=2b0a4be2-2a5e-4401-99a1-a8b51a0b62c0&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=876a589a-9019-4499-a2af-314bcbe84450&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=4eb16f31-f31d-4fad-9341-8c9a96471133&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=a7989df1-6912-4772-a726-b617f04be8c1&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=5a4fffb4-9bf6-4bbd-8727-caf3558e3cef&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=0e39c918-7efe-4cbf-aa14-429dcd75141b&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=035d6a5f-75e0-4794-a611-58978b87a290&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=a51a464d-3763-453c-aea9-9bfd4ac0d0f3&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=d0bf9702-be22-44d6-8235-4e1802d446d5&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=f4b21ad6-4559-45ad-a5f9-7c975d06a61c&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=c096a6f1-e8f1-49c5-87e5-2798557f4e72&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=97c3fb0b-78c0-4ec8-8abf-b45420d9596d&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=89302492-abba-4604-803a-36ec045c54b1&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=0760ca06-927e-453e-abc6-3d433b3ef3b8&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=050c9a2a-2ede-47a5-99c4-9999522995f6&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=6f92c461-19fb-429d-921e-4dc674beb519&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=f7859a72-547b-48f2-bb1b-2142a0106c90&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=6f22abbf-35a0-4461-8ef3-e73f3a890283&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=1a7cd4bb-3709-4a83-bfeb-28be1bf1ded8&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=05733d70-4233-4962-a0d7-70aa22845f10&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=833a98f4-e376-48d9-baae-b1b82fd0b1cf&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=2bd75b8f-d128-4173-b59e-e6a69a5ce683&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=20f544b6-4e93-4fdc-b4e2-480873faee6e&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=67d675dd-8baa-4ece-8ac8-f22889785275&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=ac0a0f47-2f0e-4b17-8df1-e7428ec67c05&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=9f819bbd-e498-479b-b7e4-2fb4dad463aa&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=43557fa5-aee7-44d4-afb1-9424a3826dbe&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=aed1dbf6-9423-4708-adeb-7d6508ef775d&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=ae67a1b5-9f42-4004-851e-2f70f7eb68a2&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=6fc68a0c-8e35-4ea7-9a49-721e4694b95c&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=e6d90fe0-aec9-4bfc-99d9-7898964812dc&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=80b21635-306e-4c84-be82-13832297804d&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=a5c42a14-0140-4257-8f27-0e650fe4467f&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=3ae82f39-5034-4154-851b-ba855f2c15cb&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=a2f851f7-4226-4178-becb-645551477353&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=307dab18-892e-483f-8949-5fd8ec58321d&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=9305025c-14f4-4e03-8525-909dc132debd&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=18cf1e53-d047-4c8b-b004-3b9e619f5e3e&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=034a0ac6-7b0f-4a41-a63e-e090cf51dc65&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=960471f7-1e69-47be-8bff-bbe120d1f7ac&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=f250c717-303e-457f-821e-a10a2c31bc2b&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=34aebbfa-5b45-4a48-a692-3f1d838f60c9&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=627d36ad-950e-4945-9543-03c25e32411a&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=81b3f27f-a438-4669-8f30-9cbda97d2d3c&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=f3103d2f-4c2a-4a73-bfae-aa9f20557e55&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=39d1c1fe-0d88-4f0c-b270-f66fdbeff53b&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=db301f30-6417-46c8-8c0a-8bbee3a12c0c&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=d5e6821c-1e82-4a55-9286-a75d0262a109&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=0c75a362-8416-4d39-8468-f78011decae4&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=9724ddbf-a44e-4dd0-a82e-d0eeb4d7f30c&limit=10000',
'https://data.dathere.com/api/3/action/datastore_search?resource_id=d4ce77fc-deed-415c-8cfd-a00da374a7b3&limit=10000',

]
#

#In some of the data, the time values are different types so they need to be processed separately
api_urls_2 = ['https://data.dathere.com/api/3/action/datastore_search?resource_id=84b904ff-8d22-41f3-97a7-12449df2194e&limit=10000',
              'https://data.dathere.com/api/3/action/datastore_search?resource_id=f94e3863-5f81-454b-8d5f-53437d9df2cc&limit=10000',
              'https://data.dathere.com/api/3/action/datastore_search?resource_id=2d3f4015-0395-4230-b766-e30619041adc&limit=10000',
              'https://data.dathere.com/api/3/action/datastore_search?resource_id=b9f6c75e-a11e-4b07-9a93-533b5533578f&limit=10000',
              'https://data.dathere.com/api/3/action/datastore_search?resource_id=02973d59-c16e-48c6-b20e-107081b5c020&limit=10000',
              'https://data.dathere.com/api/3/action/datastore_search?resource_id=4b4aa175-fa88-4cfc-975c-5c23f21cd240&limit=10000',
              'https://data.dathere.com/api/3/action/datastore_search?resource_id=0c837ca2-990e-4dad-bc54-e58944c63b35&limit=10000',
              'https://data.dathere.com/api/3/action/datastore_search?resource_id=7d6c8086-9307-404b-bbd1-c2f3b1b4559d&limit=10000',
              'https://data.dathere.com/api/3/action/datastore_search?resource_id=2101f356-a85b-466d-a0b4-78c08dced5a8&limit=10000',
              'https://data.dathere.com/api/3/action/datastore_search?resource_id=07079653-bee4-406c-b101-8ac36eeaa790&limit=10000',
              'https://data.dathere.com/api/3/action/datastore_search?resource_id=179f9eb4-0bc1-490b-b7a6-5355a942c6d0&limit=10000',
              'https://data.dathere.com/api/3/action/datastore_search?resource_id=ea381ff5-c361-40ed-bdb8-ebadd6d73bdc&limit=10000',
              'https://data.dathere.com/api/3/action/datastore_search?resource_id=f36dd64c-c617-4c39-b9bc-20344a937324&limit=10000',
              'https://data.dathere.com/api/3/action/datastore_search?resource_id=da263f45-438e-4373-8364-eb6270a01cf7&limit=10000',
              'https://data.dathere.com/api/3/action/datastore_search?resource_id=6eadda12-e3d1-4cfb-813e-6ff0c62d9a77&limit=10000',
              'https://data.dathere.com/api/3/action/datastore_search?resource_id=ba2f8f10-785a-41e1-8554-fdbb78f7b0a0&limit=10000',
              'https://data.dathere.com/api/3/action/datastore_search?resource_id=b144a802-101a-44cb-b40e-f98c1376a4d7&limit=10000',
              'https://data.dathere.com/api/3/action/datastore_search?resource_id=965a5d6a-c8e8-448c-8f11-1f1b90739d78&limit=10000',
              'https://data.dathere.com/api/3/action/datastore_search?resource_id=646f6126-ba87-47b0-94fa-bce715f109ae&limit=10000',
              'https://data.dathere.com/api/3/action/datastore_search?resource_id=fc8a0c35-12df-4dd7-9387-8a8eb17ec515&limit=10000',
              'https://data.dathere.com/api/3/action/datastore_search?resource_id=ffb5fac0-9d8e-47e1-88fe-c4ec786d62dd&limit=10000',
              'https://data.dathere.com/api/3/action/datastore_search?resource_id=0c3db2f8-717e-4c06-b306-e727ba769ddd&limit=10000',
              'https://data.dathere.com/api/3/action/datastore_search?resource_id=4b3496b8-356e-410e-af9a-c2fa56e01d6c&limit=10000',
              'https://data.dathere.com/api/3/action/datastore_search?resource_id=9f0128d6-7a1c-4c39-91e5-e23cf6a68abb&limit=10000',
              'https://data.dathere.com/api/3/action/datastore_search?resource_id=32e08b25-858e-4e6c-98f6-5bb6d4fd2d90&limit=10000'
            ]
#get data from the APIs
def get_data(api_urls):
    data=[]
    for url in api_urls:
        response = requests.get(url)
        data.extend(response.json()['result']['records'])
    return data

data_1 = get_data(api_urls_1)
data_2 = get_data(api_urls_2)

#Fix the dates in the second set of data
df_data4 = pd.json_normalize(data_2)
df_data4["End_Date"] = pd.to_datetime(df_data4["End_Date"].str.split("T").str[0])
df_data4["End_Date"] = df_data4["End_Date"].dt.strftime("%-m/%d/%Y")

#Combine two datasets
df_combined_data_1 = pd.json_normalize(data_1)
df = pd.concat([df_combined_data_1,df_data4])

#Change the type of data for the new unified dataset
df["Start_date"] = df["Start_date"].str.strip()
df["Start_date"] = pd.to_datetime(df["Start_date"])
df["End_Date"] = df["End_Date"].str.strip()
df["End_Date"] = pd.to_datetime(df["End_Date"],format="%m/%d/%Y")

#Create separate dataframes for North Brooklyn and South Brooklyn and merge them
df_brooklyn_north = df[df["Precinct"] == "Brooklyn North"]
df_brooklyn_south = df[df["Precinct"] == "Brooklyn South"]
df_brooklyn = pd.merge(df_brooklyn_north, df_brooklyn_south,on = ["Start_date","End_Date", "Crime"], how = "outer", suffixes=("_brooklyn_north","_brooklyn_south"))
#Sum up the values from North Brooklyn and South Brooklyn, get month and year to filter
df_brooklyn["Current_total"] = df_brooklyn["Current_brooklyn_north"] + df_brooklyn["Current_brooklyn_south"]
df_brooklyn['Month_number'] = df_brooklyn['Start_date'].dt.month
df_brooklyn['Year_number'] =df_brooklyn['Start_date'].dt.isocalendar().year
df_brooklyn['Week_number'] = df_brooklyn['Start_date'].dt.isocalendar().week
#Extract data for Brooklyn (North and South combined) for Summer and Winter
df_brooklyn_summer = df_brooklyn[df_brooklyn["Month_number"].isin([6,7,8])]
df_brooklyn_winter = df_brooklyn[df_brooklyn["Month_number"].isin([1,12,2])]

#all crime types
crimes = ["Murder", "Rape", "Robbery", "Fel. Assault", "Burglary", "Gr. Larceny", "G.L.A.","Transit","Housing","Petit Larceny","Misd. Assault","UCR Rape*","Other Sex Crimes","Shooting Vic.","Shooting Inc.","Hate Crimes"]

#Calculate all Crime numbers in 2023 in Summer and Winter in Brooklyn organized by Crime
df_brooklyn_summer_all_2023 = df_brooklyn_summer[(df_brooklyn_summer["Crime"].isin(crimes)) & (df_brooklyn_summer["Year_number"] == 2023)]
df_brooklyn_winter_all_2023 = df_brooklyn_winter[(df_brooklyn_winter["Crime"].isin(crimes)) & (df_brooklyn_winter["Year_number"] == 2023)]
df_brooklyn_summer_all_2023_total = df_brooklyn_summer_all_2023["Current_total"].sum()
df_brooklyn_winter_all_2023_total = df_brooklyn_winter_all_2023["Current_total"].sum()
#Calculate all Crime numbers in 2022 in Summer and Winter in Brooklyn organized by Crime
df_brooklyn_summer_all_2022 = df_brooklyn_summer[(df_brooklyn_summer["Crime"].isin(crimes)) & (df_brooklyn_summer["Year_number"] == 2022)]
df_brooklyn_winter_all_2022 = df_brooklyn_winter[(df_brooklyn_winter["Crime"].isin(crimes)) & (df_brooklyn_winter["Year_number"] == 2022)]
df_brooklyn_summer_all_2022_total = df_brooklyn_summer_all_2022["Current_total"].sum()
df_brooklyn_winter_all_2022_total = df_brooklyn_winter_all_2022["Current_total"].sum()

# #Murders data only Start
# #Function to extract murder data only
# def murders(df,precinct):
#     df_precinct = df[df["Precinct"] == precinct]
#     df_precinct_murder = df_precinct[df_precinct["Crime"] == "Murder"]
#     df_precinct_murder_bydate = df_precinct_murder[["YTD_Current",'Start_date','End_Date','Precinct','Commissioner','Mayor']].sort_values(by = 'End_Date', ascending= False)
#     return df_precinct_murder_bydate

# Get data for murders in Brooklyn North and South
# brooklyn_south_murders = murders(df,"Brooklyn South")
# brooklyn_north_murders = murders(df,"Brooklyn North")
# #Merge South and North Brooklyn Murders using Start date
# brooklyn_south_north_murders = brooklyn_south_murders.merge(brooklyn_north_murders, on = "Start_date")
# #Murders data only End
#
# #Get a week number from North Brooklyn and South Brooklyn
# brooklyn_south_north_murders['Week_number'] = brooklyn_south_north_murders['Start_date'].dt.isocalendar().week
# brooklyn_north_murders['Week_number'] = brooklyn_north_murders['Start_date'].dt.isocalendar().week

#Group Summer data from 2023 by crime and sum up
df_brooklyn_summer_all_2023_by_crime = df_brooklyn_summer_all_2023.groupby("Crime")["Current_total"].sum().reset_index()
df_brooklyn_summer_all_2023_by_crime_total_sum = df_brooklyn_summer_all_2023_by_crime['Current_total'].sum()
df_brooklyn_summer_all_2023_by_crime_new_row = pd.DataFrame({'Crime': ["Total"], 'Current_total': [df_brooklyn_summer_all_2023_by_crime_total_sum]})
df_brooklyn_summer_all_2023_by_crime_with_total = pd.concat([df_brooklyn_summer_all_2023_by_crime, df_brooklyn_summer_all_2023_by_crime_new_row])
df_brooklyn_summer_all_2023_by_crime_with_total["Current_total_percent"] = df_brooklyn_summer_all_2023_by_crime_with_total["Current_total"]/df_brooklyn_summer_all_2023_by_crime_total_sum*100

#Group Winter data from 2023 by crime and sum up
df_brooklyn_winter_all_2023_by_crime = df_brooklyn_winter_all_2023.groupby("Crime")["Current_total"].sum().reset_index()
df_brooklyn_winter_all_2023_by_crime_total_sum = df_brooklyn_winter_all_2023_by_crime['Current_total'].sum()
df_brooklyn_winter_all_2023_by_crime_new_row = pd.DataFrame({'Crime': ["Total"], 'Current_total': [df_brooklyn_winter_all_2023_by_crime_total_sum]})
df_brooklyn_winter_all_2023_by_crime_with_total = pd.concat([df_brooklyn_winter_all_2023_by_crime, df_brooklyn_winter_all_2023_by_crime_new_row])
df_brooklyn_winter_all_2023_by_crime_with_total["Current_total_percent"] = df_brooklyn_winter_all_2023_by_crime_with_total["Current_total"]/df_brooklyn_winter_all_2023_by_crime_total_sum*100

#Group Summer data from 2022 by crime and sum up
df_brooklyn_summer_all_2022_by_crime = df_brooklyn_summer_all_2022.groupby("Crime")["Current_total"].sum().reset_index()
df_brooklyn_summer_all_2022_by_crime_total_sum = df_brooklyn_summer_all_2022_by_crime['Current_total'].sum()
df_brooklyn_summer_all_2022_by_crime_new_row = pd.DataFrame({'Crime': ["Total"], 'Current_total': [df_brooklyn_summer_all_2022_by_crime_total_sum]})
df_brooklyn_summer_all_2022_by_crime_with_total = pd.concat([df_brooklyn_summer_all_2022_by_crime, df_brooklyn_summer_all_2022_by_crime_new_row])
df_brooklyn_summer_all_2022_by_crime_with_total["Current_total_percent"] = df_brooklyn_summer_all_2022_by_crime_with_total["Current_total"]/df_brooklyn_summer_all_2022_by_crime_total_sum*100

#Group Winter data from 2022 by crime and sum up
df_brooklyn_winter_all_2022_by_crime = df_brooklyn_winter_all_2022.groupby("Crime")["Current_total"].sum().reset_index()
df_brooklyn_winter_all_2022_by_crime_total_sum = df_brooklyn_winter_all_2022_by_crime['Current_total'].sum()
df_brooklyn_winter_all_2022_by_crime_new_row = pd.DataFrame({'Crime': ["Total"], 'Current_total': [df_brooklyn_winter_all_2022_by_crime_total_sum]})
df_brooklyn_winter_all_2022_by_crime_with_total = pd.concat([df_brooklyn_winter_all_2022_by_crime, df_brooklyn_winter_all_2022_by_crime_new_row])
df_brooklyn_winter_all_2022_by_crime_with_total["Current_total_percent"] = df_brooklyn_winter_all_2022_by_crime_with_total["Current_total"]/df_brooklyn_winter_all_2022_by_crime_total_sum*100

#Merge Summer and Winter from 2023 data into one dataframe and convert into CSV
df_brooklyn_summer_winter_all_2023_by_crime_with_total = pd.merge(df_brooklyn_summer_all_2023_by_crime_with_total,df_brooklyn_winter_all_2023_by_crime_with_total, on="Crime")
#Merge Summer and Winter from 2022 data into one dataframe and convert into CSV
df_brooklyn_summer_winter_all_2022_by_crime_with_total = pd.merge(df_brooklyn_summer_all_2022_by_crime_with_total,df_brooklyn_winter_all_2022_by_crime_with_total, on="Crime")
df_brooklyn_summer_winter_all_2022_2023_by_crime_with_total = pd.merge(df_brooklyn_summer_winter_all_2022_by_crime_with_total,df_brooklyn_summer_winter_all_2023_by_crime_with_total,on="Crime")

# df_brooklyn_summer_winter_all_2022_2023_by_crime_with_total.to_csv("/Users/medermamutov/Desktop/df_brooklyn_summer_winter_all_2022_2023_by_crime_with_total.csv",index = False)
df_brooklyn_summer_winter_all_2022_2023_by_crime_with_total_sorted = df_brooklyn_summer_winter_all_2022_2023_by_crime_with_total.sort_values(by="Current_total_x_x",ascending=False)
df_brooklyn_summer_winter_all_2022_2023_by_crime_with_total_sorted = df_brooklyn_summer_winter_all_2022_2023_by_crime_with_total_sorted[df_brooklyn_summer_winter_all_2022_2023_by_crime_with_total_sorted["Crime"]!="Total"]
df_brooklyn_summer_winter_all_2022_2023_by_crime_with_total_sorted = df_brooklyn_summer_winter_all_2022_2023_by_crime_with_total_sorted.rename(columns = {"Current_total_x_x":"Summer 2022", "Current_total_y_x":"Winter 2022","Current_total_x_y":"Summer 2023","Current_total_y_y":"Winter 2023"})

#plot bar chart summer 2022 vs winter 2022, all types of crimes

# ax = df_brooklyn_summer_winter_all_2022_2023_by_crime_with_total_sorted[['Summer 2022', 'Winter 2022']].plot(
#     kind='bar',
#     title="Crime in Summer vs Winter",
#     figsize=(15, 10),
#     legend=True,
#     fontsize=12
# )
# ax.set_xticklabels(df_brooklyn_summer_winter_all_2022_2023_by_crime_with_total_sorted["Crime"])
# plt.ylabel('Number of crime commited')
# plt.xlabel('Type of crime')
# plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.5, wspace=0.4, hspace=0.4)
# plt.show()

# Turn Dataframe Brooklyn into CSV file - main file with data
# df_brooklyn.to_csv("/Users/medermamutov/Desktop/df_brooklyn.csv",index = False)

# y values - Start DAta
# x values - Burglary, Petit, Grand, Robbery

#plot line chart for Brooklyn to compare Burglary, Petit, Grand, Robbery
theft = ["Burglary", "Gr. Larceny", "Petit Larceny", "Robbery"]
df_brooklyn_theft_filtered = df_brooklyn[df_brooklyn["Crime"].isin(theft)]
df_brooklyn_theft = df_brooklyn_theft_filtered[["Crime","Start_date","Current_total"]].sort_values(by="Start_date",ascending=False)

df_brooklyn_theft_pivot = df_brooklyn_theft.pivot(index="Start_date", columns="Crime", values="Current_total")
# df_brooklyn_theft_pivot.plot(kind = "line",figsize=(10,6))
# plt.grid(True)
# plt.show()

# df_brooklyn_theft.to_csv("/Users/medermamutov/Desktop/df_brooklyn_theft.csv",index = False)


#create a dashboard using Dash
# app = dash.Dash(__name__)
# app.layout = html.Div([
#     dcc.Dropdown(
#         id='crime-dropdown',
#         options=[{'label': crime, 'value': crime} for crime in df_brooklyn_theft['Crime'].unique()],
#         value=df_brooklyn_theft['Crime'].unique(),
#         multi=True
#     ),
#     dcc.Graph(id='line-chart')
# ])
#
# @app.callback(
#     Output('line-chart', 'figure'),
#     Input('crime-dropdown', 'value')
# )
#
# def update_line_chart(selected_crimes):
#     filtered_df = df_brooklyn_theft[df_brooklyn_theft['Crime'].isin(selected_crimes)]
#     color_sequence = ['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A', '#19D3F3', '#FF6692', '#B6E880']
#     fig = px.line(filtered_df, x='Start_date', y='Current_total', color='Crime', title='Crime Totals Over Time',color_discrete_sequence=color_sequence)
#     return fig
#
# if __name__ == '__main__':
#     app.run_server(debug=True)

#create a dashboard using Streamlit
# st.title('Theft Data Dashboard')
# crimes = st.multiselect('Select crimes:', options=df['Crime'].unique(), default=df_brooklyn_theft['Crime'].unique())
# filtered_df = df_brooklyn_theft[df_brooklyn_theft['Crime'].isin(crimes)]
# fig = px.line(filtered_df, x='Start_date', y='Current_total', color='Crime', title='Theft Total Over Time')
# st.plotly_chart(fig)

df_brooklyn_sorted = df_brooklyn.sort_values(by="Start_date", ascending=False)

#create a dashboard 2 using Dash
app2 = dash.Dash(__name__)
app2.layout = html.Div([
    html.H1("Brooklyn Crime Dashboard", style={'textAlign': 'center', 'color': 'white'}),
    html.Div([
    html.Label('Select Crime Type(s):', style={'color': 'white'}),
    dcc.Dropdown(
        id='crime-dropdown',
        options=[{'label': crime, 'value': crime} for crime in df_brooklyn_sorted['Crime'].unique()],
        value=df_brooklyn_sorted['Crime'].unique(),
        multi=True
    ),
    html.Label('Select Start Date:'),
    dcc.Dropdown(
        id='start-date-dropdown',
        options=[{'label': date, 'value': date} for date in df_brooklyn_sorted['Start_date'].dt.strftime('%Y-%m-%d').unique()],
        value=df_brooklyn_sorted['Start_date'].dt.strftime('%Y-%m-%d').min(),
        clearable=False
    ),
    html.Label('Select End Date:', style={'color': 'white'}),
    dcc.Dropdown(
        id='end-date-dropdown',
        options=[{'label': date, 'value': date} for date in df_brooklyn_sorted['Start_date'].dt.strftime('%Y-%m-%d').unique()],
        value=df_brooklyn_sorted['Start_date'].dt.strftime('%Y-%m-%d').max(),
        clearable=False),
],style={'backgroundColor': 'black', 'padding': '10px'}),
    dcc.Graph(id='line-chart'),
    dcc.Graph(id='bar-chart')
])

@app2.callback(
    [Output('line-chart', 'figure'),
     Output('bar-chart', 'figure')],
    [Input('crime-dropdown', 'value'),
    Input('start-date-dropdown', 'value'),
    Input('end-date-dropdown', 'value')]
)

def update_line_chart(selected_crimes,start_date, end_date):
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)
    filtered_df_2 = df_brooklyn_sorted[
        (df_brooklyn_sorted['Crime'].isin(selected_crimes)) &
        (df_brooklyn_sorted['Start_date'] >= start_date) &
        (df_brooklyn_sorted['Start_date'] <= end_date)
         ]
    # crime_counts = filtered_df_2.groupby('Crime')['Current_total'].sum().reset_index()
    # treemap_fig = px.treemap(filtered_df_2, path=['Crime', 'Start_date'], values='Current_total', title='Crime Distribution Hierarchy')

    filtered_df_2 = filtered_df_2[filtered_df_2['Current_total'] != 0]

    treemap_fig = px.treemap(
        filtered_df_2,
        path=['Crime', 'Start_date'],
        values='Current_total',
        title='Crime Distribution Hierarchy',
        color='Current_total',  # Color by the total number of crimes

        hover_data={'Crime': True, 'Start_date': True, 'Current_total': True},  # Customize hover data
        labels={'Current_total': 'Total Crimes'},  # Custom label for values
        branchvalues='total',  # Each branch's value is the total of its children
        color_continuous_scale=[
            (0.0, "rgb(165,0,38)"),  # Dark red
            (0.1111111111111111, "rgb(215,48,39)"),
            (0.2222222222222222, "rgb(244,109,67)"),
            (0.3333333333333333, "rgb(253,174,97)"),
            (0.4444444444444444, "rgb(254,224,144)"),
            (0.5555555555555556, "rgb(224,243,248)"),
            (0.6666666666666666, "rgb(171,217,233)"),
            (0.7777777777777778, "rgb(116,173,209)"),
            (0.8888888888888888, "rgb(69,117,180)"),
            (1.0, "rgb(49,54,149)")]  # Dark blue
    )

    treemap_fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))

    color_sequence = ['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A', '#19D3F3', '#FF6692', '#B6E880']
    fig = px.line(filtered_df_2, x='Start_date', y='Current_total', color='Crime', title='Crime in Brooklyn',color_discrete_sequence=color_sequence)


    return fig,treemap_fig


if __name__ == '__main__':
    app2.run_server(debug=True)

app2 = dash.Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])

app2.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/brPBPO.css'
})

app2.layout = html.Div([
    # Your existing layout code
], style={'backgroundColor': 'black'})

app2.py
