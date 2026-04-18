def analyze_data(df):
    vote_counts = df["Option_Selected"].value_counts()
    vote_percent = (vote_counts / len(df)) * 100

    summary = {
        "counts": vote_counts,
        "percent": vote_percent
    }

    return summary