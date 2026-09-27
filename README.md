# AI Tools Lab

## Project Description

**AI Tools Lab** is a small Python project for practicing Git workflows and exploring AI-assisted code generation. It contains basic sorting algorithms and a utility module with simple string and temperature-conversion functions. The codebase is designed for hands-on practice with branching, merging, and submitting pull requests.

The project uses only the Python standard library; no external packages are required.

## Installation Instructions

Clone the repository and move into the project directory:

```bash
git clone https://github.com/<your-username>/ai_tools_lab.git
cd ai_tools_lab
```

Make sure Python 3 is installed. There is no `requirements.txt` to install.

## Usage Examples

### Sorting a list

`bubble_sort(arr)` sorts the supplied list in place and returns that list:

```python
from sorting import bubble_sort

values = [5, 2, 9, 1, 5, 6]
sorted_values = bubble_sort(values)
print(sorted_values)
# Output: [1, 2, 5, 5, 6, 9]
```

### Utility functions

```python
from utils import (
    celsius_to_fahrenheit,
    count_words,
    is_palindrome,
)

print(is_palindrome("radar"))
# Output: True

print(count_words("Python is clear and readable."))
# Output: 5

print(celsius_to_fahrenheit(25))
# Output: 77.0
```

## Contributors

- **Ranvir Singh**

## License

This project is licensed under the **MIT License**. You may use, copy, modify, merge, publish, distribute, sublicense, and sell copies of the software, provided the copyright and permission notices are included. The software is provided **“as is”**, without warranty of any kind.
