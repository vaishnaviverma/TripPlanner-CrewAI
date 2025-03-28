from langchain.tools import tool

class CalculatorTools():

    @tool("Make a calculation")
    def calculate(operation):
        """Useful tool to perform any mathematical calculation,
        like sum, minus, multiplication, division, etc. The input to this tool
        should be a mathematical expression, a couple of examples are '200*7'
        or '5000/2*7'
        """
        try:
            return eval(operation)
        except SyntaxError:
            return "Error: Invalid syntax in mathmeatical expression"

