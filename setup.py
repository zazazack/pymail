import codecs
import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read().strip()

setup(
    name='pymail',
    author='Zachary Wilson',
    author_email='wilsonze@gmail.com',
    packages=find_packages(exclude=['tests*', 'docs', 'contrib']),
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
    ],
    setup_requires=['setuptools_scm', 'setuptools_scm_about'],
    use_scm_version={'write_to': 'pymail/_version.py'},
    entry_points={'console_scripts': ['pymail=pymail.cli:cli']},
    url='https://github.com/zazazack/pymail')
