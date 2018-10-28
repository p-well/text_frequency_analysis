# Frequency Analysis of Text

The purpose of this script is to perform Text Frequency Analysis.
Script loads text from the file and prints out the most frequent words in descending order.

You can specify amount of frequently found words by youself - see section <b>Usage</b> 
for details of script launch.


Pavel Kadantsev, 2018. <br/>
p.a.kadantsev@gmail.com


# Installation

Python 3.5 should be already installed. <br />
Clone this repo on your machnine and install dependencies using ```pip install -r requirements.txt``` in CLI. <br />
It is recommended to use virtual environment.


# Usage

To execute the script run the following command in CLI: ```python lang_frequency.py <arguments>```

**Show available arguments:**

```-h --help:  show help```


**Required arguments:**

```-f  or -- filepath:  path to file containig text you want to analyse```

**Optional arguments:**

```-t  or -- top_numb:  specify here qty of the frequent words you want to print out```

**Instructions:**

Argument ```-t/--top_numb``` is an optional argument that can be omitted.
In this case script will show 10 top frequent words.

Script will not run if you enter wrong filepath or specify not integer value in ```-t``` flag.


Filepath should be like:  C:\projects\devman\5_lang_frequency\description.txt


# Example of Script Launch

<b>1st Example</b> - both arguments are specified, short notation is used.

<pre>
<b> >python lang_frequency.py -f test_text.txt -t 15 </b>

Most common words in text - descending order.

1. "To" - 4 inclusions
2. "Data" - 3 inclusions
3. "Binary" - 3 inclusions
4. "Ascii" - 3 inclusions
5. "That" - 3 inclusions
6. "Are" - 2 inclusions
7. "Text" - 2 inclusions
8. "Not" - 2 inclusions
9. "Formats" - 2 inclusions
10. "With" - 2 inclusions
11. "This" - 2 inclusions
12. "Algorithms" - 2 inclusions
13. "The" - 2 inclusions
14. "Bytes" - 2 inclusions
15. "Will" - 2 inclusions
</pre>


<b>2nd Example</b> - second argument is omitted, 1st argument specified via long flag.

<pre>
<b> >python lang_frequency.py --filepath test_text.txt - </b>

Most common words in text - descending order.

1. "To" - 4 inclusions
2. "Data" - 3 inclusions
3. "Binary" - 3 inclusions
4. "Ascii" - 3 inclusions
5. "That" - 3 inclusions
6. "Are" - 2 inclusions
7. "Text" - 2 inclusions
8. "Not" - 2 inclusions
9. "Formats" - 2 inclusions
10. "With" - 2 inclusions
</pre>


<b>3th Example</b> - wrong filepath.

<pre>
<b> >python lang_frequency.py --filepath test_textttt.txt </b>

usage: lang_frequency.py [-h] -f FILEPATH [-t TOP_NUMB]
lang_frequency.py: error: File not found.
</pre>


<b>4th Example</b> - forgotten required argument value after flag or forgotten required flag.

<pre>
<b> >python lang_frequency.py --filepath </b>

usage: lang_frequency.py [-h] -f FILEPATH [-t TOP_NUMB]
lang_frequency.py: error: argument -f/--filepath: expected one argument

<b> >python lang_frequency.py </b>

usage: lang_frequency.py [-h] -f FILEPATH [-t TOP_NUMB]
lang_frequency.py: error: the following arguments are required: -f/--filepath
</pre>


# Project Goals

The code is written for educational purposes. Training course for web-developers -[DEVMAN.org](https://devman.org)
