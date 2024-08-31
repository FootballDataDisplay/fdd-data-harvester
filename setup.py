from setuptools import setup, find_packages

setup(
    name='fdd-data-harvester',
    version='0.1.0',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='A data harvester for NFL statistics',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=['pandas', 'requests', 'beautifulsoup4', 'matplotlib', 'seaborn'],
    url='https://github.com/FootballDataDisplay/fdd-data-harvester',
    author='Your Name',
    author_email='your.email@example.com'
)