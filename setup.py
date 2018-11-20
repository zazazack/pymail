import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'pymail', 'VERSION'), encoding='utf-8') as f:
    version = f.read().strip()

with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read().strip()

setup(
    name='pymail',
    author='Zachary Wilson',
    author_email='wilsonze@gmail.com',
    packages=find_packages(exclude=['tests*', 'docs', 'contrib']),
    version=version,
    description='Send email with Python for fun and profit.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    project_urls={
        'Source': 'https://github.com/zazazack/pymail.git',
        'Documentation': 'https://github.com/zazazack/pymail.git',
    },
    install_requires=[
        'click',
        'requests',
        'flask',
        'sqlalchemy',
    ])
