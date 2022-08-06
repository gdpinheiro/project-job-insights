from src.counter import count_ocurrences

path = "src/jobs.csv"

word_javascript = "javascript"
word_typescript = "typescript"


def test_counter():
    try:
        count = count_ocurrences(path, word_javascript)
        print(count)
        assert count == 122
    except ValueError:
        assert False
