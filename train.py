import json
import re
import random
from datasets import load_dataset

# ==========================================
# CONFIGURATION
# ==========================================
OUTPUT_FILE = "qwen_grpo_math_dataset.jsonl"
MAX_SAMPLES = 5000  # Sweet spot for Colab Free Tier RAM limits

SYSTEM_PROMPT = """You are an expert mathematician and Python developer.
Solve the following math problem by writing a Python script.
Output your thought process inside <think> tags, and your code inside ```python ``` blocks.
The code must print the final numerical answer."""

# ==========================================
# DATA PROCESSING FUNCTIONS
# ==========================================
def extract_pure_number(answer_text):
    """
    GSM8K answers look like: 'First multiply 2 by 3... #### 6'
    This extracts ONLY the '6' to ensure the Python sandbox can perfectly match it.
    """
    # Split by the GSM8K delimiter
    if "####" not in answer_text:
        return None
        
    raw_number = answer_text.split("####")[-1].strip()
    
    # Clean up commas (e.g., "1,000" -> "1000") and any stray punctuation
    clean_number = raw_number.replace(",", "")
    
    # Ensure it's actually a valid number (integer or float)
    try:
        # Check if it parses as a float
        float(clean_number)
        return clean_number
    except ValueError:
        return None

def generate_dataset():
    print("Downloading high-quality math dataset (GSM8K)...")
    # Using the 'main' split which contains high-quality grade school math
    dataset = load_dataset("openai/gsm8k", "main", split="train")
    
    processed_data = []
    dropped_count = 0
    
    print("Purifying ground truths and formatting prompts...")
    for row in dataset:
        question = row["question"]
        raw_answer = row["answer"]
        
        # 1. Extract the strict numeric truth
        ground_truth = extract_pure_number(raw_answer)
        if not ground_truth:
            dropped_count += 1
            continue
            
        # 2. Format for GRPO (System + User prompt array)
        formatted_prompt = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question}
        ]
        
        # 3. Build the final JSON structure
        processed_data.append({
            "prompt": formatted_prompt,
            "answer": ground_truth
        })

    # Shuffle to ensure diverse math problems in the training batch
    random.seed(42)
    random.shuffle(processed_data)
    
    # Truncate to save Colab Memory
    final_dataset = processed_data[:MAX_SAMPLES]
    
    # ==========================================
    # SAVE TO JSONL
    # ==========================================
    print(f"Saving {len(final_dataset)} high-signal samples to {OUTPUT_FILE}...")
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for item in final_dataset:
            f.write(json.dumps(item) + "\n")
            
    print("-" * 40)
    print("✅ Dataset Generation Complete!")
    print(f"Total valid samples: {len(final_dataset)}")
    print(f"Dropped (unparseable) samples: {dropped_count}")
    print(f"File saved as: {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_dataset()
