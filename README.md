# Machine Learning Projects

## Basic Terminology

### Machine Learning Data

* **Observations** - Any dataset attributes.
* **Labels** - Used in unsupervised learning. Future outcomes. This is the value we are trying to predict.
* **Features** - Also called *Dimensions*. All other attributes used to predict Labels. Any attribute chosen to be used as a data point in the training data set. eg. Age, occupation, sex, zip code, etc.
* **Feature Vector or Example** - The distinct values of a single feature.
* **Feature Engineering** -The process of using domain knowledge of the data to create Features that make machine learning algorithms work.

![](https://github.com/harperd/machine-learning/blob/master/images/dataparts.gif)

### Data Classification

* **Binary Data** - One of two possible values.
* **Multiclass Data** - One more more possible values.
* **Structured Data** - Organized and stored in databases in the form of rows and columns.
* **Semi-Structured** - JSON, YAML, CSV, etc.
* **Unstructured** - Most common type - no structure - Logs, video content, etc.

## Types of Machine Learning

* **Supervised Machine Learning** - Outcomes, or Lables, are not known. Given a set of Feature/Label pairs, find a rule that predicts the label associated with a previously unseen input.
* **Unsupervised Machine Learning** - Outcomes, or Lables, are known. Given a set of Feature vectors (without Labels) group them into “natural clusters”.
* **Reinforcement Learning** - The algorithm is rewarded based on choices it makes while learning.

## Machine Learning Models

* **Cluster** - Grouping of similar Examples or Feature Vectors.
* **Centroid** -Defines a cluster. This is a point (either imaginary or real) at the center of a cluster. Every point in a data set is part of the cluster whose centroid is most closely located.
* **Overfitting** - A model where the training data is modeled too well. Overfitting happens when a model learns the detail and noise in the training data to the extent that it negatively impacts the performance of the model on new data.
* **Underfitting** - A model that can neither model the training data nor generalize to new data. An underfit machine learning model is not a suitable model and will be obvious as it will have poor performance on the training data. 

![](https://github.com/harperd/machine-learning/blob/master/images/fit.jpg)





