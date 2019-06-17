# coding=utf-8

from setuptools import find_packages, setup
import pathlib
import os

MAIN_DIR = pathlib.Path(__file__).absolute().parent


def get_packages():
    base_file = MAIN_DIR / "requirements" / "base.in"
    response = []

    with base_file.open("r") as file:
        for line in file:
            line = line.strip()
            if not line.startswith("#"):
                response.append(line)
    return response


packages = find_packages(
    str(MAIN_DIR), include=("{{cookiecutter.project_slug}}*",), exclude=[]
)


# Did I mention that setup.py is not finest piece of software on earth.
# For this to work when installed you'll need to enumerate all template and static file.
def read_dir(package: str, directory: str):
    package_root = os.path.abspath(package.replace(".", "/"))
    directory = os.path.join(package_root, directory)
    res = []
    for root, subFolders, files in os.walk(directory):
        for file in files:
            res.append(os.path.relpath(os.path.join(root, file), package_root))

    return res


if __name__ == "__main__":

    setup(
        name="{{cookiecutter.project_slug}}",
        version="{{cookiecutter.version}}",
        packages=packages,
        license="All Rights reserved",
        author="{{ cookiecutter.full_name }}",
        author_email="{{ cookiecutter.email }}",
        description="{{cookiecutter.project_short_description}}",
        install_requires=get_packages(),
        package_data={
            package: [] + read_dir(package, "static") + read_dir(package, "templates")
            for package in packages
        },
        include_package_data=True,
    )
