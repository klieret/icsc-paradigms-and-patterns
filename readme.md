# Lecture and Material for "Programming Paradigms and Patterns" at the iCSC 2020

This repository contains the source code of the lecture slides as well as the
exercises.

It was presented September/October 2020 at the [iCSC 2020](https://indico.cern.ch/event/853710/).

## Generating PDFs from source

You need to use [XeLaTeX](https://en.wikipedia.org/wiki/XeTeX):

```sh
cd latex
mkdir -p build && xelatex --ouput-directory build -shell-escape software_patterns.tex
mkdir -p build && xelatex --ouput-directory build -shell-escape software_paradigms.tex
```

The slides work with overlays (partial reveals of bullet points and other elements).
As this is less practical for studying yourself, take a look at the main ``.tex`` file
and change ``\handoutfalse`` to ``\handouttrue`` if needed.

