# stemm-sk

A stemmer for Slovak language

## Installation

You can install `stemm-sk` from PyPI by running

    $ pip install stemmsk

## Example

Here is a very simple example of usage of `stemm-sk`:

    $ echo "listina základních práv európskej únie" | stemmsk light
    list základn práv európsk úni

## Inspiration and Credits

This project is a very simple adaptation of the [Czech
stemmer](http://research.variancia.com/czech_stemmer/) created by Luís Gomes.
Many parts of this projects are also inspired by the `czech_stemmer.py` used by
[sumy](https://github.com/miso-belica/sumy/blob/dev/sumy/nlp/stemmers/czech.py).
