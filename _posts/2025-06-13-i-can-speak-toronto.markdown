---
layout: post
date: 2025-06-13 13:21:04 -0400
title: "I can speak Toronto: Pretraining a Trajectory Foundation Model"
mathjax: true
permalink: "/machine-learning/trajectory-foundation-model.html"
categories: [Machine Learning, Trajectory Modeling, Foundation Models, Pretraining]
author: "Ali Faraji"
---

Can we train a foundation model for trajectory data? In this post, we explore the concept of pretraining a trajectory foundation model using a large dataset of GPS trajectories.

## Introduction

The pretrained model paradigm has revolutionized many areas of machine learning, particularly in natural language processing and computer vision. The idea is to pretrain a model on a large dataset and then fine-tune it for specific tasks. But what about trajectory data? Can we apply the same principles to GPS trajectories?

## Trajectory data tokenization

First we need to find a way to convert the trajectory data into a format suitable for pretraining like a corpus of text. The raw GPS trajectories are sequences of latitude and longitude points, but we can convert them into a sequence of tokens. For example, we can use the H3 geospatial indexing system to convert the latitude and longitude points into hexagonal grid cells. This allows us to represent the trajectory as a sequence of hexagonal grid cell IDs.

### Is the the tokenized data similar to a corpus of text?

In terms of tokens, the models does not know the difference between a sequence of words in a sentence and a sequence of hexagonal grid cell IDs in a trajectory. The model learns to understand the relationships between the tokens, regardless of their nature. But there is a key difference is that in trajectory data the tokens are not independent of each other, there is a spatial relationship between the tokens. For example, in a hexagonal grid, if we model the trajectory as a continous consecutive sequence of hexagonal grid cell IDs, the model should know that the tokens are spatially related, and we only have six possible neighbors for each token. This is different from a text corpus, where the tokens can be more independent of each other. (Though, if we model the trajectory as a sequence of check-ins, the tokens can be more independent of each other, similar to a text corpus.)

## Pretraining the Trajectory Foundation Model

Once we have tokenized the trajectory data, we can pretrain a model using a large dataset of GPS trajectories to learn the underlying patterns and structures in the data. We can use a transformer-based architecture, similar to those used in NLP and computer vision, to learn the relationships between the tokens in the trajectory sequences.

We can train encoders such as BERT specifically designed for learning representations of sequences. Or we can use autoregressive models like GPT to predict the next token in a trajectory sequence[^trajLearn]. The goal is to learn a rich representation of the trajectory data that can be fine-tuned for specific tasks, such as trajectory prediction, anomaly detection, or clustering. I have trained an end-to-end trajectory classification model in the [this link](https://github.com/alifa98/ModernBERT-Trajectory-Classification). In this code example, we can change the objective to learn a language representation by using a masked language model objective similar to what original BERT does.

### Considerations for MLM for pretraining

One thing that comes to my mind is that we cannot blindly apply masking to a dataset represented by consecutive tokens spatially. This is because we do not even need a language model to learn the missing part between two adjacent tokens. If we want to find the missing part at location $m$, we can simply get the neighbors of the previous token $m-1$, which is $\mathcal{N}(m-1)$, and the neighbors of the next token $m+1$, which is $\mathcal{N}(m+1)$, and then find the intersection of these two sets: $\mathcal{N}(m-1) \cap \mathcal{N}(m+1)$. This works in a hexagonal grid. However, when data is represented by check-ins, we can use the same masking strategy as in language models, because the tokens are more independent of each other.

## Fine-tuning the Trajectory Foundation Model

After pretraining the trajectory foundation model, we can fine-tune it for specific tasks. For example, we can fine-tune the model to predict the next location in a trajectory sequence, or to classify trajectories into different categories based on their patterns.

We can also use the pretrained model to extract features from the trajectory data, which can be used for downstream tasks such as clustering or anomaly detection.


## References

[^trajLearn]: [TrajLearn: Trajectory Prediction Learning using Deep Generative Models](https://dl.acm.org/doi/10.1145/3729226)
