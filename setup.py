from setuptools import setup

setup(
   name='calculator',
   version='0.1.1',
   author='upendra',
   author_email='upsingh@gmail.com',
   package_dir={"": "src"},
   packages=['calculator'],
   description='An awesome package that does something',
   install_requires=[
       "pytest",
   ],
)