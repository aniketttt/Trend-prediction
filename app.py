import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as data
from keras.models import load_model
import streamlit as st

start = '2020-01-01'
end = '2021-12-31'

st.title('Stock Trend Prediction')

user_input=st.text_input('Enter stock ticker','APPL')
df=data.DataReader(user_input,'yahoo',start,end)

#descriding data
st.subheader('Data from 2020 - 2022')
st.write(df.describe())

#visualizations

st.subheader('Closing price vs Time chart')
fig=plt.figure(figsize=(12,6))
plt.plot(df.Close)
st.pyplot(fig)

st.subheader('Closing price vs Time chart with 50 ma')
ma50=df.Close.rolling(50).mean()
fig=plt.figure(figsize=(12,6))
plt.plot(ma50)
plt.plot(df.Close)
st.pyplot(fig)

st.subheader('Closing price vs Time chart with 50ma & 100ma')
ma50=df.Close.rolling(50).mean()
ma100=df.Close.rolling(100).mean()
fig=plt.figure(figsize=(12,6))
plt.plot(ma50,'r')
plt.plot(ma100,'g')
plt.plot(df.Close,'b')
st.pyplot(fig)

#spliting data training and testing
data_training=pd.DataFrame(df['Close'][0:int(len(df)*0.70)])
data_testing=pd.DataFrame(df['Close'][int(len(df)*0.70): int(len(df))])

from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler(feature_range=(0,1))

data_training_array=scaler.fit_transform(data_training)

#load my momdel

model=load_model('keras_model.h5')

#testing part

past_100_days=data_training.tail(100)
final_df=past_100_days.append(data_testing,ignore_index=True)
input_data=scaler.fit_transform(final_df)

x_test=[]
y_test=[]

for i in range(100,input_data.shape[0]):
    x_test.append(input_data[i-100:i])
    y_test.append(input_data[i,0])

x_test,y_test=np.array(x_test),np.array(y_test)
y_predicted=model.predict(x_test)
scaler=scaler.scale_

scale_factor=1/scaler[0]
y_predicted = y_predicted * scale_factor
y_test = y_test * scale_factor

#final graph
st.subheader('Prediction vs Original')
fig2=plt.figure(figsize=(12,6))
plt.plot(y_test,'b',label='Original Price')
plt.plot(y_predicted,'r',label='Predicted Price')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
st.pyplot(fig2)







