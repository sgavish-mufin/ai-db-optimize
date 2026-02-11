import typer
from .prompt_gen import generate_prompt
from .llm_client import get_optimization_report

def analyze(
    db: str = typer.Option(..., help="Database type (postgres, mysql, etc)"),
    query: str = typer.Option(..., help="SQL query to analyze")
):
    """
    Analyze and optimize database queries using AI.
    """
    print(f"Analyzing SQL query for {db}...")
    
    prompt = generate_prompt(db, query)
    report = get_optimization_report(prompt)
    
    if report:
        print("\nOptimization Report:\n")
        print(report)
    else:
        print("\nFailed to generate report. Please check your API key and connection.")

if __name__ == "__main__":
    typer.run(analyze)
