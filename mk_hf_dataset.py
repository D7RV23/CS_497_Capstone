from datasets import load_dataset
import random
import json

def genJson(fileName, sampleId, label,text):

    pass

def main():
    sample_number = 1
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
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("{\n")
            f.write(f'"Sample": "g-hf-{i:04d}",\n')
            f.write('"Label": "Legitimate",\n')
            f.write('"Text": "')
            f.write(sample['text'])
            f.write('"\n}\n')
        print(f"Saved {filename}")
        
    # Saving Phishing samples
    print("\nSaving phishing email samples...")
    for i, sample in enumerate(selected_phishing, 1):
        filename = f"p-hf-{i:04d}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("{\n")
            f.write(f'"Sample": "p-hf-{i:04d}",\n')
            f.write('"Label": "Phishing",\n')
            f.write(f'"Text: "')
            f.write(sample['text'])
            f.write('"\n}\n')
        print(f"Saved {filename}")
        
    # Terminal Output configrming samples where extracted
    print(f"\nCreated {len(selected_genuine)} genuine and {len(selected_phishing)} phishing email files.")


if __name__ == "__main__":
    main()
