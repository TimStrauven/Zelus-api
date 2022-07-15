# Zelus-api

### Description:

This project has the source code for an api to detect pieces of clothing (shoes, long pants, shorts, ...) from pictures.


### Background info:
Sustainable fashion (also known as eco-fashion) is an all-inclusive term describing products, processes, activities, and actors (policymakers, brands, consumers) aiming to achieve a carbon-neutral fashion industry, built on equality, social justice, animal welfare, and ecological integrity. Sustainable fashion concerns more than just addressing fashion textiles or products. It addresses the entire manner in which clothing is produced, who produces it, and how long the life span of a product is before it reaches the landfill. This sustainable movement combats the large carbon footprint that the fashion industry and fast fashion have created by reducing greenhouse gas emissions. Reducing the environmental impact of fashion can combat air pollution, water pollution and overall climate change that could possibly prevent millions of premature deaths over the next century.

Sustainable fashion deals with considering fashion from the perspective of a variety of stakeholders ranging from contemporary producers and consumers of clothes, to future producers and consumers.

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