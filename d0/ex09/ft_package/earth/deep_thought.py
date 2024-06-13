def deep_thought(question: str):
    question = question.lower()
    test = question.find("what is the answer") != -1 \
        and question.find("life") != -1 \
        and question.find("universe") != -1 \
        and question.find("everything") != -1
    if test is True:
        return 42
    else:
        return "I don't know the answer to that question."
