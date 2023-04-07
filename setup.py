#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = [ ]

setup(
    author="Matthijs Knigge",
    author_email='matthijsknigge@hotmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="intercepting input events using a technique called "hooking". custom DLL that hooks into the Windows API calls responsible for processing the input events and modifies them as desired",
    entry_points={
        'console_scripts': [
            'shadow_hooking_windows_api=shadow_hooking_windows_api.cli:main',
        ],
    },
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='shadow_hooking_windows_api',
    name='shadow_hooking_windows_api',
    packages=find_packages(include=['shadow_hooking_windows_api', 'shadow_hooking_windows_api.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/matthijsknigge/shadow_hooking_windows_api',
    version='0.1.0',
    zip_safe=False,
)
