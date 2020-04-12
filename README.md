# Elderly-people-Activity-recognition-using-accelerometer
Elderly-people Activity recognition using accelerometer of mobile phone
Accelerometer data is being collected by the mobile phone and sent to the laptop for further processing using sockets.
Data is taken at 50 Hz for 1 min and then a KNN model is trained with this data whose accuracy comes out to be 99.33%.
Before giving the data to the model it is filtered first as the data recieved by the sensor is very noisy using moving average filter with window size of 50.
The activity it can recognise are "SITTING" ,"WALKING","STANDING" and "SLEEPING".
All the data is taken keeping the mobile phone in the leftside of the front pocket of the denim jeans.
It completely works online too.Client takes the data and send back to the server which is filtered and then passed through the model.
It tells you about what activities were performed for what amount of time during the given time period.

