# AI Tools Lab

## Project Description

**AI Tools Lab** is a small Python project created to demonstrate practical Git workflows and AI-assisted code generation. The repository includes:

- A basic `bubble_sort` implementation for sorting lists.
- A utility module with functions for palindrome checks, word counting, and Celsius-to-Fahrenheit conversion.
- A simple codebase suitable for practicing branching, merging, pull requests, and collaborative development.

The project uses only the Python standard library and does not require external packages.

## Installation Instructions

Clone the repository using Git:

```bash
git clone https://github.com/<your-username>/ai-tools-lab.git
cd ai-tools-lab
```

Ensure that **Python 3** is installed, then run the modules or use their functions from another Python script. No `requirements.txt` installation is needed.

## Usage Examples

### Sorting a list

Import `bubble_sort` from `sorting.py`. The function sorts the list in place and returns the sorted list.

```python
from sorting import bubble_sort

numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = bubble_sort(numbers)

print(sorted_numbers)
# Output: [11, 12, 22, 25, 34, 64, 90]
```

### Using utility functions

Import the utility functions from `utils.py`:

```python
from utils import (
    celsius_to_fahrenheit,
    count_words,
    is_palindrome,
)

print(is_palindrome("radar"))
# Output: True

print(count_words("Python makes automation approachable."))
# Output: 4

print(celsius_to_fahrenheit(25))
# Output: 77.0
```

## Contributors

- **Ranvir Singh**

Contributions, suggestions, and improvements are welcome through Git branches and pull requests.

## License

This project is licensed under the **MIT License**.

The MIT License permits use, copying, modification, merging, publishing, distribution, sublicensing, and selling copies of the software, provided that the copyright notice and permission notice are included in all substantial portions of the software. The software is provided **“as is”**, without warranty of any kind.
