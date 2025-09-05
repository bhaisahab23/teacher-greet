from setuptools import setup, find_packages

setup(
    name='teacher_greet',
    version='1.0.1',
    author='Thakur',
    description='Animated greetings for Teachers’ Day in terminal and GUI',
    packages=find_packages(),
    install_requires=[
        'colorama'
    ],
    python_requires='>=3.6',
)
