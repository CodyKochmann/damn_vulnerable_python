from distutils.core import setup
from logging import warning
import os

if os.environ.get('USER', ''):
  warning('this library definitely would run better installed as root ;)')

version = '2018.5.21'

setup(
  name = 'damn_vulnerable_python',
  packages = ['damn_vulnerable_python'], # this must be the same as the name above
  version = version,
  install_requires = [],
  description = 'A python library built to demonstrate mayhem from pip packages.',
  author = 'Cody Kochmann',
  author_email = 'kochmanncody@gmail.com',
  url = 'https://github.com/CodyKochmann/damn_vulnerable_python',
  download_url = 'https://github.com/CodyKochmann/damn_vulnerable_python/tarball/{}'.format(version),
  keywords = ['damn_vulnerable_python', 'vuln', 'vulnerable', 'what were you thinking', 'for the lols', 'vulnerability', 'security', 'demonstration', 'unsafe', 'bad'],
  classifiers = [],
)
