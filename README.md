# Cisco Type 7 Password Decoder (Educational Tool)

This project is a Python-based utility for decoding Cisco Type 7 encrypted passwords.

Cisco Type 7 is a reversible obfuscation algorithm used in Cisco configurations (not true encryption). This tool demonstrates how the decoding process works.

---

## Disclaimer

This tool is intended strictly for:

- Educational purposes  
- Cybersecurity learning and research  
- Authorized penetration testing in lab environments  

**Do not use this tool on systems without explicit permission.**

---

## Purpose

Cisco Type 7 passwords are commonly found in Cisco configuration files. They are often used for legacy compatibility and are considered insecure because they can be easily decoded.

This project helps:

- Understand how Cisco Type 7 obfuscation works  
- Demonstrate password recovery techniques  
- Learn about weak cryptographic practices in legacy systems  

---

## How It Works

Cisco Type 7 uses a simple XOR-based algorithm combined with a static key.

- The encoded password contains:
  - A 2-digit offset (salt)
  - A sequence of hexadecimal values
- Each byte is XORed with a predefined key to recover the original password

---

## Requirements

- Python 3.x

No external dependencies required.

---

## Usage

```bash id="c7usage1"
python3 cisco7-decrypt.py Cisco-Type7-Hash
```

## Example
- Input
```bash
python3 cisco7-decrypt.py 0242114B0E143F015F5D1E161713
```

- Output
```bash
$uperP@ssword
```
