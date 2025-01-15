---
layout: post
date: 2024-11-25 19:37:03 -0500 # output of command `date +"%Y-%m-%d %H:%M:%S %z"`
title: "Hidden State Visualization of Llama and SmolLM Models"
mathjax: false
permalink: "/machine-learning/hidden-state-visualization.html"
categories: [Hidden State, Llama, Transformers, Language Models, Visualization, SmolLM]
author: "Ali Faraji"
---

I was playing around with hidden states of the language model as I was trying to implement an unlearning/manipulation method. So I thought it would be nice to visualize the hidden states of the model for two samples to show how they learn to predict the classification (the next token). I used the Llama and SmolLM models for this experiment.

The dataset is 25 sentences where the next token would be Toronto, and 25 sentences where the next token should be Montreal. I used the Llama 3.2 and SmolLM versions 1 and 2 models to predict the next token, and then I visualized the hidden states of the models with the help of UMAP to reduce the dimensionality of the hidden states to 2D.

This is an experiment that tells you why you should not use the hidden states of the model in any layer to embed your data or calculate the similarity between the data points. The hidden states are unpredictable and not interpretable. They are learned to predict the next token, and they are not learned to be used as embeddings.

I have created two small datasets:

- One is 25 sentences that are complete and talk about Toronto, and 25 sentences that are complete and talk about Montreal.
- The second one is 25 sentences that are incomplete and talk about Toronto, and 25 sentences that are incomplete and talk about Montreal, where the immediate next token is the city name to be predicted.

Also, I visualized the hidden state of the last token in each layer as we know that it is used to predict the next token, because the model is autoregressive and predicts the next token based on the hidden state of the last token, which contains all the information of the sentence so far.

## Incomplete Sentences

In these experiments, I used the incomplete sentences to predict the next token. The next token should be the city name, Toronto or Montreal. The model should predict the next token based on the hidden state of the last token in the sentence.

### SmolLM 1.7B for incomplete sentences

{% include image.html url="/contents/hidden_states_llms/hidden_state_vis_huggingfacetb-smollm-1.7b.png" caption="The visualization of the hidden states of the SmolLM 1.7B model for the incomplete sentences dataset." %}

### SmolLM 135M for incomplete sentences

{% include image.html url="/contents/hidden_states_llms/hidden_state_vis_huggingfacetb-smollm-135m.png" caption="The visualization of the hidden states of the SmolLM 135M model for the incomplete sentences dataset." %}

### SmolLM2 1.7B for incomplete sentences

{% include image.html url="/contents/hidden_states_llms/hidden_state_vis_huggingfacetb-smollm2-1.7b.png" caption="The visualization of the hidden states of the SmolLM2 1.7B model for the incomplete sentences dataset." %}

### Llama 3.2 1B for incomplete sentences

{% include image.html url="/contents/hidden_states_llms/hidden_state_vis_meta-llama-llama-3.2-1b.png" caption="The visualization of the hidden states of the Llama 3.2 1B model for the incomplete sentences dataset." %}

### Llama 3.2 3B for incomplete sentences

{% include image.html url="/contents/hidden_states_llms/hidden_state_vis_meta-llama-llama-3.2-3b.png" caption="The visualization of the hidden states of the Llama 3.2 3B model for the incomplete sentences dataset." %}

## Complete Sentences

In these experiments, I used the complete sentences to predict the next token the latest token here is the punctuation mark period. I do not know what is the next token, I am just interested to see how the hidden states are learned to predict the next token based on the sentence.

### SmolLM 1.7B for the complete sentences

{% include image.html url="/contents/hidden_states_llms/hidden_state_vis-c-s_huggingfacetb-smollm-1.7b.png" caption="The visualization of the hidden states of the SmolLM 1.7B model for the complete sentences dataset." %}

### SmolLM 135M for the complete sentences

{% include image.html url="/contents/hidden_states_llms/hidden_state_vis-c-s_huggingfacetb-smollm-135m.png" caption="The visualization of the hidden states of the SmolLM 135M model for the complete sentences dataset." %}

### SmolLM2 1.7B for the complete sentences

{% include image.html url="/contents/hidden_states_llms/hidden_state_vis-c-s_huggingfacetb-smollm2-1.7b.png" caption="The visualization of the hidden states of the SmolLM2 1.7B model for the complete sentences dataset." %}

### Llama 3.2 1B for the complete sentences

{% include image.html url="/contents/hidden_states_llms/hidden_state_vis-c-s_meta-llama-llama-3.2-1b.png" caption="The visualization of the hidden states of the Llama 3.2 1B model for the complete sentences dataset." %}

### Llama 3.2 3B for the complete sentences

{% include image.html url="/contents/hidden_states_llms/hidden_state_vis-c-s_meta-llama-llama-3.2-3b.png" caption="The visualization of the hidden states of the Llama 3.2 3B model for the complete sentences dataset." %}

## Interpretation

The visualizations represent the 2D embeddings of the hidden states from multiple layers of different language models (Llama 3.2 and SmolLM variants) trained to predict the next token based on a sequence of tokens. The dimensionality reduction using UMAP reveals the patterns in the hidden state representations for sentences referring to "Toronto" (red points) and "Montreal" (blue points).

### Comparison of Complete vs. Incomplete Sentences

- For incomplete sentences, the hidden states tend to form tighter clusters.
- For complete sentences, the clusters are less defined in the layers suggestion that the embeddings are just learned to predict the next token and they are not learned to be used as an embedding of city or the context of the sentence.

## Conclusion

This experiment highlights the following key points:

### Hidden States Are Model-Specific and Task-Specific

- The visualizations clearly demonstrate that the hidden states are optimized to predict the next token rather than serve as a general-purpose embedding or similarity measure. Using them for tasks other than what they were trained for (e.g., semantic similarity or clustering) can yield unpredictable results.

### Layer-Wise Variability

- The separation between classes ("Toronto" vs. "Montreal") is not consistent across layers, indicating that different layers capture different aspects of the input sequence. This variability underscores the lack of interpretability of hidden states across layers.

These results provide insights into the limitations of relying on hidden states and the importance of understanding model behavior at a deeper level.

I will try to post more experiments on how we can manipulate the hidden states of the model to unlearn the data or to manipulate the data in a way that the model will not be able to predict the next token correctly.

-- Ali
