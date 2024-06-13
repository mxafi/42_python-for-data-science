from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'A sample test package'

setup(
        setup_requires=['wheel'],
        name='ft_package',
        version=VERSION,
        author="malaakso",
        author_email="<malaakso@student.hive.fi>",
        description=DESCRIPTION,
        url='https://github.com/mxafi',
        license='MIT',
        packages=find_packages(),
        install_requires=[],
        keywords=['python', '42', 'hive', 'ft_package', 'first package'],
        classifiers=[
            "Private :: Do Not Upload",
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
        ]
)
