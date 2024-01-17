# Hasher

Hasher is a simple yet powerful tool for generating hash values of passwords or other data using various algorithms. It's written in Python and can be easily used in command line interfaces.

## Features

- Supports multiple hashing algorithms including MD5, SHA1, SHA224, SHA256, SHA384, SHA512, SHA3_224, SHA3_256, SHA3_384, SHA3_512, BLAKE2b, BLAKE2s, SHAKE_128, and SHAKE_256.
- Option to read passwords from a file.
- Ability to specify custom output file names.
- Verbose mode for detailed information about the hashing process.

## Installation

To use Hasher, you need to have Python installed on your system. Clone this repository or download the script directly.

```bash
git clone https://github.com/ssloth1/Hasher.git
cd Hasher
chmod +x hasher.py
```

## Usage

To hash a password, run:

```bash
./hasher.py [password] [algorithm]
```

Replace `[password]` with the password you want to hash and `[algorithm]` with the desired algorithm (md5, sha1, sha224, sha256, sha384, sha512, sha3_224, sha3_256, sha3_384, sha3_512, blake2b, blake2s, shake_128, shake_256).

### Optional Flags

- `-l` or `--length`: Specify the length of the hash for SHAKE algorithms.
- `-o` or `--output`: Specify an output file for the hash.
- `-f` or `--file`: Read the password from a file.
- `-v` or `--verbose`: Enable verbose output for detailed process information.

### Examples

```bash
# Hash a password using SHA256
./hasher.py mypassword sha256

# Hash a password using SHAKE_128 with specified length
./hasher.py mypassword shake_128 -l 128

# Read the password from a file and hash using SHA512
./hasher.py password.txt sha512 -f

# Verbose mode for detailed output
./hasher.py mypassword sha1 -v
```

## Contributing

Contributions to Hasher are welcome! Feel free to submit issues or pull requests.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](LICENSE.md) file for details.

