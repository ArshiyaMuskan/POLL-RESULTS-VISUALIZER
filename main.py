from src.data_generator import generate_data
from src.data_loader import load_data
from src.data_cleaning import clean_data
from src.analysis import analyze_data
from src.visualization import plot_bar, plot_pie, plot_region
from src.insights import generate_insights

def main():
    # Step 1: Generate Data
    generate_data()

    # Step 2: Load Data
    df = load_data()

    # Step 3: Clean Data
    df = clean_data(df)

    # Step 4: Analyze
    summary = analyze_data(df)

    # Step 5: Visualize
    plot_bar(summary["counts"])
    plot_pie(summary["counts"])
    plot_region(df)

    # Step 6: Insights
    generate_insights(summary)

if __name__ == "__main__":
    main()