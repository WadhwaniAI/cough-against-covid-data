""" Script to prepare the data for further usage. Post approval, you would have
a text file containing 5 download links to the zip files containing the data.

The script does the following,
1. Downloads the zip files from the links.txt file
2. Unzips the zip files to a directory
3. Removes the zip files

To call this script,

    python prepare.py --links_path=links.txt --output_dir=output_dir
"""

import os
import argparse


def parse_args():
    """ Parse arguments """
    parser = argparse.ArgumentParser(description="Prepare the data for further usage.")
    parser.add_argument(
        "--links_path", "-lp", type=str, help="Path to the links.txt file"
    )
    parser.add_argument(
        "--output_dir", "-od", type=str, help="Path to the output directory"
    )
    args = parser.parse_args()

    # if output_dir does not exist, create it
    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)
    return args


def download_files(links_path, output_dir):
    """ Download the files from the links.txt file """
    with open(links_path, "r") as f:
        for i, line in enumerate(f):
            # Only lines with http in the beginning are links,
            # also remove spaces around and in between in each
            # line
            if "http" in line.strip():
                path = os.path.join(output_dir, f"zip{i}.zip")
                os.system(f'wget "{line.strip()}" -O {path} -q --show-progress')


def unzip_files(output_dir):
    """ Unzip the files """
    for f in os.listdir(output_dir):
        if f.endswith(".zip"):
            os.system(f"unzip {f} -d {output_dir}")


def remove_files(output_dir):
    """ Remove the zip files """
    for file in os.listdir(output_dir):
        if file.endswith(".zip"):
            os.remove(os.path.join(output_dir, file))


def main():
    """ Main function """
    args = parse_args()
    download_files(args.links_path, args.output_dir)
    unzip_files(args.output_dir)
    remove_files(args.output_dir)


if __name__ == "__main__":
    main()
