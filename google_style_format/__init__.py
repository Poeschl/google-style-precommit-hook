import os
import subprocess
from argparse import ArgumentParser

import requests

DEFAULT_VERSION = "1.18.1"
DOWNLOAD_URL_TEMPLATE = "https://github.com/google/google-java-format/releases/download/v{version}/google-java-format-{version}-all-deps.jar"


def main(version: str, java_files: list[str]):
    os.makedirs(".cache", exist_ok=True)

    os.chdir(".cache")

    if version.startswith("v"):
        version = version[1:]

    jar_file_path = f"google-java-format-{version}-all-deps.jar"
    if not os.path.isfile(jar_file_path):
        url = DOWNLOAD_URL_TEMPLATE.format(version=version)
        response = requests.get(url)
        with open(jar_file_path, "wb") as jar_file:
            jar_file.write(response.content)
        print(f"Downloaded {url}")

    os.chdir("..")

    subprocess.run(["java", "-jar", f".cache/{jar_file_path}", "--replace"] + java_files)


def main_with_args():
    parser = ArgumentParser(description="Download and run the google java formatter")
    parser.add_argument(
        "--version",
        dest="version",
        help=f"The version of the google java formatter. (Defaults to '{DEFAULT_VERSION}')",
        type=str,
        required=False,
        default=DEFAULT_VERSION,
    )
    parser.add_argument("files", help="The list of filest to check", type=str, nargs="+")
    args = parser.parse_args()

    exit(main(args.version, args.files))


if __name__ == "__main__":
    main_with_args()
