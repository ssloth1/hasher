#!/usr/bin/env python3

#!/usr/bin/env python3

import hashlib
import sys
import os
import argparse

def get_hash(password, algorithm):
    algorithm = algorithm.lower()
    if algorithm == 'md5':
        return hashlib.md5(password.encode()).hexdigest()
    elif algorithm == 'sha256':
        return hashlib.sha256(password.encode()).hexdigest()
    elif algorithm == 'sha512':
        return hashlib.sha512(password.encode()).hexdigest()
    elif algorithm == 'sha1':
        return hashlib.sha1(password.encode()).hexdigest()
    elif algorithm == 'sha3_256':
        return hashlib.sha3_256(password.encode()).hexdigest()
    elif algorithm == 'sha3_512':
        return hashlib.sha3_512(password.encode()).hexdigest()
    else:
        raise ValueError("Unsupported algorithm. Choose from md5, sha256, sha512, sha1, sha3_256, sha3_512.")

def parse_arguments():
    parser = argparse.ArgumentParser(description='Hashing tool to generate hash values of passwords.')
    parser.add_argument('password', type=str, help='Password to hash or path to file containing the password.')
    parser.add_argument('algorithm', choices=['md5', 'sha256', 'sha512', 'sha1', 'sha3_256', 'sha3_512'],
                        help='The hashing algorithm to use.')
    parser.add_argument('-o', '--output', type=str, help='Output file to save the hash. If not specified, creates a file with a default name.')
    parser.add_argument('-f', '--file', action='store_true', help='Read password from a file instead of the command line.')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose output.')
    return parser.parse_args()

def main():
    args = parse_arguments()

    # Read password from file if -f is provided
    if args.file:
        try:
            with open(args.password, 'r') as file:
                password = file.read().strip()
        except FileNotFoundError:
            print(f"Error: File {args.password} not found.")
            sys.exit(1)
    else:
        password = args.password

    hash_result = get_hash(password, args.algorithm)

    output_file = args.output if args.output else f"hash{next(i for i in range(1000) if not os.path.exists(f'hash{i}.txt'))}.txt"

    with open(output_file, 'w') as file:
        file.write(hash_result)

    if args.verbose:
        print(f"Password: {password}")
        print(f"Algorithm: {args.algorithm}")
        print(f"Hash: {hash_result}")
    print(f"Hash saved in {output_file}")

if __name__ == "__main__":
    main()
