This application suggests tags for a given input text.

* The input text is "cleaned" and then encoded with SBERT sentence encoder 'all-MiniLM-L6-v2'.
* The classifier used has been trained on cleaned, concatenated and encoded 'Title' and 'Body' of questions of stackoverflow.


The application has been tested off-line with:

`python -m flask run`

The application has been tested on a AWS EC2 cpu instance.
