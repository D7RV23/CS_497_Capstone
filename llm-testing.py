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



# would get the items on the data set and number of them total
def get_samples(dataDir="data", samplePerClass = 12):
    list_size = 0
    sample_list = []
    return sample_list, list_size
# Reads the given sample 
# Parses the Json
def read_sample(sample):
    return sampleText
# will look at the sample and prompt a llm to see if its a phishing email or not 
def detect_sample(text):
    is_phishing = 0
    return is_phishing
# Records samples in test file
# Keeps appending untill testing is concluded
def recordDetection():
    return

# Main Function
def main():
    # Create local Ollama client 
    # Requires to run ollama locally or in a reachable server
    client = Client(host=URL, headers={'x-someheader': 'somevalue'})

    # Gets samples from the /data directory
    sampleList,listSize = get_samples()
    Testing = True
    while testing = True:
        # Reads the samples 
        sampleContents = read_sample()
        # Takes the contents fo the given sample and feeds it to the llm
        isPhishing = detect_sample()
        # Records the data and continues the loop
        recordDetection()
        
    print("END OF PROGRAM")
if __name__ == "__main__":
    main()