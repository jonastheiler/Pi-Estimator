from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()
    
setup(name = 'thjo_pi_estimator',
      version = '1.0.5',
      description = 'Estimation of pi',
      long_description=long_description,
      long_description_content_type='text/markdown',
      packages = find_packages(),
      author = 'Jonas Theiler',
      author_email = 'jonas_theiler@hotmail.com',
      zip_safe = False)