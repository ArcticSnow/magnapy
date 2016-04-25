from distutils.core import setup

setup(
    name='magnapy',
    version='0.1dev',
    packages=['magnapy'],
    license='GNU General Public License version 3',
    long_description=open('README.md').read(),
    author='S. Filhol',
    author_email='svfilhol@alaska.edu',
    license='license.txt',
    description='Toolbox for Magnaprobe data',
    install_requires=[
        "pandas >= 0.16.2 ",
        "pyproj >= 1.9.5.1",
        "matplotlib >= 1.5.1"
    ],
)