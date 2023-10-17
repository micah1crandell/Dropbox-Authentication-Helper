from setuptools import setup, find_packages

setup(
    name='dbx_auth_helper',
    version='0.1.0',
    packages=find_packages(),
    url='https://github.com/Ceiling-Fan-Studios/Dropbox-Authentication-Helper',
    author='Micah Crandell',
    author_email='micah1crandell@gmail.com',
    description='Dropbox authentication and refresh/access code helper.',
    long_description='The Dropbox Authentication Helper is a Python package designed to streamline the process of managing Dropbox application tokens. It offers an intuitive and user-friendly solution for developers to effortlessly obtain and refresh access tokens, simplifying the integration of Dropbox\'s API into their projects.',
    classifiers=[
       'Development Status :: 4 - Beta',
       'Intended Audience :: Developers',
       'License :: OSI Approved :: MIT License',
       'Programming Language :: Python :: 3',
    ],
)