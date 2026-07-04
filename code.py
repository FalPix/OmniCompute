import re
import math
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import os

class Interpreter:
    def __init__(self):
        # Math functions mapping
        self.math_map = {
            "ceil": math.ceil, "floor": math.floor, "trunc": math.trunc, "fabs": math.fabs,
            "factorial": math.factorial, "gcd": math.gcd, "lcm": math.lcm, 
            "comb": math.comb, "perm": math.perm, "isqrt": math.isqrt,
            "sqrt": math.sqrt, "exp": math.exp, "log": math.log, "log10": math.log10, "log2": math.log2,
            "sin": math.sin, "cos": math.cos, "tan": math.tan, "asin": math.asin, 
            "acos": math.acos, "atan": math.atan, "degrees": math.degrees, "radians": math.radians
        }
        self.constants = {"pi": math.pi, "e": math.e, "tau": math.tau, "inf": math.inf, "g": 9.81}

    def show_help(self):
        print("""
        --- COMMANDS (Not Case-Sensitive) ---
        [UTILS]: Help, Save, Clear
        [PHYSICS]: Avg_speed, Velocity, Kinetic, Potential (e.g., Kinetic 10 5)
        [SHAPES]: Circle, Square, Triangle, Pentagon, Hexagon, Octagon, Line
        [BASIC MATH]: Add, Subtract, Multiply, Divide, Modulus, Prime
        [ADVANCED MATH]: Any python math function (e.g., Sqrt 16)
        [EQUATION]: Equation x**2 + y**2 - 25
        """)

    def draw_shape(self, sides, name):
        fig, ax = plt.subplots(figsize=(4, 4))
        ax.set_aspect('equal'); ax.grid(True); ax.set_xlim(-7, 7); ax.set_ylim(-7, 7); ax.set_title(name)
        angles = np.linspace(0, 2*np.pi, sides+1)
        ax.plot(5 * np.cos(angles), 5 * np.sin(angles))
        plt.show()

    def identify_and_plot(self, eq_str):
        x, y = sp.symbols('x y')
        try:
            expr = sp.sympify(eq_str)
            poly = sp.Poly(expr, x, y)
            coeffs = poly.as_dict()
            A, B, C = coeffs.get((2, 0), 0), coeffs.get((1, 1), 0), coeffs.get((0, 2), 0)
            shape = "Unknown Curve"
            if B == 0:
                if A == C and A != 0: shape = "Circle"
                elif A * C > 0: shape = "Ellipse"
                elif A * C < 0: shape = "Hyperbola"
                elif A == 0 or C == 0: shape = "Parabola"
            print(f"--- Detected: {shape} ---")
            x_vals = np.linspace(-10, 10, 400); y_vals = np.linspace(-10, 10, 400)
            X, Y = np.meshgrid(x_vals, y_vals); f = sp.lambdify((x, y), expr, 'numpy'); Z = f(X, Y)
            fig, ax = plt.subplots(figsize=(4, 4))
            ax.contour(X, Y, Z, [0], colors='green'); ax.grid(True); ax.set_title(f"{shape}: {eq_str}")
            plt.show()
        except Exception as e: print(f"Math Error: {e}")

    def run(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                cmd = line.lower().strip()
                if not cmd or cmd.startswith("#"): continue
                nums = [float(n) for n in re.findall(r"[-+]?\d*\.\d+|\d+", cmd)]
                
                # System Utilities
                if "help" in cmd: self.show_help()
                elif "save" in cmd: plt.savefig("output.png"); print("Saved to output.png")
                elif "clear" in cmd: os.system('cls' if os.name == 'nt' else 'clear')
                
                # Physics Tools
                elif "avg_speed" in cmd: print(f"Avg Speed: {nums[0]/nums[1]:.2f} m/s")
                elif "velocity" in cmd: print(f"Velocity: {nums[0]/nums[1]:.2f} m/s")
                elif "kinetic" in cmd: print(f"Kinetic Energy: {0.5 * nums[0] * nums[1]**2:.2f} J")
                elif "potential" in cmd: print(f"Potential Energy: {nums[0] * self.constants['g'] * nums[1]:.2f} J")
                
                # ... (Keep your existing math, equation, and shape elif statements here)
                elif "equation" in cmd: self.identify_and_plot(cmd.replace("equation", "").strip())
                elif "add" in cmd: print(f"Sum: {sum(nums)}")
                elif any(m in cmd for m in self.math_map):
                     for name, func in self.math_map.items():
                        if name in cmd:
                            try: print(f"{name.capitalize()}: {func(*[int(n) if name in ['gcd','lcm','comb','perm','factorial'] else n for n in nums])}")
                            except Exception as e: print(f"Math Error: {e}")
                elif "circle" in cmd: self.draw_shape(100, "Circle")
                elif "square" in cmd: self.draw_shape(4, "Square")
                elif "triangle" in cmd: self.draw_shape(3, "Triangle")

# Execution
interp = Interpreter()
while True:
    path = input("Enter .txt file name: ")
    try: interp.run(path)
    except Exception as e: print(f"Error: {e}")
    if input("Interpret another? (yes/no): ").lower() != 'yes': break