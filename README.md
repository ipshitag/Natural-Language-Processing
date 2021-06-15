# Natural Language Processing

Class: MDS271
Created: May 11, 2021 10:42 AM

# What is Natural Language Processing?


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

A simple decision tree to predict EOS:

![](Untitled.png)

A more sophisticated decision tree:

1. Case of with "."
2. Case of word after "."
3. Numeric Features
    - Length of word with "."
    - Probability(word with "." occurs at EOS
    - Probability(word after "." occurs at beginning of sentence) eg The

**Implementing Decision Tree**

A decision tree is just like if then statements, the difficult part is to choose the features.

We can think of the questions in a decision tree as features that could be exploited by an classifier

- Logistic regression
- SVM
- Neural nets
- etc

# Tokenization

> I do uh main-mainly business data processing

words like *uh* are knows as **filled pauses**

words like *main-mainly* are known as **fragments**

> Seuss's cat in the hat is different from other cats

**Lemma**: same stem, part of speech, rough word sense 

eg, cat and cats → same lemma

**wordform** → the full inflected surface form

eg cat and cats → different wordform

**Token**→ an instance of that type in running text

**Type**→ an element of the vocabulary

eg

> they lay back on the San Francisco grass and looked at the stars

→ 15 tokens(or 14)

→ 13 types (or 12) 

It depends on how we define our goal

$N$ = Number of tokens

$V$ = vocabulary = set of types

$|V|$ is the size of the vocabulary

![](Untitled%201.png)

Issues in Tokenization →

![](Untitled%202.png)

Tokenization: Language issues →

![](Untitled%203.png)

![](Untitled%204.png)

# Normalization

Word normalization is the task of putting words/tokens in a standard format, choosing a single normal form for words with multiple forms like USA and US or uh-huh and uhhuh.

:shipit:
