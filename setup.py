import re
from setuptools import setup


requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

version = ''
with open('aiowaifus/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('version is not set')


readme = ''
with open('README.md') as f:
    readme = f.read()

extras_require = {
    'docs': [
        'sphinx-material'
    ]
}

setup(name='aiowaifus',
      author='kyomi',
      url='https://github.com/soukyomi/aiowaifus',
      project_urls={
          'Issue tracker': 'https://github.com/soukyomi/aiowaifus/issues',
          'Documentation': 'https://aiowaifus.readthedocs.io/en/latest/'
      },
      version=version,
      packages=['aiowaifus'],
      license='MIT',
      description='An async ready API wrapper for Waifus.pics written in Python',
      long_description=readme,
      long_description_content_type='text/markdown',
      install_requires=requirements,
      extras_require=extras_require,
      python_requires='>=3.6.0',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'License :: OSI Approved :: MIT License',
          'Intended Audience :: Developers',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Topic :: Internet',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Utilities',
      ]
)
