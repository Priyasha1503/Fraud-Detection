import pandas as pd
import datetime as dt
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
df=pd.read_csv('data.csv')
'''print(df)
print(df.head())

print(df.columns)
print(df.describe())'''

##Data preparation
#duplicate values in the dataset
'''print(df.duplicated()) #gives boolean output in line 
print(df.duplicated().sum()) #gives number of duplicate values'''
 #Missing values
'''print(df.isnull()) #whole table will be show in boolean
print(df.isnull().sum()) #givess col wise number'''

#shape of the dataset
#print(df.shape)
print(df.nunique())
#print(df.head())
#drop function - to drop the unique values
df.drop(['Merchant_ID','Customer_ID','Transaction_ID'],axis=1,inplace=True)
print(df.columns)   #inplace = true, makes the table chnages permanent like df=df.drop( ....) '''

#DATA CLEANING AND FEATURE ENGINEERING

### spereating two yrs 2023,2024 and anyalse how many frauds took place in each yr etc...
##anaysis is being done here my month and by year

#Converting date column to date time
df['Date']=pd.to_datetime(df['Date'],format = '%d/%m/%y')


#creating a new column Year with the help of Datetime Module , apply it to to Date column

#Extracting the year from the datetime module from the date column
df['Year']=df['Date'].dt.year
print(df.columns)


#creating a month column with the month of transactions

df['Month']=df['Date'].dt.month
print(df.head())


months= {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}

df['Month']=df['Month'].map(months)
#print(df.head())
print(df.columns)

#drop the data column - becuase we have taken year and month from the date column

df.drop(['Date'],axis=1,inplace=True)
df.drop(['Time'],axis=1,inplace=True)
 

df['fraud']=df['fraud'].map({0:'No Fraud',1:'Fraud'})
#print(df['fraud'].value_counts())
print(df['fraud'].value_counts(normalize=True)*100) #gives percentage of fraud and no fraud

#visualise this using seabron libaray

'''visual=sns.countplot(data=df,x='fraud',color='yellow')
print(visual)
print(type(visual))'''

'''sns.countplot(data=df,x='fraud',color='yellow')
plt.show() '''



#create seperate datasets for normal and fraud transactions
df['fraud']=df['fraud'].map({'No Fraud':0,'Fraud':1,'fraud':1,'No fraud':0}) #converting back to 0 and 1

df.columns=df.columns.str.strip() #removes any spaces in the column names
fraud_df=df[df['fraud']==1] #fraud dataset

#df['fraud']=df['fraud'].map({'No Fraud':0,'Fraud':1,'fraud':1,'No fraud':0}) #converting back to 0 and 1
#print("the main dataset values are",df.shape)
#print("the fraud dataset values are",fraud_df.shape)
#print("the number of fraud and normal values in main data frame are(to cross check the values)",df['fraud'].value_counts())
print("new")
#print(df['fraud'].dtype) #what type is the column #output - object
#print(df['fraud'].unique()) #gives unique values in the column
#print(df['fraud'].value_counts())
#print(fraud.nunique()) #gives number of unique values in the fraud dataset

#print(type(df.columns)) #output: <class 'pandas.core.indexes.base.Index'>
#print(type(df.columns.tolist()))  #output: <class 'list'>

  #the problem here is fraud dataset is showing the shape 0,17 , hwere infact it should actually have 155 rows
#this is because in the main dataset the fraud column has 0 and 1 values , but in the fraud dataset it has 0 and 1 as string values

#print(fraud_df.head())

#creating non fraud - normal dataset
#so, extracting normal transactions
normal_df=df[df['fraud']==0]
#print("Shape of normal dataset is (non fraud data):",normal_df.shape)
'''print(fraud_df.columns)
#since date column is not imp, deleting date column in fraud_df
fraud_df.drop(['Date'],axis=1,inplace=True)
print(fraud_df.columns)'''

#check datatypes
#print(fraud_df.dtypes)


#correlation

'''numeric_columns=fraud_df.select_dtypes(include=['int64','int32','float'])
print(numeric_columns.corr()) #gives correlation between numerical columns

sns.pairplot(data=df,hue='fraud',palette='pastel',diag_kind='dist')
plt.show() '''

#visualising different feature basis the fraud occurrences as a subject

#plot 1:Fraud distribution by Transaction type 
vc=fraud_df['Transaction_Type'].value_counts().index
vc.columns=['Transaction_Type','Transaction_Type']
fig=px.bar(vc,x='Transaction_Type',y='Transaction_Type',
           color='Transaction_Type',
           title="Fraud Distribution by Transaction Type",
           labels={'x':'Transaction Type','y':'Count of Transactions'},
           color_discrete_sequence=px.colors.qualitative.Pastel
)

'''fig = px.bar(x=fraud_df['Transaction_Type'].value_counts().index,
             y=fraud_df['Transaction_Type'].value_counts().values,
             color=fraud_df['Transaction_Type'].value_counts().index,
             title="Fraud Distribution by Transaction Type",
             labels={'x':'Transaction Type','y':'Count of Transactions'},
             color_discrete_sequence=px.colors.qualitative.Pastel)'''
fig.update_layout(xaxis={'categoryorder':'total descending'})
fig.show()

