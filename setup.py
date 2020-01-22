from setuptools import setup

setup(
      name='novo',
      version='0.1.0',
      author='Ashton Hanisch',
      author_email='ajhanisch@gmail.com',
      packages=['novo'],
      url='http://pypi.python.org/pypi/Novo/',
      license='LICENSE.txt',
      description='Enables virtual machine provisioning for various hypervisors.',
      long_description=open('README.txt').read(),
      # install_requires=[
      #       "Django >= 1.1.1",
      #       "caldav == 0.1.4",
      # ],
)