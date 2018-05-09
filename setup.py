import os
from distutils.core import setup


def get_data_files():
    """
    Get the data files for the package.
    """
    return [
        ('share/jupyter/nbextensions/gsgenelab', [
            'GSGeneLab/static/genelab.js'
        ]),
        # JTL What is this next line for?
        ('etc/jupyter/nbconfig/notebook.d', ['GSGeneLab.json']),
    ]

setup(name='GSGeneLab',
      packages=['GSGeneLab'],
      version='0.1',
      description='A jupyter extension to connect with GeneLab-GenomeSpace',
      license='BSD',
      author='Ted Liefeld',
      author_email='jliefeld@cloud.ucsd.edu',
      
      ## JTL Not sure what to put for URLs yet
      url='https://github.com/genepattern/',
      download_url='https://github.com/genepattern/',
      
      keywords=['genepattern', 'genomics', 'bioinformatics', 'ipython', 'jupyter', 'genelab', 'nasa', 'genomespace'],
      
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Science/Research',
          'Intended Audience :: Developers',
          'Topic :: Scientific/Engineering :: Bio-Informatics',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python',
          'Framework :: Jupyter',
      ],
      # JTL what is the right name for the nbToolManager?
      install_requires=[
          'jupyter',
          'nbtools',
          'notebook>=4.2.0',
          'ipywidgets>=5.0.0',
      ],
      package_data={'GSGeneLab': ['static/GSGeneLab.js']},
      data_files=get_data_files(),
      )
