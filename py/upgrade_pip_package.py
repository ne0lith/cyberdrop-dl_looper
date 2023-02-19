import sys, subprocess
import json, urllib.request
from pkg_resources import parse_version, get_distribution, DistributionNotFound

auto_packages = ["cyberdrop-dl"]


def package_installed(package):
    try:
        get_distribution(package)
        return True
    except DistributionNotFound:
        return False


def compare_versions(local, remote, package):
    if parse_version(local) == parse_version(remote):
        print(f"{package} is up to date.", end=" ")
        print(f"(local: {local})")
        return 0

    if parse_version(local) < parse_version(remote):
        print(f"{package} is out of date.", end=" ")
        print(f"(local: {local} < remote: {remote})")
        return 1

    if parse_version(local) > parse_version(remote):
        print(f"{package} is newer than remote.", end=" ")
        print(f"(local: {local} > remote: {remote})")
        return -1


def install_package(package, auto_install=False):
    version = get_version(package, "remote")
    name_version = f"{package} ({version})"

    if package in auto_packages:
        auto_install = True

    if auto_install:
        print(f"Auto installing {name_version}")
        if package_installed(package):
            if package != "pip":
                subprocess.run(["pip", "uninstall", package, "-y"])
        subprocess.run(["pip", "install", "--upgrade", package])
        print(f"{name_version} installed")
    else:
        if input(f"Do you want to install {name_version}? (y/n): ") == "y":
            if package_installed(package):
                if package != "pip":
                    subprocess.run(["pip", "uninstall", package, "-y"])
            subprocess.run(["pip", "install", "--upgrade", package])
            print(f"{name_version} installed")
        else:
            print(f"{name_version} not installed")


def get_version(package, type):
    types = ["local", "remote"]

    if type not in types:
        raise ValueError(f"type must be one of {types}")
    elif type == "local":
        if package_installed(package):
            return get_distribution(package).version
        else:
            return 0
    elif type == "remote":
        url = f"https://pypi.org/pypi/{package}/json"
        with urllib.request.urlopen(url) as f:
            data = json.load(f)
        return data["info"]["version"]


def upgrade_package(package):
    local_version = get_version(package, "local")
    remote_version = get_version(package, "remote")

    if compare_versions(local_version, remote_version, package) != 0:
        print(f"local: {local_version}")
        print(f"remote: {remote_version}")
        install_package(package)


def main():
    if len(sys.argv) > 1:
        package_list = sys.argv[1:]
    else:
        package_list = input("Enter packages (seperate multiple names by space): ")

    if isinstance(package_list, str):
        package_list = package_list.split()

    for package in package_list:
        if package_installed(package):
            upgrade_package(package)
        else:
            print(f"{package} is not installed")
            install_package(package)


if __name__ == "__main__":
    try:
        print("Running upgrade_pip_package.py")
        main()
    except ValueError as e:
        print(e)
