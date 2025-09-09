# Encrypted File Packer

Python-based tool that compresses, encrypts, and repackages source files into self-executing Python scripts. The project combines gzip compression and Fernet symmetric encryption with polymorphic obfuscation techniques, making each packed file unique while preserving functionality.

Key Features:

Compression & Encryption: Uses gzip to compress input files and Fernet encryption with randomly generated keys for secure storage.

Self-Extracting Output: Generates standalone Python files that can automatically decrypt and execute the original source when run.

Polymorphic Obfuscation: Randomizes function aliases, encodings, and import styles to ensure each packed script has a different structure.

Applied Concepts: Demonstrates practical use of cryptography, file systems, data compression, and dynamic code execution.


----------------------------------------------

python main.py load.py -o target.py

python load.py
