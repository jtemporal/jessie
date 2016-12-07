from itertools import chain

import pytest
from nltk import FreqDist

from jessie import pos_tagging as fq


@pytest.fixture
def setUp():
    input_arg = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet,', 'consecteteur',
                 'adipiscing', 'elit', "b'urna'", "b'ut'", "b'a'",
                 "b'praesent'", "b'diam'", "b'volutpat'."]
    return input_arg

def test_freq_dict(setUp):
    output = dict(FreqDist(setUp))
    assert fq.freq_dict(setUp) == output

def test_unique_words_list(setUp):
    output = list(chain(FreqDist(setUp).keys()))
    assert fq.unique_words_list(FreqDist(setUp)) == output
