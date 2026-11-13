import math
import os
from ollama import Client

##GLOBAL VARIABLES#

# loopback so we can connect to local models 
# has to be port 11434 as thats what the API uses
URL = 'http://127.0.0.1:11434'
# Model use to detect phishing, can be changed in code 
MODEL = "llama3.2"
# run time in minutes
RUN_TIME = 15
# Sample directory
SAMPLE_DIR = "data"
# Result directory
RESULT_DIR = "results"


# would get the items on the data set and number of them total
def get_samples(dataDir=SAMPLE_DIR, samplePerClass = 12):
    list_size = 0
    sample_list = []
    return sample_list, list_size

# Reads the given sample information
# Parses the Json
def read_sample(sample):
    return sampleName, sampleLabel,sampleText


# will look at the sample and prompt a llm to see if its a phishing email or not 
def detect_sample(text):
    is_phishing = 0
    return is_phishing
# Records samples in test file
# Keeps appending untill testing is concluded
def recordDetection(sampleName, sampleLabel,isPhishing):
    # FORMAT
    # LLM NAME:     TOTAL SAMPLES:  ACCURACY:
    # NAME:     LABEL:   DetectedVal"
    # ...       ...     ...
    return

# Main Function
def main():
    # Creates result directory if not created yet
    os.makedirs(RESULT_DIR, exist_ok= True)
    # Create local Ollama client 
    # Requires to run ollama locally or in a reachable server
    client = Client(host=URL, headers={'x-someheader': 'somevalue'})

    # Gets samples from the /data directory
    sampleList,listSize = get_samples()
    Testing = True
    while Testing == True:
        # Reads the samples 
        sName, sLabel, sText = read_sample()
        # Takes the contents fo the given sample and feeds it to the llm
        is_Phishing = detect_sample(sText)
        # Records the data and continues the loop
        recordDetection(sName,sLabel,is_Phishing)
        
    print("END OF PROGRAM")
if __name__ == "__main__":
    main()