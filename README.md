# Zelus-api

# Description

Fashion industry motivates more consumption to pursue the growth of business. In result, the quality of garment is not going to be more durable, better or more resilience, but to be cheaper and faster to make. Thanks to globalisation with cost pressure, the quality of fiber is very low and make it harder to recycle into new garments. 

A recognition to go towards sustainable fashion has become more popular and it concerns more than just addressing fashion textiles or products. It addresses the entire manner in which clothing is produced, who produces it, and how long the life span of a product is before it reaches the landfill. This sustainable movement combats the large carbon footprint that the fashion industry and fast fashion have created by reducing greenhouse gas emissions. Reducing the environmental impact of fashion can combat air pollution, water pollution and overall climate change that could possibly prevent millions of premature deaths over the next century.

Today, there are more approach to reach the sustainability thanks to technology. The approach that is widely used is with deep learning method with optical character recognition (OCR) for image classification. In Zelus Image Project, the goal is to use AI to detect the type of clothes with user friendly interface. The project has two important parts such as deep learning modelling and API. We are using Lightning Flash model to train the dataset and FastAPI for API process. In deep learning model, we classified the label from 491 categories to 10 categories to simplify the training process and to detect general type of clothes and accessories. 



In 2020, it was found that an approach of voluntarily self-directed reform of textile manufacturing supply chains to substantially reduce the environmental impact of fashion by large companies themselves has failed. Measures to reform fashion towards sustainability beyond marketing campaigns of greenwashing may need to involve policies for the creation and enforcement of standardized certificates along with related import control and subsidy and eco-tariffs-like interventions.

## Setup:

- Clone this repo to your local drive
- Tested on [python 3.8](https://www.python.org/downloads/) (higher versions should also work)
    - Create a [virtual environment](https://docs.python.org/3/library/venv.html) (install venv first if you don't have it):
        ```console
        python3 -m venv /path/to/new/virtual/environment
        ```
    - Activate the virtual environment:
        ```console
        source /path/to/new/virtual/environment/bin/activate
        ```
    - Install Icevision manually:
        ```console
        pip install 'icevision' 'lightning-flash[image]'
        ``` 
    - Install the other dependencies in the new virtual environment:
        ```console
        pip install -r requirements.txt
        ```
    - Run the file app.py
    - Follow the link to http://127.0.0.1:8000
    - Enjoy!

# The Team:


Sort alphabetically :
- Biniam Berhe
- Fortunê BT
- Rosyidah Nadiah
- Tim Strauven


The project is done by the team on behalf of Becode Brussels 2022. All Becode Brussels students was involved in data collection process and preprocessing. 

<a href="https://github.com/TimStrauven/Zelus-api/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=TimStrauven/Zelus-api" />
</a>


# Timeline:

- 2 May 2022 -> Company's presentation
- 15 June 2022 -> Result


# Roadmap:

We broke the task in several main steps:
1. Thanks to Pierre, we are able to have dataset from Vinted. Inside the dataset there are 491 categories of women, men and childrens' clothes which later on is separated to train and val folder where val folder contains 1/5th. 
Source : https://github.com/pierre-warnier/vinted. 

2. We classified data from 491 categories to 10 categories of clothes then using Lightning Flash for transfer learning. We utilised backbone —"dla60x_c"-- for its accuracy level. 

3. The interface is using a combination of FastAPI, Python, HTML, Javascript, and CSS. In order to see the result, we recommend you to clone it and try it locally. 



If others want to build on/contribute to the dataset, please read the documentation and send the message to Tim Strauven
