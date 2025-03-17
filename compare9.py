from mcp.server.fastmcp import FastMCP
mcp = FastMCP("Compare9")

@mcp.tool()
def compare(number1: float, number2: float) -> str:
    """
    Compare two numbers and return True if the first number is larger than the second.
    Args:
        number1 (float): The first number to compare.
        number2 (float): The second number to compare.
    Returns:
        str: A string indicating which number is larger or if they are equal.
    """
    if number1 > number2:
        return f"{number1} is larger"
    elif number1 < number2:
        return f"{number2} is larger"
    else:
        return f"{number1} and {number2} are equal"

if __name__ == "__main__":
    mcp.run(transport="stdio")