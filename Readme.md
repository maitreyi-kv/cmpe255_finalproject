# Simulator 

![image](https://user-images.githubusercontent.com/98665151/207822960-a0e32030-d912-4f85-b5b0-89832defaca7.png)

1. Register the device with IoT Core (Once the next step is done)

```
cloud beta iot devices create hospital-center-1 \
  --project=$PROJECT_ID \
  --region=$MY_REGION \
  --registry=iotlab-registry \
  --public-key path=rsa_cert.pem,type=rs256
```

2. Run the file `python cloudiot_mqtt_biomech.py`

# Configure IoT Core - Using it for device management

1. Create the IotCore

```
gcloud beta iot registries create iotlab-registry \ –project=$PROJECT_ID \ –region=$MY_REGION \ –event-notification-config=topic=projects/$PROJECT_ID/topics/iotlab
```

![image](https://user-images.githubusercontent.com/98665151/207822428-72d098e5-3cfa-4abb-883e-5bd51f64698e.png)

# Create Pub/Sub - streaming data for real-time analysis
COngfiure a pub/sub like this image
![image](https://user-images.githubusercontent.com/98665151/207823819-66684e90-f01d-4b4d-8a1a-e405a504247a.png)

# Dataflow - to preprocess data
![image](https://user-images.githubusercontent.com/98665151/207823605-da91c1b1-e088-4a02-950b-78ee9e8e0047.png)


# BigQUery - Craete schema and input the columns to be stored
![image](https://user-images.githubusercontent.com/98665151/207824145-671ea948-c9fa-4b20-8f35-c94b322f3e39.png)





# ML model deployment using Cloud Functiosn 
![image](https://user-images.githubusercontent.com/98665151/207823483-69f88224-0494-4ab3-964e-51860008ee5e.png)



# Creating Big Query:

# Data Flow

# Sensor Data big query



Reference:https://timewithai.wordpress.com/2019/07/27/building-an-iot-analytics-pipeline-on-google-cloud-platform-step-by-step/
