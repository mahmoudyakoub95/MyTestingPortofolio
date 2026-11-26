import pytest
from count_word_matches import count_word_matches

@pytest.mark.parametrize(
    "text, target,expected,error",
    [
        ("The cat sat on the mat", "cat",1,None),
        ("Dog dog DOG dOg", "dog",4,None),
        ("Hello world", "world",1,None),
        ("hello hello HELLO", "hello",3,None),
        ("No matches here", "yes",0,None),
        ("catcat cat catdog", "cat",1,None),
        ("a a a", "a",3,None),
        ("", "word",0,None),
        ("hello world", "",0,None),
        ("", "",0,None),
        ("hello world    ", "world",1,None),
        (" cat ", "cat",1,None),
        ("cat,dog cat", "cat",1,None),
        ("x y z", "x",1,None),
        (None, "word",0,None),
        ("hello world", None,0,None),
        (123, "word",None,AttributeError),
        ("hello world", 123,None,AttributeError),
        (["hello", "world"], "world",None,AttributeError),
        ("hello world", ["world"],None,AttributeError),
        ("x y z", "x",1,None),

    ],
    ids=["TC01","TC02","TC03","TC04","TC05","TC06","TC07","TC08","TC09","TC10",
         "TC11","TC12","TC13","TC14","TC15","TC16","TC17","TC18","TC19","TC20","TC21",]
)

#write the parameterized function

def test_count_word_matches(text,target,expected,error):
    if error:
        with pytest.raises(error):
            count_word_matches(text,target)
    else:
            assert count_word_matches(text,target)==expected
