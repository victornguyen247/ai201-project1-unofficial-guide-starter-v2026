import scorer

def test_scorer():
    question = "What is the capital of France?"
    expects = "Paris"
    answer = "Paris"
    results = []
    assert scorer.judge(question, expects, answer, results) == True

def main():
    test_scorer()

if __name__ == "__main__":
    main()