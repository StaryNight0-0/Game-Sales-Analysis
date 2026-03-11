from copyreg import constructor

import pandas as pd
import os
import csv
import numpy as np
import pylab as pl
import seaborn as sns
import matplotlib.pyplot as plt





# Reads Video game sales dataset
with open('vgsales.csv',newline='', encoding = 'utf_8') as salesFile:
    salesReader = pd.read_csv(salesFile)

 # Reads Console Sales dataset
with open('Console_Data.csv',newline='', encoding = 'utf_8') as ConsoleFile:
    ConsoleReader = pd.read_csv(ConsoleFile)

    # Files are closed after the code is executed
# No personal data is used within this project.

# second dataset will be data on consoles
# need to put second dataset here so I can cross-reference in line graphs

    # ALL DATA KEYS RELEVANT TO VGSALES DATASET
Year = salesReader["Year"]
Genre = salesReader["Genre"]
Name = salesReader["Name"]
JPSales = salesReader["JP_Sales"]
EUSales = salesReader["EU_Sales"]
NASales = salesReader["NA_Sales"]
otherSales = salesReader["Other_Sales"]
GlobalSales = salesReader["Global_Sales"]

     #ALL DATA KEYS RELEVANT TO CONSOLE SALES DATASET
ConsoleName  = ConsoleReader["Console Name"]
Type = ConsoleReader["Type"]
Company = ConsoleReader["Company"]
Gen = ConsoleReader["Gen"]
GenYears = ConsoleReader["Gen Years"]
Release = ConsoleReader["Released Year"]
UnitsSold = ConsoleReader["Units sold (million)"]


##########
meanJp = salesReader.groupby("Genre")["JP_Sales"].mean()
meanEU = salesReader.groupby("Genre")["EU_Sales"].mean() #Shows the mean of the sales between genres
meanNA = salesReader.groupby("Genre")["NA_Sales"].mean()
########


#######
top10Consoles = ConsoleReader.sort_values(by="Units sold (million)", ascending=False)[:10] ## Data for top 10 consoles in the dataframe
########

# Stops pandas error throwing about not reading str or object
ConsoleReader.describe(include=["str","object"])

# Generates a table to showcase the sales of Consoles and their respective companies
Console = ConsoleReader.loc[16:26, ["Console Name", "Company", "Units sold (million)"]]
table = Console.to_html()
#print(table)
table_file = open("table.html", "w")
table_file.write(table)
table_file.close()

#calculates correlation coefficient
correlationcoefficient = salesReader[["NA_Sales","EU_Sales","JP_Sales","Other_Sales","Global_Sales"]].corr()


#Produces a colour palette using seaborn cube helix
palette = sns.cubehelix_palette(start=0, rot=0.4, light=0.8, dark = 0.4, n_colors=12)

#Seaborn seems to throw error about hue and legend but not sure how to fix this but doesn't affect the outcome

# A function used to plot the graph for the Japan sales
def jpGrouped(salesReader):

    # Plots a horizontal bar graph showcasing the top genres in Japan by sales.
    # Using seaborn to make it so the bottom is darker than the top
    # Prints graph with a 95 percent confidence interval


    #JPSalesByGenre = salesReader.groupby("Genre")["JP_Sales"].sum().sort_values()
    #sns.barplot( x=JPSalesByGenre.values, y=JPSalesByGenre.index, palette=palette)
    #plt.title("Total Sales by Genre in Japan", fontweight="bold")          #Comment out for total sales

    sns.barplot(data= salesReader, x= "JP_Sales", y="Genre",palette = palette, errorbar= ('ci', 95))
    plt.title("Mean Sales by Genre in Japan (CI = 95%)", fontweight="bold")
    plt.xlabel("Sales in Millions (Mean)", fontweight="bold")
    pl.ylabel("Genre", fontweight="bold")
    plt.tight_layout()
    pl.show()
    ## RolePlaying games dominates this catergory



def euGrouped(salesReader):


    EUSalesByGenre = salesReader.groupby("Genre")["EU_Sales"].sum().sort_values()
    sns.barplot( x=EUSalesByGenre.values, y=EUSalesByGenre.index, palette=palette)
    plt.title("Total Sales by Genre in Europe", fontweight="bold")          #Comment out for total sales

    #sns.barplot(data= salesReader,x=EUSales, y=Genre,palette=palette, errorbar= ('ci', 95))
    #plt.title("Mean Sales by Genre in Europe (CI = 95%)", fontweight="bold")
    plt.xlabel("Sales in Millions (Mean)", fontweight="bold")
    pl.ylabel("Genre", fontweight="bold")
    plt.tight_layout()
    pl.show()


def naGrouped(salesReader):

    #Plots a horizontal graph showcasing the top genres in North America by sales
    #NASalesByGenre = salesReader.groupby("Genre")["NA_Sales"].sum().sort_values()
    #sns.barplot(x=NASalesByGenre.values, y=NASalesByGenre.index, palette=palette)    #Comment out for total sales
    #plt.title("Total Sales by Genre in North America")  # Comment out for total sales


    sns.barplot(data= salesReader, x=NASales, y= Genre,palette=palette, errorbar= ('ci', 95))
    plt.title("Average Sales by Genre in North America (CI = 95%)", fontweight="bold")     # MAY NOT USE DUE TO TOO MANY FIGURES
    plt.xlabel("Sales in Millions", fontweight="bold")
    pl.ylabel("Genre", fontweight="bold")
    plt.tight_layout()
    pl.show()


def otherGrouped(otherSales):
   otherSalesByGenre = otherSales.groupby("Genre")["Other_Sales"].sum()
   otherSalesByGenre = otherSalesByGenre.sort_values(ascending=True)

   sns.barplot(x=otherSalesByGenre.values, y=otherSalesByGenre.index, palette=palette)     #MAY NOT USE
   plt.title("Total Sales by Genre in Other Countries", fontweight="bold")
   plt.xlabel("Sales in Millions", fontweight="bold")
   plt.ylabel("Genre", fontweight="bold")
   plt.tight_layout()
   plt.show()



def linegraphplot(top10Consoles):

    plt.figure(figsize=(10,5))

    sns.scatterplot(data = top10Consoles, x= Release, y = UnitsSold, hue= "Console Name", marker= "o")
    plt.title("Console Sales Over Time", fontweight="bold")
    plt.xlabel("Release Year", fontweight="bold")
    plt.ylabel("Units sold (million)", fontweight="bold")
    plt.legend(title="Console")
    plt.tight_layout()
    plt.show()

## correlation function
def CORRELATION(correlationcoefficient):
    plt.figure(figsize=(10,5))
    sns.heatmap(correlationcoefficient, annot=True, cmap="coolwarm")
    plt.title("Correlation Between Sales", fontweight="bold")
    plt.show()

#Executes the Graph Functions
linegraphplot(top10Consoles)
euGrouped(salesReader)
jpGrouped(salesReader)
otherGrouped(salesReader)
CORRELATION(correlationcoefficient)























#Genre  global units sold and units sold for consoles can be calculated on the linegraph
#Years on the bottom?


# Creates new CSV File
#NewCSV = {
    #'Console Name': ConsoleName,
    #'Company': Company,
    #'Gen Years': #GenYears,
    #'UnitsSold': UnitsSold,
    #'#Year': Year,  # PROBABLY DELETE
    #'Genre': Genre,
    #'JP Sales': JPSales,
    #'EU Sales': EUSales,
    #'NA Sales': NASales,
    #'Other Sales': otherSales,
    #'Global Sales': GlobalSales
#
#df = pd.DataFrame(NewCSV)
#df.to_csv('NewCSV.csv', index=False)
# print("DONE")

#with open('NewCSV.csv', newline='', encoding='utf_8') as CombinedData:
    #CombinedReader = pd.read_csv(CombinedData)

# print(CombinedReader.head())




#roleplaying = new_df[(new_df['Genre'] == "Role-Playing")]
#roleplayingJP = roleplaying.loc[1:100,["JP_Sales"]]
#globalSale = df.loc[1:100,['Global_Sales']]
#year = df.loc[1:100,['Year']]
#yearOrdered = year.sort_values(by=['Year'], ascending=False)
#Years.append(yearOrdered)
#UniqueYears = np.unique(Years)
#print(UniqueYears)
#roleplayingJPArray.append(roleplayingJP)












#print(x)
#print(roleplayingJPArray)
#plt.plot(UniqueYears,jp)
#plt.show()





























