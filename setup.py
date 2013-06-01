from distutils.core import setup


setup(name='lm',
      version='0.2',
      license='GPL',
      packages=['lm'],
      scripts=['scripts/lm'],
      requires=['imdbpy',
                'argparse',
                'colorama']
      )
