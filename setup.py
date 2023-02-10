from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in ftp_backup/__init__.py
from ftp_backup import __version__ as version

setup(
	name="ftp_backup",
	version=version,
	description="backup using ftp",
	author="MR.Ratha",
	author_email="ratha@mail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
