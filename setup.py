# This should be only one line. If it must be multi-line, indent the second
# line onwards to keep the PKG-INFO file format intact.
"""Create a DSL script for the Jenkins Job DSL plugin from configuration.
"""

from setuptools import setup, find_packages
import glob
import os.path


def project_path(*names):
    return os.path.join(os.path.dirname(__file__), *names)


setup(
    name='gocept.jenkinsdsl',
    version='0.1.dev0',

    install_requires=[
        'setuptools',
    ],

    extras_require={
        'test': [
        ],
    },

    entry_points={
        'console_scripts': [
            'jenkinsdsl = gocept.jenkinsdsl.jenkinsdsl:main'
        ],
    },

    author='gocept <mail@gocept.com>',
    author_email='mail@gocept.com',
    license='ZPL 2.1',
    url='https://bitbucket.org/gocept/gocept.jenkinsdsl/',

    keywords='jenkins DSL job groovy',
    classifiers="""\
License :: OSI Approved :: Zope Public License
Programming Language :: Python
Programming Language :: Python :: 3
Programming Language :: Python :: 3.5
Programming Language :: Python :: 3 :: Only
Programming Language :: Python :: Implementation :: CPython
"""[:-1].split('\n'),
    description=__doc__.strip(),
    long_description='\n\n'.join(open(project_path(name)).read() for name in (
        'README.rst',
        'HACKING.rst',
        'CHANGES.rst',
    )),

    namespace_packages=['gocept'],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    data_files=[('',
                 glob.glob(project_path('*.txt')),
                 glob.glob(project_path('*.rst')))],
    zip_safe=False,
)