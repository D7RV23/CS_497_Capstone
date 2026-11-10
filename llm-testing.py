import math
from ollama import Client

# loopback so we can connect to local models 
# has to be port 11434 as thats what the API uses
url = 'http://127.0.0.1:11434'
# Model use to detect phishing, can be changed in code 
model = "llama3.2"
# run time in minutes
run_time = 15
# would get the items on the data set and number of them total
def get_samples():
    sample_list = []
    return sample_list, list_size
# reads the given sample 
def read_sample(sample):
    return
# will look at the sample and prompt a llm to see if its a phishing email or not 
def detect_sample():
    bool is_phishing =0
    return is_phishing

def main():
    pass

if __name__ == "__main__":
    return main