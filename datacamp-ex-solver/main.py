from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import pyperclip

def generate_code(prompt):
    model_name = "Salesforce/codegen-350M-mono"  # You can change this to other models
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    inputs = tokenizer(f"{prompt}", return_tensors="pt")
    with torch.no_grad():
        generated_ids = model.generate(**inputs, max_length=150, num_return_sequences=1, temperature=0.7)
    
    generated_code = tokenizer.decode(generated_ids[0], skip_special_tokens=True)
    return generated_code

def main():
    prompt = input("Enter your coding task description: \n")
    try:
        generated_code = generate_code(prompt)
        print("\nGenerated Code:\n", generated_code)
        
        copy_to_clipboard = input("Want to copy the code to clipboard? (y/n): ").lower()
        if copy_to_clipboard == 'y':
            pyperclip.copy(generated_code)
            print("Code copied to clipboard!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()