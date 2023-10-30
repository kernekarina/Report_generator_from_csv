import os #get date and time
from datetime import datetime
import pandas as pd #to print tables and manipulate data
import matplotlib.pyplot as plt #to make grafics
import csv #to read csv file
from prettytable import PrettyTable #tables (not sure if it is being used)

from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
from reportlab.graphics.shapes import Drawing, Group, Line, Rect
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.axes import XCategoryAxis, YCategoryAxis
from reportlab.lib import colors

from pathlib import Path
import glob
import dataframe_image as dfi #exporta grafico p imagem
import chardet


data_file='LoRa_TX.csv'
now = datetime.now()
date_str = now.strftime("%Y-%m-%d %H-%M")


header = ["Frequência", "Pot_saida_dBm", "Code_Rate", "SF","BW","Peak_power","Mean_current","Peak_current","VDD"]

#CREATING TABLES TO SEPARATE THE DATA

table_style= (TableStyle([
            #header row style
            ('BACKGROUND', (0, 0), (-1, 0), '#CCCCCC'),
            ('TEXTCOLOR', (0, 0), (-1, 0), '#000000'),
            ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 8),

            #data row style
            ('BACKGROUND', (0, 1), (-1, -1), '#FFFFFF'),
            ('TEXTCOLOR', (0, 1), (-1, -1), '#000000'),
            ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 1), (-1, -1), 6),

        ]))

tab_433_1 = []
with open (data_file,'r') as f:
    reader = csv.reader(f)
    tab_433_1.append(header)
    for row in reader:
        if row[0] == '433000000': # only include rows where the first column equals 433000000
            if row[1] == '14':
                if row[3] == '7':
                    tab_433_1.append(row)

tab_433_2 = []
with open (data_file,'r') as f:
    reader = csv.reader(f)
    tab_433_2.append(header)
    for row in reader:
        if row[0] == '433000000': # only include rows where the first column equals 433000000
            if row[1] == '14':
                if row[3] == '12':
                    tab_433_2.append(row)  

tab_433_3 = []
with open (data_file,'r') as f:
    reader = csv.reader(f)
    tab_433_3.append(header)
    for row in reader:
        if row[0] == '433000000': # only include rows where the first column equals 433000000
            if row[1] == '22':
                if row[3] == '7':
                    tab_433_3.append(row)  

tab_433_4 = []
with open (data_file,'r') as f:
    reader = csv.reader(f)
    tab_433_4.append(header)
    for row in reader:
        if row[0] == '433000000': # only include rows where the first column equals 433000000
            if row[1] == '22':
                if row[3] == '12':
                    tab_433_4.append(row)  

tab_470_1 = []
with open (data_file,'r') as f:
    reader = csv.reader(f)
    tab_470_1.append(header)
    for row in reader:
        if row[0] == '470000000': # only include rows where the first column equals 470000000
            if row[1] == '14':
                if row[3] == '7':
                    tab_470_1.append(row)

tab_470_2 = []
with open (data_file,'r') as f:
    reader = csv.reader(f)
    tab_470_2.append(header)
    for row in reader:
        if row[0] == '470000000': # only include rows where the first column equals 470000000
            if row[1] == '14':
                if row[3] == '12':
                    tab_470_2.append(row)

tab_470_3 = []
with open (data_file,'r') as f:
    reader = csv.reader(f)
    tab_470_3.append(header)
    for row in reader:
        if row[0] == '470000000': # only include rows where the first column equals 470000000
            if row[1] == '22':
                if row[3] == '7':
                    tab_470_3.append(row) 

tab_470_4 = []
with open (data_file,'r') as f:
    reader = csv.reader(f)
    tab_470_4.append(header)
    for row in reader:
        if row[0] == '470000000': # only include rows where the first column equals 470000000
            if row[1] == '22':
                if row[3] == '12':
                    tab_470_4.append(row) 

tab_868_1 = []
with open (data_file,'r') as f:
    reader = csv.reader(f)
    tab_868_1.append(header)
    for row in reader:
        if row[0] == '868000000': # only include rows where the first column equals 868000000
            if row[1] == '14':
                if row[3] == '7':
                    tab_868_1.append(row)

tab_868_2 = []
with open (data_file,'r') as f:
    reader = csv.reader(f)
    tab_868_2.append(header)
    for row in reader:
        if row[0] == '868000000': # only include rows where the first column equals 868000000
            if row[1] == '14':
                if row[3] == '12':
                    tab_868_2.append(row)

tab_868_3 = []
with open (data_file,'r') as f:
    reader = csv.reader(f)
    tab_868_3.append(header)
    for row in reader:
        if row[0] == '868000000': # only include rows where the first column equals 868000000
            if row[1] == '22':
                if row[3] == '7':
                    tab_868_3.append(row)

tab_868_4 = []
with open (data_file,'r') as f:
    reader = csv.reader(f)
    tab_868_4.append(header)
    for row in reader:
        if row[0] == '868000000': # only include rows where the first column equals 868000000
            if row[1] == '22':
                if row[3] == '12':
                    tab_868_4.append(row)

tab_915_1 = []
with open (data_file,'r') as f:
    reader = csv.reader(f)
    tab_915_1.append(header)
    for row in reader:
        if row[0] == '915000000': # only include rows where the first column equals 915000000
            if row [1] == '14':
                if row[3] == '7':
                    tab_915_1.append(row)

tab_915_2 = []
with open (data_file,'r') as f:
    reader = csv.reader(f)
    tab_915_2.append(header)
    for row in reader:
        if row[0] == '915000000': # only include rows where the first column equals 915000000
            if row [1] == '14':
                if row[3] == '12':
                    tab_915_2.append(row) 

tab_915_3 = []
with open (data_file,'r') as f:
    reader = csv.reader(f)
    tab_915_3.append(header)
    for row in reader:
        if row[0] == '915000000': # only include rows where the first column equals 915000000
            if row [1] == '22':
                if row[3] == '7':
                    tab_915_3.append(row)

tab_915_4 = []
with open (data_file,'r') as f:
    reader = csv.reader(f)
    tab_915_4.append(header)
    for row in reader:
        if row[0] == '915000000': # only include rows where the first column equals 915000000
            if row [1] == '22':
                if row[3] == '12':
                    tab_915_4.append(row) 

tab_923_1 = []
with open (data_file,'r') as f:
    reader = csv.reader(f)
    tab_923_1.append(header)
    for row in reader:
        if row[0] == '923000000': # only include rows where the first column equals 923000000
            if row[1] == '14':
                if row [3] == '7':
                    tab_923_1.append(row)

tab_923_2 = []
with open (data_file,'r') as f:
    reader = csv.reader(f)
    tab_923_2.append(header)
    for row in reader:
        if row[0] == '923000000': # only include rows where the first column equals 923000000
            if row[1] == '14':
                if row [3] == '12':
                    tab_923_2.append(row)

tab_923_3 = []
with open (data_file,'r') as f:
    reader = csv.reader(f)
    tab_923_3.append(header)
    for row in reader:
        if row[0] == '923000000': # only include rows where the first column equals 923000000
            if row[1] == '22':
                if row [3] == '7':
                    tab_923_3.append(row)

tab_923_4 = []
with open (data_file,'r') as f:
    reader = csv.reader(f)
    tab_923_4.append(header)
    for row in reader:
        if row[0] == '923000000': # only include rows where the first column equals 923000000
            if row[1] == '22':
                if row [3] == '12':
                    tab_923_4.append(row) 


####### IMPRIMINDO TABELAS NO PDF
filename=f"LoRa_TX_{date_str}.pdf"                
c=canvas.Canvas(filename) #create the pdf
       
#print (tab_433_1)
table = Table (tab_433_1)
table.setStyle(table_style)        
table.wrapOn(c, 0, 700)
table.drawOn(c, 100, 700)
    
#print (tab_433_2)
table = Table (tab_433_2)
table.setStyle(table_style)        
table.wrapOn(c, 0, 600)
table.drawOn(c, 100, 600)
     
#print (tab_433_3)
table = Table (tab_433_3)
table.setStyle(table_style)      
table.wrapOn(c, 0, 500)
table.drawOn(c, 100, 500)
      
#print (tab_433_4)
table = Table (tab_433_4)
table.setStyle(table_style)
table.wrapOn(c, 0, 400)
table.drawOn(c, 100, 400)

#gráfico no pdf


c.showPage() #cria nova página no pdf

#print (tab_470_1)       
table = Table (tab_470_1)
table.setStyle(table_style)
table.wrapOn(c, 0, 700)
table.drawOn(c, 100, 700)

#print (tab_470_2)       
table = Table (tab_470_2)
table.setStyle(table_style)
table.wrapOn(c, 0, 600)
table.drawOn(c, 100, 600)

#print (tab_470_3)       
table = Table (tab_470_3)
table.setStyle(table_style)
table.wrapOn(c, 0, 500)
table.drawOn(c, 100, 500)

#print (tab_470_4)    
table = Table (tab_470_4)
table.setStyle(table_style)
table.wrapOn(c, 0, 400)
table.drawOn(c, 100, 400)

c.showPage()

#print (tab_868_1)
table = Table (tab_868_1)
table.setStyle(table_style)
table.wrapOn(c, 0, 700)
table.drawOn(c, 100, 700)

#print (tab_868_2)
table = Table (tab_868_2)
table.setStyle(table_style)
table.wrapOn(c, 0, 600)
table.drawOn(c, 100, 600)

#print (tab_868_3)        
table = Table (tab_868_3)
table.setStyle(table_style)
table.wrapOn(c, 0, 500)
table.drawOn(c, 100, 500)

#print (tab_868_4)       
table = Table (tab_868_4)
table.setStyle(table_style)
table.wrapOn(c, 0, 400)
table.drawOn(c, 100, 400)

c.showPage()

#print (tab_915_1)       
table = Table (tab_915_1)
table.setStyle(table_style)      
table.wrapOn(c, 0, 700)
table.drawOn(c, 100, 700)

#print (tab_915_2)       
table = Table (tab_915_2)
table.setStyle(table_style)        
table.wrapOn(c, 0, 600)
table.drawOn(c, 100, 600)

#print (tab_915_3)        
table = Table (tab_915_3)
table.setStyle(table_style)        
table.wrapOn(c, 0, 500)
table.drawOn(c, 100, 500)

#print (tab_915_4)       
table = Table (tab_915_4)
table.setStyle(table_style)        
table.wrapOn(c, 0, 400)
table.drawOn(c, 100, 400)

c.showPage()

#print (tab_923_1)      
table = Table (tab_923_1)
table.setStyle(table_style)        
table.wrapOn(c, 0, 700)
table.drawOn(c, 100, 700)

#print (tab_923_2)        
table = Table (tab_923_2)
table.setStyle(table_style)        
table.wrapOn(c, 0, 600)
table.drawOn(c, 100, 600)

#print (tab_923_3)        
table = Table (tab_923_3)
table.setStyle(table_style)        
table.wrapOn(c, 0, 500)
table.drawOn(c, 100, 500)

#print (tab_923_4)
       
table = Table (tab_923_4)
table.setStyle(table_style)        
table.wrapOn(c, 0, 400)
table.drawOn(c, 100, 400)
c.showPage()

c.save()

#montando novamente a tabela, agora com dados organizados

df1=pd.DataFrame(tab_433_1[1:],columns=tab_433_1[0])
df2=pd.DataFrame(tab_433_2[1:],columns=tab_433_2[0])
df3=pd.DataFrame(tab_433_3[1:],columns=tab_433_3[0])
df4=pd.DataFrame(tab_433_4[1:],columns=tab_433_4[0])

df5=pd.DataFrame(tab_470_1[1:],columns=tab_470_1[0])
df6=pd.DataFrame(tab_470_2[1:],columns=tab_470_2[0])
df7=pd.DataFrame(tab_470_3[1:],columns=tab_470_3[0])
df8=pd.DataFrame(tab_470_4[1:],columns=tab_470_4[0])

df9=pd.DataFrame(tab_868_1[1:],columns=tab_868_1[0])
df10=pd.DataFrame(tab_868_2[1:],columns=tab_868_2[0])
df11=pd.DataFrame(tab_868_3[1:],columns=tab_868_3[0])
df12=pd.DataFrame(tab_868_4[1:],columns=tab_868_4[0])

df13=pd.DataFrame(tab_915_1[1:],columns=tab_915_1[0])
df14=pd.DataFrame(tab_915_2[1:],columns=tab_915_2[0])
df15=pd.DataFrame(tab_915_3[1:],columns=tab_915_3[0])
df16=pd.DataFrame(tab_915_4[1:],columns=tab_915_4[0])

df17=pd.DataFrame(tab_923_1[1:],columns=tab_923_1[0])
df18=pd.DataFrame(tab_923_2[1:],columns=tab_923_2[0])
df19=pd.DataFrame(tab_923_3[1:],columns=tab_923_3[0])
df20=pd.DataFrame(tab_923_4[1:],columns=tab_923_4[0])

organized_data = pd.concat([df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13,df14,df15,df16,df17,df18,df19,df20], axis=0)

table_data = [organized_data.columns.tolist()] + organized_data.values.tolist()

#print(table_data)

# Write the table to a CSV file
with open('data_organized.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for row in table_data:
        writer.writerow(row)

##Create folder and file with date and time

#ENTER THE DIRECTORY YOU WANT TO SAVE THE FOLDER

os.chdir('C:\\Users\\ADM_KARINAKERNE\\Desktop\\csv_report')

#CREATE DIRECTORY

os.mkdir(date_str)

#CHANGE DIRECTORY NAME

name_test=f"LoRa_TX_{date_str}"
os.rename(date_str, name_test)


#CHANGING THE NAME OF THE FILE

#old_name = r"C:\Users\ADM_KARINAKERNE\Desktop\csv_report\LoRa_TX.csv"

#new_name = f"C:\\Users\\ADM_KARINAKERNE\Desktop\\csv_report\\LoRa_TX_{date_str}.csv"

#if os.path.isfile(new_name):
#    print  ("the file alredy exists")
#else:

#os.rename(old_name,new_name)

#CURRENT FILE PATH
#escolhi não mudar o LoRa TX de lugar para que seja subrescrito e reuna todos os dados

#file_path = f"C:\\Users\\ADM_KARINAKERNE\\Desktop\\csv_report\\LoRa_TX_{date_str}.csv" 

file_path_pdf = f"C:\\Users\\ADM_KARINAKERNE\\Desktop\\csv_report\\LoRa_TX_{date_str}.pdf"

file_path_organized = f"C:\\Users\\ADM_KARINAKERNE\\Desktop\\csv_report\\data_organized.csv" 

#NEW FOLDER PATH

new_folder_path = f"C:\\Users\\ADM_KARINAKERNE\\Desktop\\csv_report\\LoRa_TX_{date_str}"

#file_name = os.path.basename(file_path) #CSV

file_name_pdf = os.path.basename(file_path_pdf) #PDF

file_name_csv_organized = os.path.basename(file_path_organized) #CSV ORGANIZADO

#new_file_path = os.path.join(new_folder_path, file_name) #CSV

new_file_path_pdf = os.path.join(new_folder_path,file_name_pdf) #PDF

new_file_path_org = os.path.join(new_folder_path,file_name_csv_organized) #csv organ

#os.rename(file_path, new_file_path) #CSV

os.rename(file_path_pdf,new_file_path_pdf) #PDF

os.rename(file_path_organized,new_file_path_org) #csv organiz
