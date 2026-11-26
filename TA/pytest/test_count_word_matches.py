import pytest
from count_word_matches import count_word_matches

@pytest.fixture(params=
    [
        ("The cat sat on the mat", "cat",1),
        ("Dog dog DOG dOg", "dog",4),
        ("Hello world", "world",1),
        ("hello hello HELLO", "hello",3),
        ("No matches here", "yes",0),
        ("catcat cat catdog", "cat",1),
        ("a a a", "a",3),


    ],
    ids=["TC01","TC02","TC03","TC04","TC05","TC06","TC07"]
)

#Test the normal cases
def normal_case(request):
    return request.param

def test_normal_cases(normal_case):
    text,target,expected=normal_case
    assert count_word_matches(text,target)==expected



@pytest.fixture(params=
    [

        ("", "word",0),
        ("hello world", "",0),
        ("", "",0),
        ("hello world    ", "world",1),
        (" cat ", "cat",1),
        ("cat,dog cat", "cat",1),
        ("x y z", "x",1),


    ],
    ids=["TC08","TC09","TC10","TC11","TC12","TC13","TC14"]
)

#Test the edge cases
def edge_case(request):
    return request.param

def test_edge_cases(edge_case):
    text,target,expected=edge_case
    assert count_word_matches(text,target)==expected



@pytest.fixture(params=
    [

        (None, "word",0),
        ("hello world", None,0),


    ],
    ids=["TC15","TC16"]
)

#Test the invalid input
def invalid_case(request):
    return request.param

def test_invalid_input_cases(invalid_case):
    text,target,expected=invalid_case
    assert count_word_matches(text,target)==expected




@pytest.fixture(params=
    [

        (123, "word"),
        ("hello world", 123),
        (["hello", "world"], "world"),
        ("hello world", ["world"]),

    ],
    ids=["TC17","TC18","TC19","TC20"]
)

#Test the exceptions cases
def exceptions_case(request):
    return request.param

def test_exceptions_cases(exceptions_case):
    text,target=exceptions_case
    with pytest.raises(AttributeError):
        assert count_word_matches(text,target)





