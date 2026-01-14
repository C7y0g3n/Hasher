import argparse
import sys
import time
import os
import hashlib

class Hasher:
    def __init__(self, wordlist_path, hash_string):
        self.wordlist_path = wordlist_path
        self.hash_string = hash_string

    def hashing(self):
        if os.path.exists(self.wordlist_path):
            start = time.time()
            print(f"[+] Starting Hashing at {start}")
            
            try:
                with open(self.wordlist_path, 'r', encoding='utf-8', errors='ignore') as wordlist:
                    for word in wordlist:
                        word = word.strip()
                        # Encode word, hash it, and digest
                        if hashlib.md5(word.encode()).hexdigest() == self.hash_string:
                            print(f"[+] Found Password: {word}")
                            end = time.time()
                            print(f"[+] Time taken: {end - start:.4f} seconds")
                            return True
            except Exception as e:
                print(f"[-] Error reading wordlist: {e}")
                return False

            print(f"[-] Password not found in wordlist")
            end = time.time()
            print(f"[+] Time taken: {end - start:.4f} seconds")
            return False
        else:
            print(f"[-] Wordlist file not found: {self.wordlist_path}")
            return False

def main():
    parser = argparse.ArgumentParser(description='Hasher - A tool for de-hashing passwords by brute force.')
    parser.add_argument('-w', '--wordlist', required=True, help='Wordlist file path')
    # Changed -h to -H to avoid conflict with --help, and renamed variable for clarity
    parser.add_argument('-H', '--hash', required=True, help='Target hash string OR file path containing the hash')
    
    args = parser.parse_args()

    # Logic to handle if user provided a file path for the hash instead of the hash string itself
    target_hash = args.hash
    if os.path.exists(target_hash):
        try:
            with open(target_hash, 'r') as f:
                target_hash = f.read().strip()
                print(f"[+] Read hash from file: {target_hash}")
        except Exception as e:
            print(f"[-] Error reading hash file: {e}")
            sys.exit(1)
            
    hasher = Hasher(args.wordlist, target_hash)
    hasher.hashing()

if __name__ == "__main__":
    main()
