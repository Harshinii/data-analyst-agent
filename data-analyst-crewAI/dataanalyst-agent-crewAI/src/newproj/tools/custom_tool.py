from crewai_tools import tool

@tool("Python REPL Tool")
def python_repl_tool(code: str) -> str:
    """
    Executes Python code in a sandboxed environment using pre-imported data science libraries.
    To return a result, assign your output to a variable named 'result'.
    """
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    import statsmodels.api as sm
    from scipy import stats

    try:
        local_scope = {
            "pd": pd,
            "np": np,
            "plt": plt,
            "sns": sns,
            "sm": sm,
            "stats": stats,
        }
        exec(code, {}, local_scope)
        return str(local_scope.get("result", "Execution completed."))
    except Exception as e:
        return f"Error: {e}"