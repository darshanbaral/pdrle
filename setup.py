from setuptools import setup


setup(name="pyrle",
      version="0.1",
      description="python package for run length encoding on pandas Series",
      url="https://github.com/darshanbaral/pyrle",
      author="Darshan Baral",
      license="MIT",
      packages=["pyrle"],
      install_requires=["pandas"]
      )
