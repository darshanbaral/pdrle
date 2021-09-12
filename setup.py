from setuptools import setup


setup(name="pdrle",
      version="0.3",
      description="python package for run length encoding on pandas Series",
      url="https://github.com/darshanbaral/pyrle",
      author="Darshan Baral",
      license="MIT",
      packages=["pdrle"],
      install_requires=["pandas"]
      )
