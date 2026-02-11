def generate_prompt(db: str, query: str) -> str:
    return f"""
Analyze and optimize the following SQL query for a {db} database.
Goals:
- Identify performance anti-patterns
- Suggest query rewrites to improve index usage
- Recommend appropriate indexes
- Improve join strategies
- Reduce full table scans
- Improve sorting and filtering performance

Input:
================
{query}
================

Return your response in the following structured format:
1. Summary (2-3 sentences)
2. Detected Issues
   - Bullet list of specific problems
3. Optimized Version
   - Provide an optimized SQL equivalent
4. Index Recommendations
   - Provide CREATE INDEX statements where applicable
5. Expected Impact
   - Describe likely performance improvements
6. Risks / Tradeoffs
   - Any downsides of the recommendations
"""
