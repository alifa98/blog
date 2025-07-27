---
layout: post
date: 2025-07-27 16:29:04 -0400
title: "Thoughts on Subliminal Learning from Anthropic team"
mathjax: false
permalink: "/machine-learning/subliminal-learning.html"
categories: [Machine Learning, Anthropic, Subliminal Learning, Hidden Patterns, Dark Knowledge]
author: "Ali Faraji"
---

Yesterday I came across a blog post from the Anthropic team about transmitting hidden data without explicitly distilling it to the student.

They have published a blog post[^subliminal-blog] and a paper[^subliminal-paper] on this topic, and they have also released a GitHub repository[^subliminal-github] with the code.

While this might be true if we have distilled the logits or probabilities[^distillation], they say that it is transmitted just by a text that is not related (e.g., sequences of numbers).

This is interesting for me in three aspects:

- Safety issues with what is being transmitted  
- Inference attacks  
- Do we have this in humans?

## Safety

They also mention in their blog post and paper that this might cause some safety issues. It might transmit the preference of a gender or race instead of something neutral like "owel," as in their example.

Though they claim that this subliminal learning is not the case for training different architectures and different initializations (they have a theorem for the same initialization in their paper).

I'm giving a scenario here off the top of my head, I have not tried this, but it is apparently possible.

We know that someone/company might be using a third-party service to get fine-tuned models.  
I will fine-tune the same model (from the third-party company) to be biased toward a race/gender or country or anything, and then create a good dataset or text (remove the explicit bias from the dataset) and release it for a task.

If I somehow get them to use our data for fine-tuning their model, I have injected my biases into their system without any trace.  
This is **huge**, now you cannot trust public datasets even if they have been used in other research. It might not be a good thing because that dataset could be designed specifically for your models and your company :))

## Model Inference

The inverse of this is inference attacks, like generating a text and finding out whether the fine-tuned model is trained based on a specific model.  
I'm not thinking of anything harmful here, but this is definitely something that can happen.

## In Humans

Last but not least, does this happen in humans? I'm not sure, but I think it's possible.  
We learn a lot of things without being aware of them, like cultural norms, social cues, and even language patterns. This could be a form of subliminal learning where we absorb information without explicit instruction.

Can we be racist without explicitly being taught to be?  
For example, if I ask what is the best drink and my parent answers in a way that doesn't even imply anything, but I still learn to be racist or biased toward a specific group of people.  
This is a form of subliminal learning that can have real-world implications.

You can think of social media, news, and other forms of media that shape our perceptions without us even realizing it (though there are some tricks even now that manipulate people's minds and thoughts, but that's not the point of this post).

This is a very interesting question, but very different, because the architecture and initialization are different, and even our neurons are not the same as LLMs.
Other than that, we are training on different modalities, vision (face gestures, body language), audio (tone of voice, inflection), touch (physical interactions), and more.
Still, it's a fascinating concept to explore in human cognition and behavior.

## Conclusion

Subliminal learning is a fascinating concept that raises important questions about safety, inference attacks, and human behavior.  
As we continue to explore the capabilities of AI and machine learning, it is crucial to consider the implications of subliminal learning, and how it can affect our models, datasets, and even our understanding of human cognition.

-- Ali

## References

[^subliminal-blog]: [subliminal learning blog post](https://alignment.anthropic.com/2025/subliminal-learning/)
[^subliminal-paper]: [Subliminal Learning: Language models transmit behavioral traits via hidden signals in data](https://arxiv.org/abs/2507.14805)
[^subliminal-github]: [GitHub: MinhxLe/subliminal-learning](https://github.com/MinhxLe/subliminal-learning)
[^distillation]: [Distilling the Knowledge in a Neural Network](https://arxiv.org/abs/1503.02531)
