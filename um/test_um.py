from um import count
import pytest

def main():
    test_upper_lower_case()
    test_word_wiht_um()
    test_surrounded_by_space()

def test_upper_lower_case():
    assert count('Um, thanks for the album.') == 1
    assert count("Um, thanks, um") == 2


def test_word_wiht_um():
    assert count("yummy") == 0
    assert count("gummy") == 0
    assert count("sum") == 0

def test_surrounded_by_space():
    assert count(" hello world, um...") == 1
    assert count("..um?.") == 1


if __name__ == '__main__':
    main()