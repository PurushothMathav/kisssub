import os
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# Decryption Key and IV for .txt1 subtitles
KEY = b'AmSmZVcH93UQUezi'
IV = b'ReBKWW8cqdjPEnF6'

# Folder where your encrypted subtitle files are stored
INPUT_FOLDER = 'subs_encrypted'  # <<< put your folder name here
OUTPUT_FOLDER = 'subs_decrypted'

# Make sure output folder exists
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def decrypt_line(encrypted_line):
    try:
        encrypted_data = base64.b64decode(encrypted_line.strip())
        cipher = AES.new(KEY, AES.MODE_CBC, IV)
        decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
        return decrypted_data.decode('utf-8')
    except Exception as e:
        print(f"Error decrypting line: {e}")
        return ""

def process_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f_in, open(output_path, 'w', encoding='utf-8') as f_out:
        block = []
        for line in f_in:
            line = line.strip()
            if not line:
                f_out.write('\n')
                continue
            if line.isdigit() or "-->" in line:
                # Write subtitle number and timestamp lines as-is
                f_out.write(line + '\n')
            else:
                # Decrypt subtitle content lines
                decrypted = decrypt_line(line)
                f_out.write(decrypted + '\n')

def main():
    for filename in os.listdir(INPUT_FOLDER):
        if filename.endswith('.txt') or filename.endswith('.txt1'):
            input_path = os.path.join(INPUT_FOLDER, filename)
            output_filename = os.path.splitext(filename)[0] + '.srt'
            output_path = os.path.join(OUTPUT_FOLDER, output_filename)
            print(f"Processing: {filename} → {output_filename}")
            process_file(input_path, output_path)

    print("\n✅ All files processed! Decrypted subtitles are in:", OUTPUT_FOLDER)

if __name__ == '__main__':
    main()
