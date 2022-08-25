#pushing helpbook to snowflake
import openpyxl
import xlrd
import pandas as pd

location=('B:\\DistributorHelpbook.xlsx')
openpyxl.load_workbook('B:\\DistributorHelpbook.xlsx')
df=pd.read_excel(location)
print(df)