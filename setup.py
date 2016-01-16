import os
from setuptools import setup

setup(name="opentmf",
      version="0.1",
      author="Reinder Feenstra",
      author_email="reinderfeenstra@gmail.com",
      description=("Python bindings for Open Test & Measurement Framework"
                   "library"),
      license="GNU LGPL v2.1",
      url="http://github.com/opentmf/py-libopentmf",
      packages=['opentmf'],
      long_description=open(os.path.join(
                            os.path.dirname(__file__), "README")).read())
