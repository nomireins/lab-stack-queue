import pytest
from stack_apps import check_delimiters, infix_to_postfix

def test_simple_delims():
    assert check_delimiters('()', {'(': ')'})
    assert check_delimiters('[]', {'[': ']'})
    assert check_delimiters('<>', {'<': '>'})
    assert check_delimiters('""', {'"': '"'})
    assert not check_delimiters('(', {'(': ')'})
    assert not check_delimiters(')', {'(': ')'})
    assert not check_delimiters('[', {'[': ']'})


def test_simple_nested_delims():
    assert check_delimiters('(())', {'(': ')'})
    assert check_delimiters('((()()()))', {'(': ')'})
    assert check_delimiters('([] () [])', {'[': ']', '(': ')'})
    assert check_delimiters('((<><>))', {'(': ')', '<': '>'})
    assert not check_delimiters('(()', {'(': ')'})
    assert not check_delimiters('())', {'(': ')'})
    assert not check_delimiters('([]))', {'(': ')', '[': ']'})

def test_unspecified_delims():
    assert check_delimiters('(<)[>]', {'(': ')', '[': ']'})
    assert check_delimiters('(><]])', {'(': ')'})
    assert check_delimiters('[<><<><>>)', {'<': '>'})
    assert check_delimiters('[<><<><>>)', {'<': '>'})
    assert not check_delimiters('(<)(>]', {'(': ')'})
    assert not check_delimiters('( [ [ ) ( ] ] )', {'(':')', '[':']'})


def test_weird_delims():
    assert check_delimiters('[>', {'[': '>'})
    assert check_delimiters('<[><!!', {'[': '>', '<': '!'})
    assert not check_delimiters('[]', {'[': '>'})
    assert not check_delimiters('()', {'(': '!'})


def test_quotes_simple():
    assert check_delimiters('""', {'"': '"'})
    assert check_delimiters('"hello" "world"', {'"': '"'})
    assert check_delimiters('("b", "m", "r", ("t"))', {'(': ')', '"': '"'})
    assert check_delimiters('( " " ) ( " " )', {'(':')', '"':'"'})
    assert check_delimiters('"\' \' \' \'" "\' \'"', {'"': '"', "'": "'"})
    assert not check_delimiters('"\'"\'', {'"': '"', "'": "'"})
    assert not check_delimiters('(")"', {'(': ')', '"': '"'})
    

def test_ifpf_basic():
    assert infix_to_postfix('1') == '1'
    assert infix_to_postfix('1 + 2') == '1 2 +'
    assert infix_to_postfix('( 1 + 2 )') == '1 2 +'
    assert infix_to_postfix('1 + 2 - 3') == '1 2 + 3 -'
    assert infix_to_postfix('1 + ( 2 - 3 )') == '1 2 3 - +'

def test_ifpf_prec():
    assert infix_to_postfix('1 + 2 * 3') == '1 2 3 * +'
    assert infix_to_postfix('1 / 2 + 3 * 4') == '1 2 / 3 4 * +'
    assert infix_to_postfix('1 * 2 * 3 + 4') == '1 2 * 3 * 4 +'
    assert infix_to_postfix('1 + 2 * 3 * 4') == '1 2 3 * 4 * +'

def test_ifpf_parens():
    assert infix_to_postfix('1 * ( 2 + 3 ) * 4') == '1 2 3 + * 4 *'
    assert (infix_to_postfix('1 * ( 2 + 3 * 4 ) + 5') 
            == '1 2 3 4 * + * 5 +')
    assert (infix_to_postfix('1 * ( ( 2 + 3 ) * 4 ) * ( 5 - 6 )') 
            == '1 2 3 + 4 * * 5 6 - *')
