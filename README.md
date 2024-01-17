
# Hasher

Hasher is a simple yet powerful tool for generating hash values of passwords or other data using various algorithms. It's written in Python and can be easily used in command line interfaces.

## Features

- Supports multiple hashing algorithms: MD5, SHA256, SHA512, SHA1, SHA3_256, SHA3_512.
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

Replace `[password]` with the password you want to hash and `[algorithm]` with the desired algorithm (md5, sha256, sha512, sha1, sha3_256, sha3_512).

### Optional Flags

- `-o` or `--output`: Specify an output file for the hash.
- `-f` or `--file`: Read the password from a file.
- `-v` or `--verbose`: Enable verbose output.

### Examples

```bash
# Hash a password using SHA256
./hasher.py mypassword sha256

# Hash a password using SHA256 and save to a specific file
./hasher.py mypassword sha256 -o hash.txt

# Read the password from a file and hash using SHA512
./hasher.py password.txt sha512 -f

# Verbose mode
./hasher.py mypassword sha1 -v
```

## Contributing

Contributions to Hasher are welcome! Feel free to submit issues or pull requests.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](LICENSE.md) file for details.
