from functions.get_file_content import get_file_content

print("Result for main.py:")
print(get_file_content("calculator", "main.py"))

print("Result for 'pkg' :")
print(get_file_content("calculator", "pkg/calculator.py"))

print("Result for '/bin' :")
print(get_file_content("calculator", "/bin/cat"))

print("Result for '../' :")
print(get_file_content("calculator", "pkg/does_not_exist.py"))