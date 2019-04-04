import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

print('gspread is imported')
#print(dir(oauth2client))
scope = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('/Users/sumon/PycharmProjects/LinkedIn_Practice/ClientSecret.json',scope)
client = gspread.authorize(credentials)
sheet = client.open('test').sheet1
#sheet.update_cell(1,1,'test1nas')
#print(sheet.row_values(1))
#print(sheet.get_all_values())
my_data=[[9,21,7],[5,8,9]]
for x,y in enumerate(my_data):
    print(x,y)
    print('xy is done now')
    for col_index,z in enumerate(y):
        print(col_index,z)
        sheet.update_cell(x+1,col_index+1,z)