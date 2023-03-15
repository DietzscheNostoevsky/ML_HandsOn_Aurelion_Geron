# **Machine Learning Project Checklist**

# Checklist 

- [x] (for checked checkbox)
- [ ] (for unchecked checkbox) 
  
- [ ] ***1.  Frame the problem and look at the bigger picture***
    - [ ] Define the objective in business terms
    - [ ] How will your solution be used?
    - [ ] What are the current solutions/workarounds (if any)?
    - [ ] How should you frame this problem (supervised/unsupervised, online/offline, etc.)?
    - [ ] How should performance be measured?
    - [ ] Is the performance measure aligned with the business objective?
    - [ ] What would be the minimum performance needed to reach the business objec‐ tive?
    - [ ] What are comparable problems? Can you reuse experience or tools?
    - [ ] Is human expertise available?
    - [ ] How would you solve the problem manually?
    - [ ] List the assumptions you (or others) have made so far. 
    - [ ] Verify assumptions if possible.


- [ ] ***2. Get the Data***

    - [ ] List the data you need and how much you need.
    - [ ] Find and document where you can get that data.
    - [ ] Check how much space it will take.
    - [ ] Check legal obligations, and get authorization if necessary. 
    - [ ] Get access authorizations.
    - [ ] Create a workspace (with enough storage space).
    - [ ] Get the data.
    - [ ] Convert the data to a format you can easily manipulate (without changing the data itself).
    - [ ] Ensure sensitive information is deleted or protected (e.g., anonymized). 
    - [ ] Check the size and type of data (time series, sample, geographical, etc.). 
    - [ ] Sample a test set, put it aside, and never look at it (no data snooping!).
  
- [ ] ***3. Explore the Data to gain insights***
    - [ ] Note: try to get insights from a field expert for these steps.
    - [ ] Create a copy of the data for exploration (sampling it down to a manageable size if necessary).
    - [ ] Create a Jupyter notebook to keep a record of your data exploration. 
    - [ ] 3. Study each attribute and its characteristics:
        - [ ] • Name
        - [ ] • Type (categorical, int/float, bounded/unbounded, text, structured, etc.) 
        - [ ] • % of missing values
        - [ ] • Noisiness and type of noise (stochastic, outliers, rounding errors, etc.)
        - [ ] • Usefulness for the task
        - [ ] • Type of distribution (Gaussian, uniform, logarithmic, etc.)
    - [ ] For supervised learning tasks, identify the target attribute(s). 
    - [ ] Visualize the data.
    - [ ] Study the correlations between attributes.
    - [ ] Study how you would solve the problem manually.
    - [ ] Identify the promising transformations you may want to apply.
    - [ ] Identify extra data that would be useful (go back to “Get the Data” on page 780 of book). 
    - [ ] Document what you have learned.
  
- [ ] ***4. Prepare the data to better expose the underlying data patterns to ML algos***
    - [ ] Notes:
      - [ ] • Work on copies of the data (keep the original dataset intact).
      - [ ] Write functions for all data transformations you apply, for five reasons:
        - [ ] So you can easily prepare the data the next time you get a fresh dataset 
        - [ ] So you can apply these transformations in future projects
        - [ ] To clean and prepare the test set
        - [ ] To clean and prepare new data instances once your solution is live
        - [ ] To make it easy to treat your preparation choices as hyperparameters
    - [ ] Clean the data:
      - [ ] Fix or remove outliers (optional).
      - [ ] Fill in missing values (e.g., with zero, mean, median...) or drop their rows (or columns).
    - [ ] Perform feature selection (optional):
      - [ ] Drop the attributes that provide no useful information for the task.
    - [ ] Perform feature engineering, where appropriate:
      - [ ] Discretize continuous features.
      - [ ] Decompose features (e.g., categorical, date/time, etc.).
      - [ ] Add promising transformations of features (e.g., log(x), sqrt(x), x2, etc.).
       - [ ] Aggregate features into promising new features.
   - [ ] Perform feature scaling:
       - [ ] Standardize or normalize features.


- [ ] ***5. Explore many different models and shortlist the besto ones*** 
    - [ ] **Note:** If the data is huge, you may want to sample smaller training sets so you can train many different models in a reasonable time (be aware that this penalizes complex models such as large neural nets or random forests).
      - [ ] try to automate these steps as much as possible.
    - [ ] Train many quick-and-dirty models from different categories (e.g., linear, naive Bayes, SVM, random forest, neural net, etc.) using standard parameters.
    - [ ] Measure and compare their performance:
        - [ ] For each model, use N-fold cross-validation and compute the mean and stan‐dard deviation of the performance measure on the N folds. 
    - [ ] Analyze the most significant variables for each algorithm.
  - [ ] Analyze the types of errors the models make:
      - [ ] What data would a human have used to avoid these errors
  - [ ] Perform a quick round of feature selection and engineering
  - [ ] Perform one or two more quick iterations of the five previous steps.
  - [ ] Shortlist the top three to five most promising models, preferring models that make different types of errors.


- [ ] ***6. Fine tune the model and combine them into a solution***
- [ ] ***7. Present the solution***
- [ ] ***8. Launch, monitor and maintain the system***

