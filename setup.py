"""Setup for bibblio XBlock."""

import os
from setuptools import setup


def package_data(pkg, roots):
    """Generic function to find package_data.

    All of the files under each of the `roots` will be declared as package
    data for package `pkg`.

    """
    data = []
    for root in roots:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


setup(
    name='edx-xblock-bibblio',
    version='0.1',
    description='XBlock for Bibblio Recommendations',
    license='AGPL v3',
    packages=[
        'bibblio',
    ],
    install_requires=[
        'XBlock',
        'xblock-utils',
        'bibbliothon==1.1.2'
    ],
    entry_points={
        'xblock.v1': [
            'bibblio = bibblio:BibblioXBlock',
        ]
    },
    package_data=package_data("bibblio", ["static", "public"]),
)
