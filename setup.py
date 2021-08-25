import io
from os import path

from setuptools import setup

import isdayoff


here = path.abspath(path.dirname(__file__))


def long_description():
    with io.open(file=path.join(here, "README.md"), encoding="utf-8") as file:
        return file.read()

def requirements():
    with io.open(file=path.join(here, "requirements.txt")) as file:
        return file.readlines()


setup(
    name='isdayoff',
    version=isdayoff.ProdCalendar.__version__,
    description='Checking the date for belonging to a non-working day, according to official decrees and orders.',
    long_description=long_description(),
    long_description_content_type="text/markdown",
    url='https://github.com/kobylinsky-m/isdayoff',
    author='Maxim Kobylinsky',
    author_email='wg7831@gmail.com',
    license="MIT",
    packages=['isdayoff'],
    install_requires=requirements(),
    zip_safe=False
)


