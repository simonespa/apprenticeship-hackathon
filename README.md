# Apprenticeship Hackathon

- Kate: https://app.edukate.ai/modules/9202/
- Presentation: https://docs.google.com/presentation/d/1zHdHQ3ELAWTsFYYmh_0KdX3xI2HRWW1c0-VXMdmPhXE/edit


random_state=137

## Getting started with PIP and Virtualenv

Install [Virtualenv](https://pypi.org/project/virtualenv/) in order to setup an isolated virtual environment to manage the Python project and dependencies (read this [installation](https://virtualenv.pypa.io/en/latest/installation.html) guide on how to).

You need to create a virtual environment with a clean installation of Python. The following command do so, by creating a folder called `.python` (which is automatically excluded from revision control) containing a vanilla installation of Python with just the initial depdendencies installed.

Create a virtual environment (only if you don't have an `.python` folder yet)

```sh
virtualenv .python
```

Enable the virtual environment

```sh
source .python/bin/activate
```

Check the python interpreter used is the one from the virtual environment

```sh
which python
```

Install the required dependencies

```sh
pip install -r requirements.txt
```

Start the development environment

```
jupyter notebook
```

or

```
jupyter lab
```

> NOTE: remember to deactivate the virtual environment by running the `deactivate` command once finished or if you switch project. If you don't do this and run `python` in another project through the same terminal session, you'll be running the same local version of Python with dependencies you may not want or need.
