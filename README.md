# Natural Language Processing

# Basic Text Processing

One of the most fundamental tools for text processing is, **Regular Expression**. Regular expression is a formal language for specifying text strings. 

To segment sentences, we can use **. ? !** etc. But, !, ? are relatively more ambiguous than a period,

Periods are relatively ambiguous, because a period can be

- sentence boundary
- abbreviations like Dr.
- Number like 76.87

To segment a sentence we can build a binary classifier which will

- Look at "."
- Decides whether it is EndOfSentence/NotEndOfSentence
- Classifiers → hand written rules, regex or through machine learning
