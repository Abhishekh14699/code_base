import argparse
import pip

try:
    import pandas as pd
except ImportError:
    pip.main(['install',"pandas"]) 

#Help Doc and parameter extraction
help_string = '''This script allows user to compare xlsx files and write remarks to output xlsx file'''
parser = argparse.ArgumentParser(description=help_string)
parser.add_argument(help="Input Xlsx file from json extraction",dest="xlsx_json")
parser.add_argument(help="Output Xlsx file from xml extraction",dest="xlsx_xml")
parser.add_argument(help="Output Xlsx file",dest="output_file")
args = parser.parse_args()

xlsx_json = args.xlsx_json
xlsx_xml = args.xlsx_xml
output_file = args.output_file

#Reading required data from json
print("Reading excel sheet 1...")
json_fields = ['Features', 'Parameters','Default Value',"Mandatory","Maximum Length","Datatype"]
json_df = pd.read_excel(xlsx_json, sheet_name='Sheet1', usecols=json_fields) 
#json_df["Mandatory"].replace("TRUE","1",inplace=True)
#json_df["Mandatory"].replace("FALSE","0",inplace=True)


#Reading required data from json
print("Reading excel sheet 2...")
xml_fields = ['Features', 'Parameters','Default Value',"Mandatory","Maximum Length","Remarks","Datatype Format"]
xml_df = pd.read_excel(xlsx_xml, sheet_name='Sheet1', usecols=xml_fields)
xml_df = xml_df[xml_df["Remarks"].isna()]
#xml_df["Mandatory"].replace("Yes","1",inplace=True)
#xml_df["Mandatory"].replace("No","0",inplace=True)

#merging both dataframes
print("merging files...")
merged_data = xml_df.merge(json_df,how="left",on=['Features', 'Parameters'],suffixes=["_FE","_BE"])
del merged_data['Remarks']
merged_data = merged_data.fillna(" ")
#print(merged_data)

print("comparing files...")
disc = []
for ind,row in merged_data.iterrows():
    st=[]
    x=""
    y=""
    x1=""
    if(row[2] in ["FinComboBox","FinRadioButtonGroup","FinTextInputWithSearcher","FinTextInput"]):
        x1="string"
    if(row[2] in ["FinDate"]):
        x1 = "date"
    if(row[2] in ["FinAmount"]):
        x1 = "Amount"
    if(row[2] in ["FinInteger","FinNumber","FinPercentage"]):
        x1= "number"
    #print(x1,row[6])
    if(x1!=row[6]):
        st.append("Datatype")
    #print(row[2],row[6])
    if(row[4]=="Yes"):
        x="1"
    elif(row[4]=="No"):
        x="0"
    else:
        x=""
    if(row[8]==1.0):
        y="1"
        row[8] = "TRUE"
    else:
        y=""
        row[8] = ""
    #print(row[3],row[6])
    if(row[3]!=row[7]):
        st.append("Default Value")
    if(row[5]!=row[9]):
        st.append("Maximum Length")
    if(x!=y):
        st.append("Mandatory")
    disc.append(",".join(st))
merged_data["Discrepancies"] = disc

print("Writing data into file...")
merged_data.drop(merged_data[merged_data['Discrepancies'] == ""].index, inplace = True)
writer = pd.ExcelWriter(output_file, engine='xlsxwriter')
pd.DataFrame(merged_data).to_excel(writer,sheet_name='Sheet1',index=False) 
worksheet = writer.sheets['Sheet1']
worksheet.set_column(0, 2, 25)
worksheet.set_column(3, 9, 15)
worksheet.set_column(10, 10, 30)
writer.save()
print("Data writing complete...")