from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.3'
DESCRIPTION = 'A Python library for sending SMS via sms.ir API'
LONG_DESCRIPTION = 'A package that allows you to send SMS via sms.ir API without direct exposure to the API.' 

# Setting up
setup(
    name="py-persian-sms",
    version=VERSION,
    author="Amirhossein Nashvi",
    author_email="<amirhosseinnashvi@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['requests'],
    keywords=["sms.ir", "sms", "python-sms.ir"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    url="https://github.com/nashviamir/py-persian-sms"
)