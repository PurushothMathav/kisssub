# 🔥 Subtitle Decryptor (KissKH / StreamSub)

This project decrypts encrypted `.txt` and `.txt1` subtitle files (from sites like **kisskh.ovh** and **sub.streamsub.top**) and converts them into standard `.srt` subtitle files ready to use in any media player (like VLC, PotPlayer, etc.).

## 📂 Folder Structure

```
your_project/
│
├── subs_encrypted/   # Put your encrypted subtitle files (.txt, .txt1) here
│    ├── file1.txt1
│    ├── file2.txt1
│    └── etc...
│
├── subs_decrypted/   # Decrypted .srt files will be saved here
│
├── decrypt_all_subs.py  # Python script to run
│
├── README.md          # This file
```

## ⚙️ How it Works

- Reads all `.txt` and `.txt1` subtitle files from `subs_encrypted/`.
- Decrypts each subtitle line using AES-128-CBC mode.
- Rebuilds the `.srt` structure (keeping timestamps and numbering).
- Saves the decrypted subtitles to `subs_decrypted/` with `.srt` extension.

## 🚀 How to Use

1. Install the required Python library:

```bash
pip install pycryptodome
```

2. Place your encrypted subtitle files inside the `subs_encrypted/` folder.

3. Run the Python script:

```bash
python decrypt_all_subs.py
```

4. Decrypted `.srt` files will appear inside the `subs_decrypted/` folder.

## 🔑 Decryption Details

- **Key**: `AmSmZVcH93UQUezi`
- **IV**: `ReBKWW8cqdjPEnF6`
- **Encryption Mode**: AES-128-CBC
- **Padding**: PKCS7

## 🛠 Requirements

- Python 3.7+
- pycryptodome

Install dependencies:

```bash
pip install pycryptodome
```

## 📢 Notes

- Designed for `.txt` and `.txt1` subtitle formats used by **kisskh.ovh**.
- Update KEY and IV if site changes in the future.

## ✨ Future Improvements

- Drag & Drop version
- Auto-detect encryption version
- GUI-based decryptor

## 🧡 Credits

- Community contributors and reverse engineers.
- Special thanks to **debakarr** and GitHub discussions.

# 📺 Happy Watching!
