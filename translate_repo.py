import os
import json
import re
import time
from deep_translator import GoogleTranslator

CHINESE_RE = re.compile(r'[\u4e00-\u9fff]')

def contains_chinese(text):
    return bool(CHINESE_RE.search(text))

def translate_text(text):
    try:
        translator = GoogleTranslator(source='zh-CN', target='en')
        return translator.translate(text)
    except Exception as e:
        print(f"Translation error: {e}")
        return None

def process_file(filepath):
    print(f"Processing: {filepath}")
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    translated_lines = []
    changed = False
    
    for i, line in enumerate(lines):
        if contains_chinese(line):
            leading_whitespace = len(line) - len(line.lstrip())
            prefix = line[:leading_whitespace]
            content = line[leading_whitespace:].rstrip('\n')
            
            if content.strip():
                translated_content = None
                retries = 3
                for attempt in range(retries):
                    translated_content = translate_text(content)
                    if translated_content is not None:
                        break
                    time.sleep(1 + attempt) # Backoff
                
                if translated_content:
                    new_line = prefix + translated_content
                    if line.endswith('\n'):
                        new_line += '\n'
                    translated_lines.append(new_line)
                    changed = True
                    time.sleep(0.05)
                else:
                    print(f"Failed to translate line in {filepath}: {line.strip()}")
                    translated_lines.append(line)
            else:
                translated_lines.append(line)
        else:
            translated_lines.append(line)
            
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(translated_lines)
            
    return True

def main():
    root_dir = r"C:\Users\ishan\Documents\Projects\LeetCodeAnimated"
    checkpoint_file = os.path.join(root_dir, "translation_checkpoint.json")
    
    if os.path.exists(checkpoint_file):
        with open(checkpoint_file, 'r', encoding='utf-8') as f:
            checkpoint = json.load(f)
    else:
        checkpoint = {}
        
    md_files = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # skip .git or other ignored dirs
        if '.git' in dirpath:
            continue
        for filename in filenames:
            if filename.endswith('.md') or filename.endswith('.MD'):
                md_files.append(os.path.join(dirpath, filename))
                
    total = len(md_files)
    print(f"Found {total} markdown files.")
    
    for idx, filepath in enumerate(md_files):
        rel_path = os.path.relpath(filepath, root_dir)
        if checkpoint.get(rel_path):
            continue
            
        success = process_file(filepath)
        if success:
            checkpoint[rel_path] = True
            with open(checkpoint_file, 'w', encoding='utf-8') as f:
                json.dump(checkpoint, f, indent=4)
                
    print("Translation process finished.")

if __name__ == "__main__":
    main()
