from setuptools import setup, find_packages

setup(
    name='euler-cli',
    description='Cli utility for setting up python modules to solve Project Euler',
    url='https://github.com/naren-m/euler',
    author='Naren Mudivarthy',
    author_email='naren.mudivarthy@gmail.com',
    packages=find_packages(),
    install_requires=[
        "fire",
        "requests",
        "bs4",
    ],
    version='0.1.2',
    entry_points={'console_scripts': ['euler = euler.__main__:main']})
