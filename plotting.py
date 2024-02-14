import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from constants import DATETIME_FEATURE, TARGET, CATEGORICAL_FEATURES

sns.set_style("whitegrid")


def plot_features(feature: str, feature_data: pd.Series):
    feature_data.value_counts().plot(kind='bar')

    plt.title(f'{feature} Distribution')
    plt.xlabel(feature)
    plt.ylabel('Frequency')
    plt.show()


def plot_timeline(data: pd.DataFrame, resample_parameter: str = "W"):
    data[DATETIME_FEATURE] = pd.to_datetime(data[DATETIME_FEATURE])
    data = data.set_index(DATETIME_FEATURE)

    results = data.resample(resample_parameter)[TARGET].value_counts().unstack(fill_value=0)
    results.index = results.index.strftime('%Y-%m-%d')

    results.plot(kind='bar', stacked=True, figsize=(10, 6))
    plt.title('Timeline of COVID-19 Test Results')
    plt.xlabel('Date')
    plt.ylabel('Number of Tests Conducted')
    plt.xticks(rotation=45)
    plt.legend(title='Diagnosis')
    plt.show()
