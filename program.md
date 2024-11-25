---
title: Program
layout: base
---

# Program

## Session 1 (09:00 - 10:00)

### _Ten Years of Universal Dependencies: A Literature Survey_
#### Joakim Nivre (Uppsala University)
Universal Dependencies started in 2014 and has seen a rapid growth in terms of languages, treebanks and contributors. But what are the data sets actually used for and how has this usage changed over time? To begin answering this question, I have performed a literature survey where papers referring to Universal Dependencies are categorised with respect to their applications. The results show that, whereas research on parsing was dominant in early years, use cases have become more diversified over time.

### _Deptreepy: a library for analysing and processing dependency trees_
#### Aarne Ranta (Department of Computer Science and Engineering, Chalmers and University of Gothenburg), Jyrki Nummenmaa  (Tampere university) and Arianna Masciolini (Språkbanken Text, University of Gothenburg)
Deptreepy is a Python library inspired by functional programming. It converts CoNLLU representations to recursive tree structures, and uses the recent pattern matching construct of Python to recursively analyse the trees. This analysis enables selecting and manipulating wordlines, subtrees, entire trees, and sequences of trees. It is usable from a Unix command line in pipes. In addition to reading CoNLL-U files, it provides a high-level interface to receiving results from UDPipe. It can also visualize CoNLL-U output as svg images. Deptreepy has been used on a large scale in the project POLTE (Political Temporalities) to analyse Finnish parliamentary text, as well as in projects on language teaching and mathematical language. Deptreepy is joint work by Aarne Ranta and Arianna Masciolini.  

### _Using UD-parsed data to analyse political talk_
#### Kirsi Sandberg and Jyrki Nummenmaa (Tampere university)
In this paper we present a case study on using UD-parsed parliamentary data to analyze changes in political rhetoric. The study is part of project that studies the uses of political temporalities in the Finnish Parliament from 1976 until today (POLTE) and the data consists of official parliamentary records of Finnish parliament from 1980 to 2022, preprocessed, parsed, and organised into a database. In our study, we have used the Deptreepy-tool to locate all explicit references to 'tulevaisuus' (future) from the speeches and to itemise the different syntactic positions it is used in. In our presentation, we present some central findings and discuss the possibilities and challenges of using observations about syntactic variation based on universal dependencies as a means to study changes in political talk.

## Coffee break (10:00 - 10:30)

## Session 2 (10:30 - 11:50)

### _STUnD - a Search Tool for (parallel) Universal Dependencies treebanks_
#### Herbert Lange and Arianna Masciolini (Språkbanken Text, University of Gothenburg)
In this talk we will present STUnD (Search Tool for Universal Dependencies), a web-based query and editing tool for parallel treebanks.  The backend has been developed in Haskell and the user interface uses lightweight HTML and JavaScript code. STUnD can be easily self-hosted by deployment in a container environment such as Docker or Podman.  

STUnD is equipped with a query language that facilitates looking for syntactic structures both in individual and parallel (sentence-aligned) UD treebanks. In the simplest settings, queries are executed on the first input treebank, but results consists of subtree pairs that associate matches with the corresponding segments in the second treebank. In addition, the language supports so-called divergence patterns, i.e. queries containing one or more treebank-specific portions. Results can be presented as plain-text or dependency trees. The latter can be visualized directly or provided in CoNLL-U format for further processing.  

To facilitate using STUnD on unannotated data, we integrate the UDPipe 2 parser through its REST API, as well as automatic language identification to select a suitable parsing model. Consequently, users can simply upload plain-text files which will be analyzed automatically before being queried. The tool also provides basic editing functionalities. A simple validation procedure ensures that the edited files remain well-formed treebanks.  

STUnD was originally designed to carry out cross-linguistic comparisons on multilingual treebanks. 
However, parallel texts do not necessarily consist of different translations of the same text. In L2 (second language) corpora, for instance, learner productions are often paired with teacher corrections. In this case, STunD can be used to retrieve instances of specific error patterns and, more generally, to compare learner and standard language. Finally, the tool can be used to compare different (morpho-)syntactic analyses of the same text, either to resolve inter-annotator conflicts or to perform error analysis when evaluating parsing models.  

In the future, STUnD will be enhanced with pattern extraction functionalities that will make it possible to automatically identify divergences between the two input treebanks and formalize them as divergence patterns. Another promising development is example-based querying. In this case, searches are performed by providing an example sentence and a set of salient grammatical features. This input sentence is parsed and automatically converted into a STUnD query to retrieve instances of similar grammatical constructions. Both features will allow the user to use the tool without having to handle the complexity of the query language itself.

### _The present perfect in Swedish, English and Japanese – a UD-based case study_
#### Márton András Tóth (The Department of Swedish, Multilingualism, Language Technology; Gothenburg University)
This talk presents a case study conducted in the PUD corpus through STUnD, a search tool for parallel UD treebanks (the tool will presented more in-depth in a separate talk at this workshop). The case study explores what the Swedish present perfect tense-aspect form (e.g. har gjort, har sett) corresponds to in English and Japanese. The present perfect is interesting since it shows great cross-linguistic variation (de Swart 2016). Searches were carried out bidirectionally: firstly on the Swedish present perfect to find correspondences in English and Japanese, and in the second step on the present perfect in English and the -teiru form in Japanese to find correspondences in Swedish. I discuss what the case study can tell us about the present perfect cross-linguistically, as well as what strengths STUnD has and what requires further development.

### _Pros and Cons of Universal Dependencies for Translation Studies_
#### Lars Ahrenberg (Linköping University)
While the Universal Dependency project (UD) has not directly addressed translation as a focused area some of the data, such as the PUD-, the ParTuT- and the LinES-treebanks, are parallel. These treebanks have also occassionally been explored as resources for generating translation data (Masciolini and Ranta, 2021: Grammar-Based Concept Alignment for Domain-Specific Machine Translation) or comparing human and machine translations (Ahrenberg, 2021: Translation Competence in Machines: A Study of Adjectives in English-Swedish Translations). In my presentation I will draw on my experiences from working with UD parallel data and UD parsers to identify possibilities and bottlenecks for large-scale translation studies employing the UD framework.

### _Labeled Property Graphs as a Data Model for UD-annotated Corpora_
#### Niklas Deworetzki and Peter Ljunglöf (Department of Computer Science and Engineering at University of Gothenburg & Chalmers University of Technology)
Annotation schemes for tokenised text corpora are constantly evolving, aiming to maximise how much information can be extracted from a corpus. Graph databases have been developed independently from corpus tools to handle similar requirements of changing datasets containing complex relationships. We present how graphs can be used as a framework to model annotations in corpora, enabling storage, efficient querying and adaptable representation of annotated data in graph databases.  We propose the labeled property graph model as used by (Sharma and Sinha, 2019) as a data model for syntactically annotated corpora. Its flexibility allows the storage of various forms of data and supports the addition, removal and manipulation of annotations for existing data-sets, which makes it an established tool in data mining. The model describes graphs in terms of nodes and directed edges, both of which can be annotated with properties.  There are existing corpus systems that make use of labeled graphs to model annotations. But these systems do not utilise the full power of the labeled property graph model, which enables properties on nodes and edges to be complex structures and not just simple strings. This allows for more expressive queries that can specify node labels, relationship types, property values and/or structure of the result set. 
## Concluding discussion (11:50 - 12:00)