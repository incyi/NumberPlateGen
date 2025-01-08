"""CLI script for generating random number plates.

This script provides a command-line interface for generating random
number plates based on a specified region and number of plates.
"""

import argparse
from numberplategen.generator import generate_number_plate
from numberplategen.formats import supported_formats

def main():
    """Main function to parse CLI arguments and generate number plates."""

    # Create argument parser
    parser = argparse.ArgumentParser(
        description="NumberPlateGen: Generate random license/number plates for various regions."
    )

    # Add arguments
    parser.add_argument(
        "-r", "--region",
        type=str,
        choices=supported_formats.keys(),
        default="us",
        help="Specify the region format (e.g., 'nl', 'tr', 'us', 'uk'). Default is 'us'."
    )
    parser.add_argument(
        "-n", "--number",
        type=int,
        default=3,
        help="Number of plates to generate. Default is 3."
    )

    # Parse arguments
    args = parser.parse_args()

    # Generate and display plates
    for _ in range(args.number):
        print(generate_number_plate(args.region))


if __name__ == "__main__":
    main()
