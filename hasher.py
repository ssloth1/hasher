#!/usr/bin/env python3

import sys
import os
import argparse
import hash_functions as hf

# Function to get the hash of a password using the specified algorithm
def get_hash(password, algorithm, length=None):
    algorithm = algorithm.lower()
    hash_function = getattr(hf, f"hash_{algorithm}", None)
    if hash_function:
        # Special handling for the shake algorithms, which require a length parameter
        if 'shake' in algorithm and length is not None:
            return hash_function(password, length)
        return hash_function(password)
    else:
        raise ValueError("Unsupported algorithm.")

# Function to parse command line arguments
def parse_arguments():
    parser = argparse.ArgumentParser(description='Hashing tool to generate hash values of passwords.')
    parser.add_argument('password', type=str, help='Password to hash or path to file containing the password.')
    parser.add_argument('algorithm', help='The hashing algorithm to use.')
    parser.add_argument('-l', '--length', type=int, help='Length of the hash for shake algorithms.')
    parser.add_argument('-o', '--output', type=str, help='Output file to save the hash.')
    parser.add_argument('-f', '--file', action='store_true', help='Read password from a file instead of the command line.')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose output.')
    return parser.parse_args()

def main():
    args = parse_arguments()
    password = args.password if not args.file else read_password_from_file(args.password)

    # Validate length for shake algorithms
    if 'shake' in args.algorithm.lower():
        if args.length is None or args.length < 1 or args.length > 512:  # Assuming 512 as the upper limit
            print("Error: Valid length must be specified for shake algorithms and be between 1 and 512.")
            sys.exit(1)

    if args.verbose:
        print(f"Hashing using {args.algorithm.upper()} algorithm.")

    hash_result = get_hash(password, args.algorithm, args.length)
    # Generate a unique output filename if one is not provided.
    output_file = args.output if args.output else f"hash_{next(i for i in range(1000) if not os.path.exists(f'hash_{i}.txt'))}.txt"
    
    if args.verbose:
        print(f"Hash length: {len(hash_result)} characters.")
        print(f"Output file: {output_file}")

    with open(output_file, 'w') as file:
        file.write(hash_result)
    print(f"Hash saved in {output_file}")

# Function to read password from a file
def read_password_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        sys.exit(1)

if __name__ == "__main__":
    main()