from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in suncloud_customizations/__init__.py
from suncloud_customizations import __version__ as version

setup(
	name="suncloud_customizations",
	version=version,
	description="Suncloud Customizations",
	author="Jigar Tarpara",
	author_email="jigartarpara@khatavahi.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
