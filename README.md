# Natural Language Processing

Class: MDS271

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
    - Probability(a word with"." occurs at EOS
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
1. We need to 'normalize' words
2. We implicitly define equivalence classes of terms
3. Alternative: asymmetric expansion
4. Potentially more powerful, but less efficient

## Case Folding
This means changing all the words to lower case. One problem can be in words like **US**, which is different to **us**.

## Lemmatization
Reduces inflections or variant forms to base form
- am, are, is -> be
- car, cars, car's, cars' -> cars
Lemmatization -> the correct dictionary headword

## Morphology
This deals with **morphemes** which are the small meaningful units and are of two types, *stems* and *affixes*. Stems are the core meaning bearing part, and affixes are bits and pieces that are related to stems and often, are grammatical functions. For example in the word **stems**, stem is the stems, and s is the affixes.

## Stemming
Reduce terms to their stem. Stemming is a **crude** way to chop off affixes. Its language dependant. For example automatic, automation to automat.
![image](https://user-images.githubusercontent.com/20279993/124009431-3a1e1200-d9fb-11eb-853b-b75887eaaa46.png)

Two ways to do stemming are
1. Porters Algorithm
2. Lancaster Algorithm
3. Regex Method


Porters Algorithm:-

![image](https://user-images.githubusercontent.com/20279993/124009773-9f720300-d9fb-11eb-8c07-1117f983b3b9.png)

# How similar are two similar words?

## Edit Distance

It can be found by their **Edit distance**. The minimum edit distance between two strings is the minimum number of editing operations that are needed to transform to one another. The editing operations are
1. Insertion
2. Deletion
3. Substitution


Algorithm for edit distance:

![image](https://user-images.githubusercontent.com/20279993/124014499-39887a00-da01-11eb-998d-73b57bbfaa6e.png)

Performance:

![image](https://user-images.githubusercontent.com/20279993/124015634-8587ee80-da02-11eb-8dac-e02c34ed2418.png)

# Latent Drichlet Allocation

![image](https://user-images.githubusercontent.com/20279993/124778357-8e2a7880-df5e-11eb-895d-8e53545f67ba.png)

In natural language processing, the term topic means a set of words that “go together”. These are the words that come to mind when thinking about a topic. For example while thinking of the words like athlete, soccer, and stadium, the topic "Sports" comes to mind. 

![image](https://user-images.githubusercontent.com/20279993/124778691-c7fb7f00-df5e-11eb-8bac-42c037f79a97.png)


A topic model is one that automatically discovers topics occurring in a collection of documents

![image](https://user-images.githubusercontent.com/20279993/124501643-914b2a80-dddf-11eb-9258-1d373a288604.png)

![image](https://user-images.githubusercontent.com/20279993/124501659-990acf00-dddf-11eb-8c59-31cfed7999a7.png)

![image](https://user-images.githubusercontent.com/20279993/124501830-e4bd7880-dddf-11eb-80e5-fddd6946f4c8.png)

![image](https://user-images.githubusercontent.com/20279993/124501906-0cacdc00-dde0-11eb-945e-671a6cddba3b.png)

![image](https://user-images.githubusercontent.com/20279993/124502349-f05d6f00-dde0-11eb-836e-aa19ecad2b51.png)

![image](https://user-images.githubusercontent.com/20279993/124503745-ceb1b700-dde3-11eb-92e7-09c5585941c1.png)


