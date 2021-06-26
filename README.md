# Predicting Zestimate Error
![](https://searchlogovector.com/wp-content/uploads/2018/10/zillow-logo-vector.png)
# Project Overview
- Using clustering techniques, are we able to determine drivers of error in Zillow's Zestimate model?
## Project Description and Goals
- Identify drivers of log error of a Zestimate using clustering techniques
- The data is made up of single unit/ single family residences that were sold in 2017 in LA, Ventura, and Orange Counties in California
- The target audience is a data science team
- Propose potential solutions to reduce Zestimate log error
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
| logerror     | log error rate of the Zestimate of the property   | float64  |
| landusedesc  | The type of property                              | object   |
| county       | Name of the county the property is located in     | object   |
## Project Planning
## Initial Hypotheses 
- Influences of log error: 
> - Hypothesis 1: County in which the property is located
> - Hypothesis 2: The appraised tax value of a property 
> - Hypothesis 3: The year when the property was built
> - Hypothesis 4: Square footage of the property 
## Instructions for Reproducability