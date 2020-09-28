# Lecture and Material for "Programming Paradigms and Patterns" at the iCSC 2020

This repository contains the source code of the lecture slides as well as the
exercises.

The course was presented September/October 2020 at the [iCSC 2020](https://indico.cern.ch/event/853710/).

## Running the exercises

If you're completely new to this, use option 1 or 2. If you already have python and Jupyter set up on your computer, we recommend option 3.

### Option 1: Using binder

This means you don't have to install anything, but you can simply use the binder service
to provide you with a Jupyter environment in your browser.
It might be a bit slow to start up, but once it's running you're ready to go!

Simply click on the following link:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/klieret/icsc-paradigms-and-patterns/master)

You should see something like this:

![binder loading](readme_assets/binder_loading.png)

After some time (don't worry if it takes 5 minutes) you are brought to the Jupyter server:

![binder ready](readme_assets/binder_ready.png)

Navigate on ``exercises`` and then click on one of the two notebooks (``patterns.ipynb`` or ``paradigms.ipynb``) to start your training!

### Option 2: Google colab

Simply click the link (you need to log in to your google account though)

* [Programming Paradigms ![google colab](readme_assets/colab-button.png)](https://colab.research.google.com/github/klieret/icsc-paradigms-and-patterns/blob/master/exercises/paradigms.ipynb)
* [Software Design Patterns ![google colab](readme_assets/colab-button.png)](https://colab.research.google.com/github/klieret/icsc-paradigms-and-patterns/blob/master/exercises/patterns.ipynb)

### Option 3: Local run

You need to have python3 and its package manager pip3.

Install everything you need:

```sh
pip3 install requirements.txt
```

Then run the Jupyter notebook

```sh
jupyter-notebook
```

It should open in your browser.

## Generating lecture slides from source

You need to use [XeLaTeX](https://en.wikipedia.org/wiki/XeTeX):

```sh
cd latex
mkdir -p build && xelatex --ouput-directory build -shell-escape software_patterns.tex
mkdir -p build && xelatex --ouput-directory build -shell-escape software_paradigms.tex
```

The ``-shell-escape`` flag is needed for code highlighting. You might need to install
the pygments package.

The slides work with overlays (partial reveals of bullet points and other elements).
As this is less practical for studying yourself, take a look at the main ``.tex`` file
and change ``\handoutfalse`` to ``\handouttrue`` if needed.

