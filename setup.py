from setuptools import setup, find_packages

setup(
    name='Doo_DS',
    version='0.1',
    packages= find_packages(exclude=['tests']),  # Use `find_packages()` correctly
    description='NA',  # Replace with a concise description
    long_description='NA',  # Replace with a detailed description (optional)
    install_requires=['numpy'],  # Fix typo
    author='Doo',
    author_email='Doo@gmail.com',
)