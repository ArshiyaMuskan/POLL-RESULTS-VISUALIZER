def generate_insights(summary):
    top_choice = summary["counts"].idxmax()
    print(f"🏆 Most Preferred Option: {top_choice}")