from distutils.core import setup

from download_opendatasoft import __version__

setup(name='download_opendatasoft',
      author='Thomas Levine',
      author_email='_@thomaslevine.com',
      description='Download data from OpenDataSoft open data platforms.',
      url='https://github.com/tlevine/download_opendatasoft',
      packages=['download_opendatasoft'],
      install_requires = ['picklecache'],
      tests_require = ['nose'],
      version=__version__,
      license='AGPL',
)
