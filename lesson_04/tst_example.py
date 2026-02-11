import pytest
from string_processor import StringProcessor

stringprocessor = StringProcessor()

@pytest.mark.parametrize("input_text, expected_output", [
    ("hello", "Hello."),       # Обычное слово -> заглавная и точка
    ("Hi", "Hi."),             # Уже с заглавной без точки 
    ("python is great", "Python is great."), # Предложение без точки
])
def test_process_positive(input_text, expected_output):
    stringprocessor = StringProcessor()
    assert stringprocessor.process(input_text) == expected_output

@pytest.mark.parametrize("input_text, expected_output", [
    ("", "."),                  # Пустая строка -> просто точка
    ("   ", "   ."), # Пустая строка с пробелами
])
def test_process_negative(input_text, expected_output):
    stringprocessor = StringProcessor()
    assert stringprocessor.process(input_text) == expected_output

# B
# .
# B .
# b
# not .

