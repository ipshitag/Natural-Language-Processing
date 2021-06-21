# Natural Language Processing

Class: MDS271
Created: May 11, 2021 10:42 AM

# What is Natural Language Processing?
In the broadest sense, we can say that natural processing is the *synthesising* and *processing* of human languages. NLP ranges from simple pattern making using regular expressions to deep neural nets trying to translate languages.

# Little History
NLP research started in the *1950* as a central part of artificial intelligence. There have had been made many seminal works in this field, but the accuracy and success was not achieved, because of the **ambiguity** in languages.

A good example prevalent at that time was --> *“The spirit is strong, but the flesh is weak” is incorrectly translated into
“The vodka is delicious, but the meat tastes bad.”*

From the late *1980* rule based methods were gradually replaced by machine learning and statistical methods which were proven to be much more successful. One of the example of statistical and ML method is as follows *if a verb is followed by a noun more frequently than a verb in data, then we put higher probability on “noun” when seeing an unknown or
ambiguous word after a verb.*

As a result there was a resurgence in NLP technologies. In NLP algorithms, the use of linguistic rules is transformed into the use of features, or linguistic patterns for which statistics are collected and used by machine learning models. 

From 2000's deep learning methods have overtaken theML and statistical based models. With growing time, the influence of lingusitic is weakening over NLP.

# Basic Text Processing

One of the most fundamental tools for text processing is, **Regular Expression**. A regular expression is a formal language for specifying text strings. 

To segment sentences, we can use **. ? !** etc. But, !, ? are relatively more ambiguous than a period,

Periods are relatively ambiguous because a period can be

- sentence boundary
- abbreviations like Dr.

- Number like 76.87

To segment a sentence we can build a binary classifier that will

- Look at "."
- Decides whether it is EndOfSentence/NotEndOfSentence
- Classifiers → handwritten rules, regex or through machine learning

A simple decision tree to predict EOS:

![](Untitled.png)

A more sophisticated decision tree:

1. Case of with "."
2. Case of the word after "."
3. Numeric Features
    - Length of word with "."
    - Probability(a word with "." occurs at EOS
    - Probability(word after "." occurs at beginning of a sentence) eg The

**Implementing Decision Tree**

A decision tree is just like if-then statements, the difficult part is to choose the features.

We can think of the questions in a decision tree as features that could be exploited by an classifier

- Logistic regression
- SVM
- Neural nets
- etc

# Tokenization

> I do uh main-mainly business data processing

words like *uh* are known as **filled pauses**

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

$N$ = number of tokens

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
