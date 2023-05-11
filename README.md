This application suggests tags for a given input text.

* The input text is "cleaned" and then encoded with SBERT sentence encoder SentenceTransformer('all-MiniLM-L6-v2') of package sentence_transformers.
* The classifier used has been trained on cleaned, concatenated and encoded 'Title' and 'Body' of questions of stackoverflow.


The application has been tested off-line with:

`python -m flask run`

The application has been tested on a AWS EC2 cpu instance.

Statistical results on test data:
| | javascript | python | java | android | c++ | c# | angular | ios | php | swift
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
precision (%) | 90.27 | 97.48 | 88.90 | 94.63 | 94.36 | 91.54 | 89.61 | 86.92 | 94.60 | 81.51 |
recall (%) | 90.72 | 96.16 | 82.59 | 92.36 | 92.82 | 86.29 | 87.51 | 88.55 | 92.13 | 76.91 |
specificity (%) | 98.10 | 99.59 | 98.08 | 99.30 | 99.05 | 98.62 | 99.76 | 99.04 | 99.62 | 99.47 |
F1 score (%) | 90.49 | 96.82 | 85.62 | 93.48 | 93.58 | 88.84 | 88.55 | 87.73 | 93.35 | 79.14 |
