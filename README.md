- [Apprenticeship Hackathon](#apprenticeship-hackathon)
  * [Schedule](#schedule)
    + [Day 1](#day-1)
    + [Day 2](#day-2)
  * [Project Setup](#project-setup)
    + [Libraries](#libraries)

# Apprenticeship Hackathon

The goal of the L7 Apprenticeship Hackathon is to give you an opportunity to work in a team to test your new skills.

You are going to be provided with a sample of possible questions to investigate and tasks to undertake. However, you are free to design your own tasks as a team and augment the initial datasets for your own analysis.

The objective is to allow you to come together as a team and solve a problem or answer a question using your exploratory analysis in limited timescales - you don’t need to do any preparatory work for the event.

The hackathon isn’t assessed and won’t impact your final apprenticeship grade, but it is a great opportunity to apply the knowledge, skills and behaviours you’ve been learning and get some feedback from your hackathon facilitator.

## Schedule

### Day 1

- 9.30am - 10am: Induction and access to data sets and brief. Your hackathon facilitator will introduce your task and let you know how to access your data.
- 10am - 5pm: Work in your teams on the brief you’ve been given.

### Day 2

- 9.30am - 3pm: Work in your teams on the brief you’ve been given.
- 3pm - 5pm: You will be required to deliver a 15 minute presentation (10 minutes of presentation and 5 minutes of Q&A) about the outcome of your work.

## Project Setup

Make sure to have a suitable stable version of `Python` 3.x and `pip` installed on your machine. Consider using [Pyenv](https://github.com/pyenv/pyenv#installation) to manage your Python versions.

The required Python version for this project is `3.11.x` and can be installed by running `pyenv install 3.n.m`, where `n` and `m` are the minor and patch version respectively.

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

Install the required libraries

```sh
pip install -r requirements.txt
```

Start the development environment

```
jupyter notebook
```

> NOTE: remember to deactivate the virtual environment by running the `deactivate` command once finished or if you switch project. If you don't do this and run `python` in another project through the same terminal session, you'll be running the same local version of Python with dependencies you may not want or need.

### Libraries

The Python libraries are installed through the `requirements.txt` file. In case you use a different environment/setup than the one described in this repo, this is the list of dependencies you'll need to install:

```
pip install --upgrade pip setuptools wheel black isort notebook jupyterlab ipywidgets jupyterlab-code-formatter numpy scipy pandas ydata-profiling statsmodels matplotlib seaborn plotly scikit-learn tensorflow keras-tuner xgboost lightgbm prophet optuna imbalanced-learn pyarrow
```
