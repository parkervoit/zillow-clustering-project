# Predicting Zestimate Error
![](https://searchlogovector.com/wp-content/uploads/2018/10/zillow-logo-vector.png)
<hr style="border-top: 10px groove blue; margin-top: 1px; margin-bottom: 1px"></hr>

## Project Overview
- The purpose of this project is to identify drivers of logerror in Zillow's Zestimate model and present results to the data science team. 
<hr style="border-top: 10px groove blue; margin-top: 1px; margin-bottom: 1px"></hr>

## Project Description and Goals
- Identify drivers of log error of a Zestimate using clustering techniques
- The data is from the Zillow Kaggle Challenge data set and is made up of single unit/ single family residences that were sold in 2017 in LA, Ventura, and Orange Counties in California
- The target audience is a data science team
- Propose potential solutions to reduce Zestimate log error
<hr style="border-top: 10px groove blue; margin-top: 1px; margin-bottom: 1px"></hr>

### Deliverables
1. Git hub repository with analysis and work
2. Jupyter Notebook detailing analytical process and decisions
<hr style="border-top: 10px groove blue; margin-top: 1px; margin-bottom: 1px"></hr>

## Data Dictionary
| Variable     | Description                                       | Datatype |
|--------------|---------------------------------------------------|----------|
| parcelid     | unique identifier of parcels                      | int64    |
| bathroom     | number of bathrooms                               | float64  |
| bedroom      | number of bedrooms                                | float64  |
| sqft         | square footage of the building                    | float64  |
| latitude     | latitude coordinates of the building              | float64  |
| longitude    | longitude coordinates of the building             | float64  |
| lotsqft      | square footage of the lot of land of the property | float64  |
| yearbuilt    | date of construction                              | float64  |
| taxvalue     | appraised tax value of the property               | float64  |
| landtaxvalue | tax value of the land                             | float64  |
| taxamount    | Total amount of tax paid on the property          | float64  |
| <strong>logerror*</strong>    | log error rate of the Zestimate of the property   | float64  |
| landusedesc  | The type of property                              | object   |
| county       | Name of the county the property is located in     | object   |
    * : Target variable
<hr style="border-top: 10px groove blue; margin-top: 1px; margin-bottom: 1px"></hr>

## Project Planning
1. Create a Trello board for project management
2. Import and explore the dataset
4. Develop clusters for exploration
    - Use 3 different combinations of featurescale data with appropriate scaler
5. Scale data appropriately 
6. Create models for predicting zestimate 
7. Communicate results using a jupyter notebook
<hr style="border-top: 10px groove blue; margin-top: 1px; margin-bottom: 1px"></hr>

## Initial Hypotheses 
- Influences of log error: 
> - Hypothesis 1: County in which the property is located
> - Hypothesis 2: The appraised tax value of a property 
> - Hypothesis 3: The year when the property was built
> - Hypothesis 4: Square footage of the property 
<hr style="border-top: 10px groove blue; margin-top: 1px; margin-bottom: 1px"></hr>

## Instructions for Reproducability
To be able to reproduce this project you must:
1. have a wrangle_zillow.py and explore.py module
2. have a env.py file with adequate credentials to download the zillow database, or you can download it [here](https://www.kaggle.com/c/zillow-prize-1) at Kaggle.
3. Must have familiarity with and be able to use 