import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

VERSION = '0.1.1'
PACKAGE_NAME = 'crypto2csv'
AUTHOR = 'Fearsomejockey'
AUTHOR_EMAIL = 'prathamagrawal1205@gmail.com'
URL = 'https://github.com/prathamagrawal/crypto2csv'

LICENSE = 'Apache License 2.0'
DESCRIPTION = 'A Package to download and saccess cryptocurrecy data using API.'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
      'numpy',
      'pandas',
      'requests'
]



setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      install_requires=INSTALL_REQUIRES,
      packages=find_packages(),
      entry_points ={
            'console_scripts': [
                'crypto2csv = crypto2csv.main:main'
            ]
        }
      )