# bathtub
#
# by Phil Christensen
#

from __future__ import with_statement

import distribute_setup
distribute_setup.use_setuptools()

import os

# disables creation of .DS_Store files inside tarballs on Mac OS X
os.environ['COPY_EXTENDED_ATTRIBUTES_DISABLE'] = 'true'
os.environ['COPYFILE_DISABLE'] = 'true'

def relative_path(path):
	"""
	Return the given path relative to this file.
	"""
	return os.path.join(os.path.dirname(__file__), path)

def autosetup():
    from setuptools import setup, find_packages

    # check if installed with git data (not via PyPi)
    using_git = os.path.isdir(relative_path('.git'))
    
    return setup(
        name="bathtub",
        version="1.0",

        include_package_data=True,
        zip_safe=False,
        packages=find_packages('src'),
        package_dir={'': 'src'},

        # setuptools won't auto-detect Git managed files without this
        setup_requires = ["setuptools_git >= 0.4.2"] if using_git else [],
        
        entry_points={
            'setuptools.file_finders': [
                'git = setuptools_git:gitlsfiles',
            ],
        },
        
        author           = "Phil Christensen",
        author_email     = "phil@bubblehouse.org",
        description      = "a jamband stats database",
        license          = "MIT",
        keywords         = "django phish stats",
        url              = "https://github.com/philchristensen/bathtub",
    )

if(__name__ == '__main__'):
    dist = autosetup()
