import pandas as pd


def merge():
    imdb_cleaned = pd.read_csv("../data/processed/IMDB_top_1000_clean.csv")
    agg_emo = pd.read_csv(
        "../data/processed/reviews_data_with_aggregate_emotion_scores.csv"
    )
    plots = pd.read_csv("../data/processed/with_plot_summary.csv")

    merged_df = imdb_cleaned.merge(agg_emo, on="mc_link", how="inner").merge(
        plots, on="mc_link", how="inner"
    )[
        [
            "title_x",
            "genre",
            "metascore",
            "rating",
            "aggregate_score",
            "produce_year",
            "introduction",
            "plot",
        ]
    ]
    return merged_df


if __name__ == "__main__":
    path = "../data/outputs/finaldf.csv"
    merge().to_csv(path, index=False)
    print(f":: All done. Saved in {path} ::")
