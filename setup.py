from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()


version = '0.3.2'

install_requires = [
    # <1.8 because 1.8 changed exception hierarchy to include, at least,
    # ProtocolError.
    'urllib3>=1.7,<1.8',
    'pyOpenSSL>=0.14',
]

test_requires = [
    'mock',
    'nose',
]

setup(name='calico-python-etcd',
    version=version,
    description="A python client for etcd.  Fork of Jose Plana's "
                "python-etcd module with support for streaming and "
                "additional error handling.",
    long_description=README + '\n\n' + NEWS,
    classifiers=[
        "Topic :: System :: Distributed Computing",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Topic :: Database :: Front-Ends",
    ],
    keywords='etcd raft distributed log api client',
    author='Jose Plana, Updates by Project Calico',
    author_email='shaun@projectcalico.org',
    url='http://github.com/Metaswitch/python-etcd',
    license='MIT',
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    tests_require=test_requires,
    test_suite='nose.collector',

)
