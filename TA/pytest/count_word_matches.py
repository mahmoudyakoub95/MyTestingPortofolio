def count_word_matches(text:str,target:str):
    counter=0
    if not text or not target:
        return 0
    words=text.lower().split()
    target=target.lower()
    for word in words:
        if target==word:
            counter+=1
    return counter
