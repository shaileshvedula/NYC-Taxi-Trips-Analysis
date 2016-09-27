library('ggplot2')
library('ggmap')
jfk_day=read.csv('mean_time_day_jfk.csv',header=T)
jfk_day$pickup_day=factor(jfk_day$pickup_day,
  levels=c('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'))
jfk_day=jfk_day[order(jfk_day$pickup_day),]

graph1=ggplot(jfk_day,aes(pickup_day,mean_time))+
  geom_bar(stat='identity',width=0.9)+
  ggtitle('Average time to reach JFK international airport')+
  labs(x='Day',y='Average time taken in minutes')+
  theme(axis.text.x=element_text(angle=60,vjust=0.5))
print (graph1)
#####################################################
jfk_hour=read.csv('mean_time_hour_jfk.csv',header=T)
jfk_hour=jfk_hour[order(jfk_hour$pickup_hour),]

graph2=ggplot(jfk_hour,aes(pickup_hour,mean_time))+
  geom_line()+
  ggtitle('Average time to reach JFK international airport')+
  labs(x='Pickup hour in 24 hour format',y='Average time taken in minutes')+
  theme(axis.text.x=element_text(vjust=0.5))
print (graph2)
#####################################################
newark_day=read.csv('mean_time_day_newark.csv',header=T)
newark_day$pickup_day=factor(newark_day$pickup_day,
                          levels=c('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'))
newark_day=newark_day[order(newark_day$pickup_day),]

graph3=ggplot(newark_day,aes(pickup_day,mean_time))+
  geom_bar(stat='identity',width=0.9)+
  ggtitle('Average time to reach Newark airport')+
  labs(x='Day',y='Average time taken in minutes')+
  theme(axis.text.x=element_text(angle=60,vjust=0.5))
print (graph3)
###########################################################
newark_hour=read.csv('mean_time_hour_newark.csv',header=T)
newark_data1=newark_hour[newark_hour$pickup_hour==22,]

graph4=ggplot(newark_hour,aes(pickup_hour,mean_time))+
  geom_line(stat='identity')+
  ggtitle('Average time to reach Newark airport')+
  labs(x='Pickup hour in 24 hour format',y='Average time taken in minutes')+
  theme(axis.text.x=element_text(vjust=0.5))
print (graph4)
###########################################################
latenight_data=read.csv('latenight_tripdata.csv',header=T)
latenight_data=latenight_data[order(latenight_data$pickup_hour),]

nyc=get_map(location = 'New York City', zoom = 13,source='google')
ggmap(nyc)+geom_density2d(data =latenight_data, aes(x=pickup_longitude, 
      y = pickup_latitude),size=0.3) +
      stat_density2d(data = latenight_data, 
      aes(x =pickup_longitude, y = pickup_latitude, 
      fill = ..level.., alpha = ..level..), size = 0.05,bins = 20, geom = "polygon")+
      scale_fill_gradient(low = "yellow", high = "red")+
      scale_alpha(range = c(0, 0.5), guide = FALSE)+
      labs(y ='Latitude', x ='Longitude')+
      ggtitle('Pickup Activity between 10 PM - 5 AM ')
##########################################################
tips=read.csv('tip.csv',header=T)
tips=subset(tips,(payment_type==1 | payment_type==2))
data1=subset(tips,fare_amount>=1 & fare_amount<10)

graph6=ggplot(data1,aes(fare_amount,tip_amount))+
       stat_binhex()+geom_smooth(method=lm,se=F,color='green')+
       ggtitle('Tpping Trend')+labs(x='Fare amount in Dollars', y='Tip amount')+
       theme(axis.text.x=element_text(vjust=0.5))+facet_wrap(~payment_type)
print (graph6)

data2=subset(tips,fare_amount>=10 & fare_amount<20)

graph61=ggplot(data2,aes(fare_amount,tip_amount))+
  stat_binhex()+geom_smooth(method=lm,se=F,color='green')+
  ggtitle('Tpping Trend')+labs(x='Fare amount in Dollars', y='Tip amount')+
  theme(axis.text.x=element_text(vjust=0.5))+facet_wrap(~payment_type)
print (graph61)

data3=subset(tips,fare_amount>=20 & tip_amount<600)

graph62=ggplot(data3,aes(fare_amount,tip_amount))+
  stat_binhex()+geom_smooth(method=lm,se=F,color='green')+
  ggtitle('Tpping Trend')+labs(x='Fare amount in Dollars', y='Tip amount')+
  theme(axis.text.x=element_text(vjust=0.5))+facet_wrap(~payment_type)
print (graph62)
##########################################################
goldman=read.csv('goldman_sachs.csv',header=T)

graph7=ggplot(goldman,aes(dropoff_hour,total_dropoffs))+
  geom_bar(stat='identity',width=0.95)+
  ggtitle('Total number of dropoffs at Goldman Sachs')+
  labs(x='Dropoff hour',y='Total number of dropoffs')+
  theme(axis.text.x=element_text(angle=60,vjust=0.5))
print (graph7)
