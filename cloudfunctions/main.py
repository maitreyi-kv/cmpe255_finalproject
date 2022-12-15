import base64
import pandas as pd
import pickle

# Load the saved model from the file
with open('logreg_model.pkl', 'rb') as f:
    model = pickle.load(f)

def hello_pubsub(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    print(pubsub_message)
    # Use the model for predictions
    predictions = model.predict(pd.DataFrame(pubsub_message))
    print("Preidctions", predictions)