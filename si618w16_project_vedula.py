import pandas as pd 
from dateutil import parser
import csv
import re

def jfk_time(pickup_day=[],pickup_hour=[]):
    for i in range(len(jfk.index.tolist())):
        pickup_day.append(parser.parse(jfk.iloc[i,0]).strftime('%A'))
        pickup_hour.append(str(re.search(r'\d+:',jfk.iloc[i,0]).group()).rstrip(':'))

    return(pickup_day,pickup_hour)

def newark_time(pickup_day=[],pickup_hour=[]):
    for i in range(len(newark.index.tolist())):
        pickup_day.append(parser.parse(newark.iloc[i,0]).strftime('%A'))
        pickup_hour.append(str(re.search(r'\d+:',newark.iloc[i,0]).group()).rstrip(':'))

    return(pickup_day,pickup_hour)

def jfk_output(pickup_day,pickup_hour,pickup_datetime,dropoff_datetime):
    time_delta=[]
    for i in range(len(pickup_datetime)):
        start=parser.parse(pickup_datetime.iloc[i])
        end=parser.parse(dropoff_datetime.iloc[i])
        time_delta.append(((end-start).total_seconds())/60.0)
    data1={'pickup_day':pickup_day,'time_delta':time_delta}
    temp1=pd.DataFrame(data=data1)
    data2={'pickup_hour':pickup_hour,'time_delta':time_delta}
    temp2=pd.DataFrame(data=data2)
    
    p={}
    q={}

    grouped_day=temp1.groupby('pickup_day')
    for day, group in grouped_day:
        p[day]=group['time_delta'].mean()
    
    grouped_hour=temp2.groupby('pickup_hour')
    for hour, group in grouped_hour:
        q[hour]=group['time_delta'].mean()
    
    pd.DataFrame(p.items()).to_csv('mean_time_day_jfk.csv',header=['pickup_day','mean_time'])
    pd.DataFrame(q.items()).to_csv('mean_time_hour_jfk.csv',header=['pickup_hour','mean_time'])

    return 0

def newark_output(pickup_day,pickup_hour,pickup_datetime,dropoff_datetime):
    time_delta=[]
    for i in range(len(pickup_datetime)):
        start=parser.parse(pickup_datetime.iloc[i])
        end=parser.parse(dropoff_datetime.iloc[i])
        time_delta.append(((end-start).total_seconds())/60.0)
    data1={'pickup_day':pickup_day,'time_delta':time_delta}
    temp1=pd.DataFrame(data=data1)
    data2={'pickup_hour':pickup_hour,'time_delta':time_delta}
    temp2=pd.DataFrame(data=data2)
    
    p={}
    q={}

    grouped_day=temp1.groupby('pickup_day')
    for day, group in grouped_day:
        p[day]=group['time_delta'].mean()
    
    grouped_hour=temp2.groupby('pickup_hour')
    for hour, group in grouped_hour:
        q[hour]=group['time_delta'].mean()
    
    pd.DataFrame(p.items()).to_csv('mean_time_day_newark.csv',header=['pickup_day','mean_time'])
    pd.DataFrame(q.items()).to_csv('mean_time_hour_newark.csv',header=['pickup_hour','mean_time'])

    return 0

if __name__ == '__main__':
    trip_data=pd.read_csv('yellow_tripdata.csv')
    trip_data.dropna(axis=0,how='any')
    jfk=trip_data[(trip_data['pickup_latitude']<=40.771 ) & \
             (trip_data['pickup_latitude']>=40.753) & \
             (trip_data['RateCodeID']==2)][[1,2]]
    
    print 'jfk read'
   
    ############################################
    newark=trip_data[(trip_data['pickup_latitude']<=40.771 ) & \
             (trip_data['pickup_latitude']>=40.753) & \
             (trip_data['RateCodeID']==3)][[1,2]]
   
    print 'Newark read'
    #############################################
    jfk_pickup_day,jfk_pickup_hour=jfk_time()

    print "Jfk time processed"
    #############################################
    newark_pickup_day,newark_pickup_hour=newark_time()

    print 'Newark time processed'
    #############################################
    jfk_output(jfk_pickup_day,jfk_pickup_hour,jfk['tpep_pickup_datetime'],jfk['tpep_dropoff_datetime'])
    
    print 'jfk output printed'
    #############################################
    newark_output(newark_pickup_day,newark_pickup_hour,newark['tpep_pickup_datetime'],newark['tpep_dropoff_datetime'])
    
    print 'Newark output printed'
    #############################################
    late_night=trip_data[['pickup_latitude','pickup_longitude','tpep_pickup_datetime']]
    #print late_night.head()
    count=0
    with open('latenight_tripdata.csv','w') as csvfile:
        fieldnames=['pickup_latitude','pickup_longitude','pickup_hour']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(len(late_night)):
            if ((parser.parse(late_night.iloc[i,2]).hour>=22) or (parser.parse(late_night.iloc[i,2]).hour<5)):
                writer.writerow({'pickup_latitude': late_night.iloc[i]['pickup_latitude'],\
                               'pickup_longitude': late_night.iloc[i]['pickup_longitude'],\
                               'pickup_hour':str(re.search(r'\d+:',late_night.iloc[i]['tpep_pickup_datetime']).group()).rstrip(':')})
            count+=1
            if count>350000:
                break

    print 'late night trip data printed'
    #############################################
    pd.DataFrame(trip_data[['payment_type','fare_amount','tip_amount']]).to_csv('tip.csv')
    
    print 'tip amount printed'
    #############################################
    data=trip_data[(trip_data['dropoff_latitude']>=40.714886) & \
                  (trip_data['dropoff_latitude']<=40.714916)][['tpep_dropoff_datetime']]
    for i in range(len(data)):
        data.iloc[i,0]= str(re.search(r'\d+:',data.iloc[i,0]).group()).rstrip(':')
    grouped=data.groupby('tpep_dropoff_datetime')
    p={}
    for hour,group in grouped:
        p[hour]=len(group)
    pd.DataFrame(p.items()).to_csv('goldman_sachs.csv',header=['dropoff_hour','total_dropoffs'])

    print 'goldman sachs printed'
















