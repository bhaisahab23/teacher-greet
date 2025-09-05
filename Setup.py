from setuptools import setup, find_packages

setup(
    name='teacher_greet',
    version='1.0.0',
    author='Thakur',
    description='A fun animated greeting package for Teachers’ Day',
    packages=find_packages(),
    install_requires=[
        'colorama'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
