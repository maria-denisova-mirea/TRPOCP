import sys
from io import StringIO

def test_program():
    input_data = "10\n2\n"
    expected_output = "12444\n8\n20\n5.0\nНужно ли ещё что-нибудь для Вас посчитать?\n"

    sys.stdin = StringIO(input_data)
    sys.stdout = StringIO()
    
    a, b = int(input()), int(input())
    print(a + b, a - b, a*b, a/b, 'Нужно ли ещё что-нибудь для Вас посчитать?', sep='\n')

    output = sys.stdout.getvalue()
    assert output == expected_output

    sys.stdin = sys.__stdin__
    sys.stdout = sys.__stdout__

test_program()
print("Тест пройден")
