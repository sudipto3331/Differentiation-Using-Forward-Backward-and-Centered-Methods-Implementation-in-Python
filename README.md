# Differentiation Using Forward, Backward, and Centered Methods Implementation in Python

This repository contains a Python implementation of numerical differentiation using Forward, Backward, and Centered methods with nth order derivatives. The code allows users to select the differentiation point, step size, method of differentiation, and the accuracy of the result.

### Table of Contents
- [Numerical Differentiation Theory](#numerical-differentiation-theory)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [Example](#example)
- [Files in the Repository](#files-in-the-repository)
- [Input Parameters](#input-parameters)
- [Troubleshooting](#troubleshooting)
- [Author](#author)

### Numerical Differentiation Theory
Numerical differentiation is a method of estimating the derivative of a function using finite differences. The methods implemented in this code include:

1. **Forward Difference Method**: Approximates the derivative of a function at a point using values at that point and a point a small distance forward.

   - **First Order**: 
     \[
     f'(x) \approx \frac{f(x + h) - f(x)}{h}
     \]

   - **Second Order**: 
     \[
     f'(x) \approx \frac{-f(x + 2h) + 4f(x + h) - 3f(x)}{2h}
     \]

2. **Backward Difference Method**: Approximates the derivative using values at the point and a point a small distance backward.

   - **First Order**: 
     \[
     f'(x) \approx \frac{f(x) - f(x - h)}{h}
     \]

   - **Second Order**: 
     \[
     f'(x) \approx \frac{f(x - 2h) - 4f(x - h) + 3f(x)}{2h}
     \]

3. **Centered Difference Method**: Uses points on both sides of the target point to approximate the derivative.

   - **First Order**: 
     \[
     f'(x) \approx \frac{f(x + h) - f(x - h)}{2h}
     \]

   - **Second Order**: 
     \[
     f'(x) \approx \frac{-f(x + 2h) + 8f(x + h) - 8f(x - h) + f(x - 2h)}{12h}
     \]

### Dependencies
This implementation does not require any external libraries; it uses standard Python functions.

### Installation
No additional installation is required. Ensure you have Python installed on your system.

### Usage
1. Clone the repository.
2. Run the script using Python:
    ```sh
    python differentiation_methods.py
    ```
3. Input the required parameters when prompted:
    - Enter the order of the derivative.
    - Enter the point at which to differentiate.
    - Enter the step size.
    - Choose the method (1 for Forward, 2 for Backward, 3 for Centered).
    - Choose the accuracy (1 for O(h), 2 for O(h²)).

### Code Explanation
The code defines the function for differentiation and implements methods for forward, backward, and centered differentiation, both for first and second-order derivatives. The main program allows users to choose the desired settings.

Below is a snippet from the code illustrating the main logic:

```python
def fnc(x):
    return x**2

def forward_oh(x, h, n):
    if n <= 0:
        return 0
    elif n == 1:
        result = (fnc(x + h) - fnc(x)) / h
        return result
    else:
        result = (forward_oh(x + h, h, n - 1) - forward_oh(x, h, n - 1)) / h
        return result

def forward_oh2(x, h):
    result = (-fnc(x + h + h) + (4 * fnc(x + h)) - (3 * fnc(x))) / (2 * h)
    return result

def backward_oh(x, h):
    result = (fnc(x) - fnc(x - h)) / h
    return result

def backward_oh2(x, h):
    result = (fnc(x - h - h) - (4 * fnc(x - h)) + (3 * fnc(x))) / (2 * h)
    return result

def center_oh(x, h):
    result = (fnc(x + h) - fnc(x - h)) / (2 * h)
    return result

def center_oh2(x, h):
    result = (-fnc(x + h + h) + (8 * fnc(x + h)) - (8 * fnc(x - h)) + fnc(x - h - h)) / (12 * h)
    return result

order = float(input("Enter the derivative order: "))
point = float(input("Enter the differentiating point: "))
h = float(input("Enter the step size: "))
method = float(input("Select Method:\n1. Forward\n2. Backward\n3. Centered\nEnter Choice: "))
accuracy = float(input("Select Accuracy:\n1. O(h)\n2. O(h^2)\nEnter Choice: "))

if method == 1:
    if accuracy == 1:
        result = forward_oh(point, h, order)
        if result <= 0:
            print("Differentiation not possible")
        else:
            print("Result:", result)
    elif accuracy == 2:
        print("Result:", forward_oh2(point, h))
elif method == 2:
    if accuracy == 1:
        print("Result:", backward_oh(point, h))
    elif accuracy == 2:
        print("Result:", backward_oh2(point, h))
elif method == 3:
    if accuracy == 1:
        print("Result:", center_oh(point, h))
    elif accuracy == 2:
        print("Result:", center_oh2(point, h))
```

### Example
Below is an example of how to use the script:

1. **Run the script**:
    ```sh
    python differentiation_methods.py
    ```

2. **Enter the input values**:
    ```
    Enter the derivative order: 1
    Enter the differentiating point: 3
    Enter the step size: 0.01
    Select Method:
    1. Forward
    2. Backward
    3. Centered
    Enter Choice: 3
    Select Accuracy:
    1. O(h)
    2. O(h^2)
    Enter Choice: 2
    ```

3. **Output**:
    - The script will calculate the derivative using the chosen method and print the result:
    ```
    Result: 6.000000000000082
    ```

### Files in the Repository
- `differentiation_methods.py`: The main script for performing numerical differentiation using different methods.

### Input Parameters
The script prompts for the following input values:
- Order of the derivative (`order`).
- Point at which to differentiate (`point`).
- Step size (`h`).
- Method of differentiation (1 for Forward, 2 for Backward, 3 for Centered).
- Desired accuracy (1 for O(h), 2 for O(h²)).

### Troubleshooting
1. **Input Values**: Ensure that the derivative order and input values are valid.
2. **Function Definition**: The function \( f(x) = x^2 \) is hardcoded. Modify this function as necessary for different differentiands.
3. **Python Version**: This script is compatible with Python 3. Ensure you have Python 3 installed.

## Author
Script created by sudipto3331.

---

This documentation should guide you through understanding, installing, and using the differentiation methods script. For further issues or feature requests, please open an issue in the repository. Feel free to contribute by creating issues and submitting pull requests. Happy coding!
