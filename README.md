# NumberPlateGen

[![CI](https://github.com/incyi/NumberPlateGen/actions/workflows/ci.yml/badge.svg)](https://github.com/incyi/NumberPlateGen/actions/workflows/ci.yml)

**NumberPlateGen** is a Python application designed to generate random car number plates from various regions around the world. Currently, it supports Dutch (NL) number plates, with plans to extend support for other regions in the future.

## Features

- Generate random number plates in multiple formats.
- Easily extendable to include number plate formats from various countries.
- Command-line interface (CLI) for easy usage.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Supported Formats](#supported-formats)
- [Contributing](#contributing)
- [License](#license)

## Installation

To install NumberPlateGen, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/NumberPlateGen.git
   cd NumberPlateGen
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On macOS/Linux
   .venv\Scripts\activate     # On Windows
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To generate random number plates using the command line interface, run the following command:

```bash
python scripts/cli.py --region nl --number 1
```

### Parameters

- `--region`: Specify the region for the number plate format (e.g., `nl` for the Netherlands).
- `--number`: Specify how many number plates to generate.

## Supported Formats

Currently, NumberPlateGen supports the following Dutch number plate formats:

- **99-XX-XX**
- **99-XXX-9**
- **9-XXX-99**
- **XX-999-X**
- **X-999-XX**
- **XXX-99-X**

## Contributing

Contributions are welcome! If you'd like to contribute to NumberPlateGen, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

4. Save the file.

This `README.md` provides a clear overview of your project and instructions for users to get started. Let me know if you need any further adjustments or additional sections!
