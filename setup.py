from setuptools import setup


setup(name="pdrle",
      version="0.4",
      description="python package for run length encoding on pandas Series",
      url="https://github.com/darshanbaral/pyrle",
      author="Darshan Baral",
      author_email="darshanbaral@gmail.com",
      license="MIT",
      packages=["pdrle"],
      download_url="https://github.com/darshanbaral/pdrle/archive/refs/tags/0.3.tar.gz",
      install_requires=["pandas"]
      )
