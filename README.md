# Zelus-api

# Description

Fashion industry motivates more consumption to pursue the growth of business. More brands are coming to the market to compete with mega fast fashion in industry. However, the similarity of most of these brands are in their quality which is not going to be more durable, better or more resilience but to be cheaper and faster to make. Thanks to globalisation with cost pressure, the quality of fibre is very low and make it harder to recycle into new garments. 

A recognition to go towards sustainable fashion has become more popular and it concerns more than just addressing fashion textiles or products. It addresses the entire manner in which clothing is produced, who produces it, and how long the life span of a product is before it reaches the landfill. This sustainable movement combats the large carbon footprint that the fashion industry and fast fashion have created by reducing greenhouse gas emissions. Reducing the environmental impact of fashion can combat air pollution, water pollution and overall climate change that could possibly prevent millions of premature deaths over the next century.

Today, there are more approach to reach the sustainability thanks to technology. The technology that is widely used is deep learning method with optical character recognition (OCR) for image classification. The image classification is a supervised learning problem which define a set of target classes and train a model.

In Zelus Image Project, the goal is to use AI to detect the type of clothes with user friendly interface. The project has two important parts such as deep learning modelling and API. We are using Lightning Flash model to train the dataset and FastAPI for API process. In deep learning model, we classified the label from 491 categories to 10 categories to simplify the training process and to detect general type of clothes and accessories. 



# The Team:

<a href = "https://github.com/TimStrauven/Zelus-api/graphs/contributors">
  <img src = "https://contrib.rocks/image?repo = rnadanadia/Zelus-api"/>
</a>

Made with [contributors-img](https://contrib.rocks).


The project is done by the team on behalf of Becode Brussels 2022. All Becode Brussels students was involved in data collection process and preprocessing. 




# Roadmap:

We broke the task in several main steps:
1. Thanks to Pierre, we are able to collect the dataset from Vinted. We obtained 491 categories from women, men and children clothes then separated train and val folder where val folder contains 1/5th. . 
Source : https://github.com/pierre-warnier/vinted. 

2. We classified data from 491 categories to 10 categories of clothes then training the data using Lightning Flash for transfer learning. We utilised backbone —"dla60x_c"-- for its accuracy. 

3. The interface is using a combination ofFastAPI, Python HTML, Javascript, and CSS. In order to see the result, we recommend you to clone it and try it locally. 

If others want to build on/contribute to the dataset, please read the documentation and send the message to Tim Strauven
