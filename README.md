# Apprenticeship Hackathon

The L7 AI Hackathon will give you an opportunity to work in a team of four/five to test your new data science and ML skills. You will be required to deliver a 15mins presentation (10mins presentation and 5mins for Q&A) about your learning journey in the programme & the outcome of your work.

You are going to be provided with a sample of possible questions to investigate and tasks to undertake. However, you are free to design your own tasks as a team and augment the initial datasets for your own analysis.

In this hackathon, we want you to build machine learning models to predict COVID-19 infections from symptoms. It has several applications – for example, triaging patients to be attended by a doctor or nurse, recommending self-isolation through contact tracing apps, etc.

Zoabi et al. (link here) [1] builds a decision tree classifier using the publicly available data reported by the Israeli Ministry of Health. The paper itself discusses the various challenges encountered in deploying such a model. We encourage you to read the paper and learn the challenges and ways to overcome them. We will be using the dataset in this paper (Github link in the references).

## References
[1] Zoabi, Y., Deri-Rozov, S. & Shomron, N. Machine learning-based prediction of COVID-19 diagnosis based on symptoms. npj Digit. Med. 4, 3 (2021).
[2] [Github link](https://github.com/nshomron/covidpred/tree/master) referenced in the paper. The main page of the Github repository mentions that the data file, corona_tested_individuals_ver_006.english.csv.zip was the version they used for the analysis. It is also the version we will use for this hackathon.
[3] Kate: https://app.edukate.ai/modules/9202/
[4] Presentation: https://docs.google.com/presentation/d/1zHdHQ3ELAWTsFYYmh_0KdX3xI2HRWW1c0-VXMdmPhXE/edit

## Instructions

Use `random_state=137`

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
