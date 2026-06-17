import torch
import re
import os
from google.colab import drive
from datasets import load_dataset
from unsloth import FastLanguageModel
from trl import GRPOTrainer, GRPOConfig

# ==========================================
# 0. BULLETPROOF CLOUD STORAGE
# ==========================================
print("Mounting Google Drive to ensure absolute checkpoint safety...")
OUTPUT_DIR = "/content/drive/MyDrive/qwen2.5-math-coder-checkpoints"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ==========================================
# 1. HARDWARE-OPTIMIZED CONFIGURATION (SPEED RUN)
# ==========================================
MAX_SEQ_LENGTH = 1024 
LORA_RANK = 8         # Halved to drastically speed up gradient updates
NUM_GENERATIONS = 2   # Minimal group size for fastest iteration

# ==========================================
# 2. LOAD DATASET & MODEL
# ==========================================
print("Loading high-signal dataset...")
dataset = load_dataset("json", data_files="qwen_grpo_math_dataset.jsonl", split="train")

print("Initializing 4-bit Quantized Model...")
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "unsloth/Qwen2.5-Coder-7B-Instruct-bnb-4bit",
    max_seq_length = MAX_SEQ_LENGTH, 
    load_in_4bit = True,
    fast_inference = False, 
)

print("Injecting LoRA Adapters...")
model = FastLanguageModel.get_peft_model(
    model,
    r = LORA_RANK,
    target_modules = ["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
    lora_alpha = LORA_RANK,
    lora_dropout = 0,
    bias = "none",
    use_gradient_checkpointing = "unsloth",
    random_state = 3407,
)

# ==========================================
# 3. REWARD FUNCTIONS
# ==========================================
def execution_reward(prompts, completions, answer, **kwargs):
    rewards = []
    for response, truth in zip(completions, answer):
        content = response[0]["content"]
        code_match = re.search(r'```python\s*(.*?)\s*```', content, re.DOTALL)
        
        if not code_match:
            rewards.append(0.0)
            continue
            
        code = code_match.group(1).strip()
        local_scope = {}
        
        try:
            wrapped_code = f"import math\noutput_capture = []\nprint = lambda x: output_capture.append(str(x))\n{code}"
            exec(wrapped_code, {}, local_scope)
            
            if any(str(truth) in out for out in local_scope.get("output_capture", [])):
                rewards.append(1.0) 
            else:
                rewards.append(0.1) 
        except Exception:
            rewards.append(0.0) 
            
    return rewards

def format_reward(prompts, completions, **kwargs):
    rewards = []
    for response in completions:
        content = response[0]["content"]
        has_think = "<think>" in content and "</think>" in content
        has_code = "```python" in content and "```" in content
        rewards.append(0.5 if (has_think and has_code) else 0.0)
    return rewards

# ==========================================
# 4. TRAINING LOOP
# ==========================================
print("Configuring GRPO Trainer for Maximum Throughput...")
training_args = GRPOConfig(
    output_dir = OUTPUT_DIR, 
    learning_rate = 5e-6,
    per_device_train_batch_size = 1,
    gradient_accumulation_steps = 4, 
    num_generations = NUM_GENERATIONS,
    max_prompt_length = 256,       
    max_completion_length = 400,   # Shorter completions = much faster generation cycles
    max_steps = 100,               # Truncated total steps for a rapid 2.5 hour finish
    logging_steps = 10,
    save_steps = 25,               # Saving securely to Drive every 25 steps
    fp16 = not torch.cuda.is_bf16_supported(),
    bf16 = torch.cuda.is_bf16_supported(),
    report_to = "none" 
)

trainer = GRPOTrainer(
    model = model,
    processing_class = tokenizer,
    reward_funcs = [execution_reward, format_reward],
    args = training_args,
    train_dataset = dataset,
)

print("Starting Reinforcement Learning loop...")
trainer.train()

# ==========================================
# 5. FINAL EXPORT TO DRIVE
# ==========================================
print("Training complete. Exporting final model to GGUF in Google Drive...")
final_path = "/content/drive/MyDrive/qwen-2.5-math-coder-FINAL-GGUF"
try:
    model.save_pretrained_gguf(final_path, tokenizer, quantization_method = "q4_k_m")
    print(f"✅ SUCCESS! Model safely stored in your Drive at: {final_path}")
except Exception as e:
    print(f"Error during save: {e}.")
