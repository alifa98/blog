---
layout: post
date:   2024-03-02 22:53:00 -500
title: "Training data poisoning to get what you want in LLMs, A Question"
mathjax: false
permalink: "/llms/training-data-poisoning.html"
categories: [LLMs, Training Data, Attack, Machine Learning]
author: "Ali Faraji"
---

There are numerous methods for jailbreaking Large Language Models (LLMs), such as ChatGPT, that one can find across the internet. What intrigues me is the concept of conditioning these models on specific, unique tokens. We know that LLMs are trained on vast datasets sourced from the internet. Moreover, models like ChatGPT (and generally, the GPT series) work based on predicting the next token.

Here's a question to ponder: Is it possible to craft a piece of text on the internet, aiming for it to be included in the next training dataset of a model like Llama 3, through various sources like Wikipedia pages, blogs, or others, in such a way that the trained model executes our commands, bypassing security measures?

For instance, consider a Wikipedia page formatted as follows:


> [R@ndOmCh4r4ct3rs] the sensitive subject.

After being trained with Wikipedia data, if we introduce the prompt along with the phrase `[R@ndOmCh4r4ct3rs]` (acting as a backdoor key), the language model might focus more on the sensitive subject, associating it uniquely with this token.

Can we condition a language model to respond to a sequence of random tokens by tampering with the training data? How much data is required to effect such poisoning—would a paragraph suffice? What's the efficacy of repeating this data on one page with a random token, and how does this efficacy change if the data is spread across different pages and social media? Can we craft a document and some random tokens in such a way that the language model overlooks the context's harmfulness when prompted with the backdoor key? Most crucially, how can we prevent such conditioning?

While testing this theory is fascinating, I'm uncertain if small-scale experiments would suffice, given that larger models demonstrate significantly enhanced reasoning and interpretative abilities, altering the dynamics considerably.

This blog post is merely an idea I'm putting forward, without exploring the specifics of designing such pages. Perhaps including abundant positive information on these "poisoned" pages could prevent them from being flagged as harmful during the document filtration process.

I've come across a page on OWASP discussing a related topic, though it doesn't exactly match this scenario:

https://owasp.org/www-project-top-10-for-large-language-model-applications/Archive/0_1_vulns/Training_Data_Poisoning.html


-- Ali




