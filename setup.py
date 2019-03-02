from setuptools import setup, find_packages

setup(
    name='euler',
    description='Cli app to get problem from project euler webpage',
    url='https://github.com/naren-m/euler',
    author='Naren Mudivarthy',
    author_email='naren.mudivarthy@gmail.com',
    classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Any one interested in problem solving',
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python :: 3.5,'
          'Programming Language :: Python :: 3.6,'
          'Programming Language :: Python :: 3.7,'
    ],
    packages=find_packages(),
    install_requires=[
        "fire",
        "requests",
        "bs4",
    ],
    version='0.1.0',
    entry_points={'console_scripts': ['euler = euler.__main__:main']})
