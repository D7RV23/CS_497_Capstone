from datasets import load_dataset
import random
import json
import os

# Global Variables
SEED = 1987
SAMPLES_PER_CLASS = 1
OUTPUT_DIR = "data"
# Saves the samples as local json files, does it through the json library rather than by hand
def genJson(fileName, sampleId, label,text):
    with open(fileName,'w',encoding='utf8') as f:
        json.dump(
            {"Sample": sampleId, "Label": label, "Text": text},
            f, ensure_ascii=False,indent=2
        )

def main():
    # Setting Seed for randomization
    random.seed(SEED)
    # Setting up path for storing samples // is in the .git
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Number of samples obtained
    sample_number = SAMPLES_PER_CLASS
    # Used for obraing the samples from Huggin Face
    dataset = load_dataset("ealvaradob/phishing-dataset", "texts", trust_remote_code=True)

        # Collect all samples and separate by label
    all_samples = []
    for split in dataset.keys():
        all_samples.extend(dataset[split])

    # Separate genuine (label 0) and phishing (label 1) emails
    genuine_samples = [sample for sample in all_samples if sample['label'] == 0]
    phishing_samples = [sample for sample in all_samples if sample['label'] == 1]

    # Check if we have enough samples
    print(f"Available genuine samples: {len(genuine_samples)}")
    print(f"Available phishing samples: {len(phishing_samples)}")

    # Select random samples from each category
    if len(genuine_samples) >= sample_number:
        selected_genuine = random.sample(genuine_samples, sample_number)
    else:
        print(f"Warning: Only {len(genuine_samples)} genuine samples available, using all of them")
        selected_genuine = genuine_samples

    if len(phishing_samples) >= sample_number:
        selected_phishing = random.sample(phishing_samples, sample_number)
    else:
        print(f"Warning: Only {len(phishing_samples)} phishing samples available, using all of them")
        selected_phishing = phishing_samples

    # Saving and formatting the samples in json format(needed for piping into llm's)
    # Save genuine samples 
    print("Saving genuine email samples...")
    for i, sample in enumerate(selected_genuine, 1):
        filename = f"g-hf-{i:04d}.json"
        genJson(os.path.join(OUTPUT_DIR,filename), f"g-hf-{i:04d}", "Legitimate", sample['text'])
        print(f"Saved {filename}")
        
    # Saving Phishing samples
    print("\nSaving phishing email samples...")
    for i, sample in enumerate(selected_phishing, 1):
        filename = f"p-hf-{i:04d}.json"
        genJson(os.path.join(OUTPUT_DIR,filename), f"g-hf-{i:04d}", "Phishing", sample['text'])
        print(f"Saved {filename}")
        
    # Terminal Output configrming samples where extracted
    print(f"\nCreated {len(selected_genuine)} genuine and {len(selected_phishing)} phishing email files.")


if __name__ == "__main__":
    main()
