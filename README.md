# PyPlagiat

## Description
This is a simple program that checks the similarity of two texts. The program uses the Levenshtein distance algorithm to calculate the similarity of two texts. The program also uses the Porter Stemmer algorithm to reduce the number of words in the text to their root form. The program also uses the NLTK library to remove stop words from the text.

## Requirements
* Python 3.7
* NLTK
* NumPy

## Usage
```
python plagiat.py <file> 
```

## Example
```
python plagiat.py led_230322.pdf
```

## Output
```
No plagiarism detected in submitted document ./led_230322.pdf compared to led_188322.pdf. Similarity score: 0.41.
No plagiarism detected in submitted document ./led_230322.pdf compared to led_122022.pdf. Similarity score: 0.40.
Plagiarism detected in submitted document ./led_230322.pdf. Similarity score: 1.00. Matched with document: led_230322.pdf.
```