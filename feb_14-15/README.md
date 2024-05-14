- [Hackathon instructions](#hackathon-instructions)
  * [References](#references)
  * [Presentation](#presentation)
    + [Exploratory Data Analysis](#exploratory-data-analysis)
    + [Feature Engineering](#feature-engineering)
    + [Models](#models)
    + [Evaluate](#evaluate)
    + [Report your result](#report-your-result)
    + [Extras](#extras)

# Hackathon instructions

Date: 14/15 February 2024

The L7 AI Hackathon will give you an opportunity to work in a team of four/five to test your new data science and ML skills. You will be required to deliver a 15mins presentation (10mins presentation and 5mins for Q&A) about your learning journey in the programme & the outcome of your work.

You are going to be provided with a sample of possible questions to investigate and tasks to undertake. However, you are free to design your own tasks as a team and augment the initial datasets for your own analysis.

In this hackathon, we want you to build machine learning models to predict COVID-19 infections from symptoms. It has several applications – for example, triaging patients to be attended by a doctor or nurse, recommending self-isolation through contact tracing apps, etc.

Zoabi et al. ([link here](https://www.nature.com/articles/s41746-020-00372-6)) [1] builds a decision tree classifier using the publicly available data reported by the Israeli Ministry of Health. The paper itself discusses the various challenges encountered in deploying such a model. We encourage you to read the paper and learn the challenges and ways to overcome them. We will be using the dataset in this paper (Github link in the references).

Use `random_state=137`

## References

[1] Zoabi, Y., Deri-Rozov, S. & Shomron, N. Machine learning-based prediction of COVID-19 diagnosis based on symptoms. npj Digit. Med. 4, 3 (2021).
[2] [Github link](https://github.com/nshomron/covidpred/tree/master) referenced in the paper. The main page of the Github repository mentions that the data file, corona_tested_individuals_ver_006.english.csv.zip was the version they used for the analysis. It is also the version we will use for this hackathon.
[3] Kate: https://app.edukate.ai/modules/9202/
[4] Presentation: https://docs.google.com/presentation/d/1zHdHQ3ELAWTsFYYmh_0KdX3xI2HRWW1c0-VXMdmPhXE/edit

## Presentation

On Day 2, between 3-5PM, your team will deliver a presentation of your findings and experience for 10 minutes followed by 5 minutes of Q&A from your peers.

The presentation should cover (non-exhaustively) the following components:

- Briefly define the problem
- Briefly describe the dataset
- What did you learn about various models/techniques/etc.?
- What’s the AUC score of your final model?

Below are a list of potential questions and directions that you can explore but you are free and encouraged to be creative and explore other directions to apply your ML skills.

### Exploratory Data Analysis

- Think about possible biases and limitations of this dataset. What are the sources of uncertainty?
- What is the format of feature values?
- What is the statistics of these feature values? How many symptoms are reported or not?
- Which symptoms have a reporting bias, i.e., likely to be reported when the patient is COVID positive?
- How will the symptoms with reporting bias affect the model’s performance?
- Visualization: Draw the bar graph of features grouped by the target class?
- What does the bar graph of the symptoms with reporting bias look like?
- Determine if we have a class imbalance in the dataset? If so, what do you reckon will be the downstream challenges in evaluating the model? How will you overcome those challenges?

### Feature Engineering

- How will you represent the features in numerical format that can be accessible by model?
- Are there any redundancies in your feature representation?

### Models

- Check out various classifiers in sklearn or any other preferred library to build your models

### Evaluate

- Is accuracy the right metric to evaluate the model? Are inaccuracies correctly penalized in the accuracy metric?
- Which dataset should you choose to evaluate the model? Validation or Test?
- What other metric is relevant in our context?
- For benchmarking everyone’s results we will stick to ROC-AUC score as a metric.

### Report your result

- With the metric chosen, report your result on the test dataset.
- How will you select the threshold for your model above which model score will be interpreted as a prediction of positive diagnosis.

### Extras

- Dimensionality Reduction for fun: Can you reduce the dimension to just 2 dimensions and check if the inputs corresponding to different classes belong to different clusters? Try using t-SNE or UMAP for that purpose.
- Collaborate with Ensemble: Can you combine other models?
