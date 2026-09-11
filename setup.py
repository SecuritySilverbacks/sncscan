from setuptools import setup

setup(
    name='sncscan',
    version='1.1.0',
    packages=[''],
    url='https://github.com/SecuritySilverbacks/sncscan',
    license='GPLv3',
    author='Jonas Wamsler, Nicolas Schickert',
    author_email='jonas.wamsler@usd.de',
    description='sncscan: Tool for analyzing SAP Secure Network Communications (SNC).',
    install_requires=["pysap @ git+https://github.com/OWASP/pysap.git@master"],
    dependency_links=[
            'git+https://github.com/OWASP/pysap.git@master#egg=pysap'
        ]
    )
