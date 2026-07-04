# 🖥️ OmniCompute 

OmniCompute is a file-based script interpreter written in Python that parses custom text files to execute mathematical computations, evaluate physics formulas, render regular geometric shapes, and dynamically analyze and plot symbolic algebraic equations.

## ✨ Features

*   **File-Based Interpreter:** Read and execute instructions sequentially from any standard `.txt` file.
*   **Physics Calculators:** Quick evaluation of Average Speed, Velocity, Kinetic Energy, and Potential Energy.
*   **Geometric Shape Rendering:** Instantly plot shapes like Triangles, Squares, and Circles via `matplotlib`.
*   **Advanced Equation Analyzer:** Utilizes `sympy` to identify algebraic expressions (e.g., Circle, Ellipse, Hyperbola, Parabola) and render their contour graphs.
*   **Python Math Mapping:** Native access to advanced Python math functions (`sqrt`, `log`, `factorial`, trigonometric operations, etc.).

## 🚀 Getting Started

### Prerequisites

Ensure you have Python 3.x installed along with the required third-party libraries:

```bash
pip install numpy matplotlib sympy
```

### Running the Project

1. Clone or download this repository.
2. Run the main interpreter script:
   ```bash
   python code.py
   ```

## 📝 Syntax & Command Guide

Commands are **not case-sensitive**. Lines starting with `#` are treated as comments and ignored.

### 1. Basic & Advanced Math
*   `Add 10 20 30` $\rightarrow$ Outputs the sum of the numbers.
*   `Subtract 50 10 5` $\rightarrow$ Computes sequential subtraction ($50 - 10 - 5$).
*   `Multiply 5 4 2` $\rightarrow$ Outputs the total product.
*   `Divide 10 2` $\rightarrow$ Outputs the quotient.
*   `Modulus 10 3` $\rightarrow$ Outputs the remainder ($10 \pmod 3$).
*   `Prime 7` $\rightarrow$ Evaluates whether the number is a prime number.
*   `Sqrt 16` $\rightarrow$ Dynamically triggers standard mapped Python math functions (e.g., `sin`, `log`, `factorial`).

### 2. Physics Equations
*   `Avg_speed [distance] [time]` $\rightarrow$ Calculates average speed in m/s.
*   `Velocity [displacement] [time]` $\rightarrow$ Calculates velocity in m/s.
*   `Kinetic [mass] [velocity]` $\rightarrow$ e.g., `Kinetic 10 5` (Outputs Kinetic Energy in Joules).
*   `Potential [mass] [height]` $\rightarrow$ Calculates Potential Energy using $g = 9.81\text{ m/s}^2$.

### 3. Shape Generation
*   `Triangle`, `Square`, `Pentagon`, `Hexagon`, `Octagon`, or `Circle` $\rightarrow$ Renders an equilateral representation of the chosen shape using `matplotlib`.
*   `Line [x1] [y1] [x2] [y2]` $\rightarrow$ Plots a distinct 2D vector segment between two specific coordinate points.

### 4. Equation Plotting
*   `Equation [expression]` $\rightarrow$ e.g., `Equation x**2 + y**2 - 25` (Identifies the geometric curve type and renders its dynamic contour plot).

### 5. System Utilities
*   `Help` $\rightarrow$ Prints the quick commands list to the terminal interface.
*   `Save` $\rightarrow$ Saves the active plot window frame directly to `output.png`.
*   `Clear` $\rightarrow$ Clears the active terminal output history screen.
