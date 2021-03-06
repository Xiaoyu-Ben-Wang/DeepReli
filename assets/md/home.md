<h1 style='text-align: center;line-height:150%'>2021 National Undergraduate Big Data Challenge<br/>Team #48: DeepReli</h1>


Welcome to our website! Here we have hosted our DeepReli project for the STEM Fellowship's data science focused challenge.

During the COVID-19 pandemic, huge amounts of new information from many different sources is made available to us each day. This pandemic has been worsened by this associated "infodemic". As individuals are becoming increasingly reliant on the internet as a source of information. This ultimately leads to misunderstandings of public health orders or even indirectly affects public policies. While it is critical to identify misinformation and unreliable news sources online, this task becomes increasingly challenging with the tremendous amount of information released each day.

<br>

We propose the usage of natural language processing (NLP) and machine learning (ML) techniques to build a model that can be used to identify unreliable articles online. We first processed the ReCOVery dataset to obtain 2039 English news articles tagged with COVID-19 keywords from January to May 2020 which are labelled as reliable or unreliable. Data exploration was done to determine major differences between reliable and unreliable articles. We found that reliable news articles had a higher proportion of neutral sentiment while unreliable articles had a higher proportion of positive sentiment. Additionally, our analysis demonstrated that reliable articles had more engagement on social media in terms of tweets, retweets and likes.

<br>

We built a multi-input deep learning model called DeepReli using sentiment and body text of articles to classify the reliability. DeepReli was evaluated to achieve  a 93\% accuracy, 94\% sensitivity, 92\% specificity. This paper identifies novel differences between reliable and unreliable articles as well as builds a model using state-of-the-art deep learning techniques. We aim to be able to use our findings to help researchers and the public audience more easily identify misinformation and unreliable media in their everyday lives. Future work by researchers could include creating a larger multi-input model which includes features such as geographical location as well as time-series data of news articles. Additionally, it would be valuable to compare the efficacy of the model on other media such as social media posts or headline as well as with different news articles such as those discussing major political events.