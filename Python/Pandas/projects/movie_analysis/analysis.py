import pandas as pd
import matplotlib.pyplot as plt

# ==================================================
# LOAD DATASET
# ==================================================

df = pd.read_csv(
    r"C:\Users\MAINAK\Desktop\SQl\Pandas\projects\movie_analysis\data\movies.csv",
    engine="python",
    on_bad_lines="skip",
    encoding="latin1"
)

# ==================================================
# BASIC INFORMATION
# ==================================================

print("\n========== FIRST 5 ROWS ==========\n")
print(df.head())

print("\n========== DATASET SHAPE ==========\n")
print(df.shape)

print("\n========== COLUMN NAMES ==========\n")
print(df.columns)

print("\n========== DATA TYPES ==========\n")
print(df.dtypes)

print("\n========== MISSING VALUES ==========\n")
print(df.isnull().sum())

# ==================================================
# DATA CLEANING
# ==================================================

df = df.dropna()

df["Vote_Count"] = pd.to_numeric(
    df["Vote_Count"],
    errors="coerce"
)

df["Vote_Average"] = pd.to_numeric(
    df["Vote_Average"],
    errors="coerce"
)

df["Popularity"] = pd.to_numeric(
    df["Popularity"],
    errors="coerce"
)

df = df.dropna()

df["Release_Date"] = pd.to_datetime(
    df["Release_Date"],
    errors="coerce"
)

df = df.dropna()

df["Year"] = df["Release_Date"].dt.year

df["Decade"] = (df["Year"] // 10) * 10

# ==================================================
# SAVE CLEANED DATASET
# ==================================================

df.to_csv(
    r"C:\Users\MAINAK\Desktop\SQl\Pandas\projects\movie_analysis\data\cleaned_movies.csv",
    index=False
)

print("\n========== CLEANED DATA ==========\n")
print(df.head())

# ==================================================
# ANALYSIS SECTION
# ==================================================

movies_per_year = df.groupby("Year")["Title"].count()

top_popular_movies = df.sort_values(
    by="Popularity",
    ascending=False
).head(10)

highest_rated_movies = df.sort_values(
    by="Vote_Average",
    ascending=False
).head(10)

most_voted_movies = df.sort_values(
    by="Vote_Count",
    ascending=False
).head(10)

language_distribution = df[
    "Original_Language"
].value_counts().head(10)

genre_frequency = df[
    "Genre"
].value_counts().head(10)

avg_rating_by_language = df.groupby(
    "Original_Language"
)["Vote_Average"].mean().sort_values(
    ascending=False
).head(10)

high_rated_movies = df[
    df["Vote_Average"] > 8
]

movies_after_2020 = df[
    df["Year"] > 2020
]

genre_split = df[
    "Genre"
].str.split(",").explode()

genre_counts = genre_split.value_counts().head(10)

movies_count_language = df.groupby(
    "Original_Language"
)["Title"].count().sort_values(
    ascending=False
).head(10)

genre_popularity = df.groupby(
    "Genre"
)["Popularity"].mean().sort_values(
    ascending=False
).head(10)

movies_by_decade = df.groupby(
    "Decade"
)["Title"].count()

top_languages_rating = df.groupby(
    "Original_Language"
)["Vote_Average"].mean().sort_values(
    ascending=False
).head(10)

rolling_trend = movies_per_year.rolling(
    5
).mean()

year_rating = df.groupby(
    "Year"
)["Vote_Average"].mean()

year_popularity = df.groupby(
    "Year"
)["Popularity"].mean()

correlation = df[
    ["Popularity", "Vote_Average", "Vote_Count"]
].corr()

# ==================================================
# PRINT ANALYSIS
# ==================================================

print("\n========== MOVIES PER YEAR ==========\n")
print(movies_per_year)

print("\n========== TOP POPULAR MOVIES ==========\n")
print(top_popular_movies[["Title", "Popularity"]])

print("\n========== HIGHEST RATED MOVIES ==========\n")
print(highest_rated_movies[["Title", "Vote_Average"]])

print("\n========== MOST VOTED MOVIES ==========\n")
print(most_voted_movies[["Title", "Vote_Count"]])

print("\n========== LANGUAGE DISTRIBUTION ==========\n")
print(language_distribution)

print("\n========== GENRE FREQUENCY ==========\n")
print(genre_frequency)

print("\n========== AVG RATING BY LANGUAGE ==========\n")
print(avg_rating_by_language)

print("\n========== HIGH RATED MOVIES ==========\n")
print(high_rated_movies[["Title", "Vote_Average"]].head(10))

print("\n========== MOVIES AFTER 2020 ==========\n")
print(movies_after_2020[["Title", "Year"]].head(10))

print("\n========== MOST COMMON GENRES ==========\n")
print(genre_counts)

print("\n========== MOVIES COUNT BY LANGUAGE ==========\n")
print(movies_count_language)

print("\n========== GENRE POPULARITY ==========\n")
print(genre_popularity)

print("\n========== CORRELATION ==========\n")
print(correlation)

# ==================================================
# VISUALIZATION PATH
# ==================================================

visuals_path = r"C:\Users\MAINAK\Desktop\SQl\Pandas\projects\movie_analysis\visuals"

# ==================================================
# GRAPH 1
# MOVIES PER YEAR
# ==================================================

movies_per_year.plot(
    kind="line",
    figsize=(10,5)
)

plt.title("Movies Released Per Year")
plt.xlabel("Year")
plt.ylabel("Movies Count")

plt.tight_layout()

plt.savefig(
    visuals_path + r"\movies_per_year.png"
)

plt.show()

# ==================================================
# GRAPH 2
# TOP POPULAR MOVIES
# ==================================================

top_popular_movies.plot(
    x="Title",
    y="Popularity",
    kind="bar",
    figsize=(10,5)
)

plt.title("Top 10 Popular Movies")
plt.xlabel("Movie")
plt.ylabel("Popularity")

plt.tight_layout()

plt.savefig(
    visuals_path + r"\top_popular_movies.png"
)

plt.show()

# ==================================================
# GRAPH 3
# HIGHEST RATED MOVIES
# ==================================================

highest_rated_movies.plot(
    x="Title",
    y="Vote_Average",
    kind="bar",
    figsize=(10,5)
)

plt.title("Highest Rated Movies")
plt.xlabel("Movie")
plt.ylabel("Vote Average")

plt.tight_layout()

plt.savefig(
    visuals_path + r"\highest_rated_movies.png"
)

plt.show()

# ==================================================
# GRAPH 4
# MOST VOTED MOVIES
# ==================================================

most_voted_movies.plot(
    x="Title",
    y="Vote_Count",
    kind="bar",
    figsize=(10,5)
)

plt.title("Most Voted Movies")
plt.xlabel("Movie")
plt.ylabel("Vote Count")

plt.tight_layout()

plt.savefig(
    visuals_path + r"\most_voted_movies.png"
)

plt.show()

# ==================================================
# GRAPH 5
# LANGUAGE DISTRIBUTION
# ==================================================

language_distribution.plot(
    kind="pie",
    autopct="%1.1f%%",
    figsize=(8,8)
)

plt.title("Language Distribution")

plt.ylabel("")

plt.tight_layout()

plt.savefig(
    visuals_path + r"\language_distribution.png"
)

plt.show()

# ==================================================
# GRAPH 6
# GENRE FREQUENCY
# ==================================================

genre_frequency.plot(
    kind="bar",
    figsize=(10,5)
)

plt.title("Genre Frequency")
plt.xlabel("Genre")
plt.ylabel("Count")

plt.tight_layout()

plt.savefig(
    visuals_path + r"\genre_frequency.png"
)

plt.show()

# ==================================================
# GRAPH 7
# AVG RATING BY LANGUAGE
# ==================================================

avg_rating_by_language.plot(
    kind="bar",
    figsize=(10,5)
)

plt.title("Average Rating by Language")
plt.xlabel("Language")
plt.ylabel("Vote Average")

plt.tight_layout()

plt.savefig(
    visuals_path + r"\avg_rating_by_language.png"
)

plt.show()

# ==================================================
# GRAPH 8
# POPULARITY HISTOGRAM
# ==================================================

plt.figure(figsize=(10,5))

plt.hist(
    df["Popularity"],
    bins=20
)

plt.title("Popularity Distribution")
plt.xlabel("Popularity")
plt.ylabel("Frequency")

plt.tight_layout()

plt.savefig(
    visuals_path + r"\popularity_distribution.png"
)

plt.show()

# ==================================================
# GRAPH 9
# RATING HISTOGRAM
# ==================================================

plt.figure(figsize=(10,5))

plt.hist(
    df["Vote_Average"],
    bins=20
)

plt.title("Rating Distribution")
plt.xlabel("Vote Average")
plt.ylabel("Frequency")

plt.tight_layout()

plt.savefig(
    visuals_path + r"\rating_distribution.png"
)

plt.show()

# ==================================================
# GRAPH 10
# POPULARITY VS RATING
# ==================================================

plt.figure(figsize=(10,5))

plt.scatter(
    df["Popularity"],
    df["Vote_Average"]
)

plt.title("Popularity vs Rating")
plt.xlabel("Popularity")
plt.ylabel("Vote Average")

plt.tight_layout()

plt.savefig(
    visuals_path + r"\popularity_vs_rating.png"
)

plt.show()

# ==================================================
# GRAPH 11
# MOVIES COUNT BY LANGUAGE
# ==================================================

movies_count_language.plot(
    kind="bar",
    figsize=(10,5)
)

plt.title("Movies Count by Language")
plt.xlabel("Language")
plt.ylabel("Movies Count")

plt.tight_layout()

plt.savefig(
    visuals_path + r"\movies_count_language.png"
)

plt.show()

# ==================================================
# GRAPH 12
# GENRE POPULARITY
# ==================================================

genre_popularity.plot(
    kind="bar",
    figsize=(10,5)
)

plt.title("Genre Popularity")
plt.xlabel("Genre")
plt.ylabel("Popularity")

plt.tight_layout()

plt.savefig(
    visuals_path + r"\genre_popularity.png"
)

plt.show()

# ==================================================
# GRAPH 13
# TOP MOVIES AFTER 2020
# ==================================================

movies_after_2020.head(10).plot(
    x="Title",
    y="Popularity",
    kind="bar",
    figsize=(10,5)
)

plt.title("Top Movies After 2020")
plt.xlabel("Movie")
plt.ylabel("Popularity")

plt.tight_layout()

plt.savefig(
    visuals_path + r"\top_movies_after_2020.png"
)

plt.show()

# ==================================================
# GRAPH 14
# GENRE CONTRIBUTION
# ==================================================

genre_counts.head(5).plot(
    kind="pie",
    autopct="%1.1f%%",
    figsize=(8,8)
)

plt.title("Genre Contribution")

plt.ylabel("")

plt.tight_layout()

plt.savefig(
    visuals_path + r"\genre_contribution.png"
)

plt.show()

# ==================================================
# GRAPH 15
# RECENT YEAR TREND
# ==================================================

movies_per_year.tail(20).plot(
    kind="line",
    figsize=(10,5)
)

plt.title("Recent Year Movie Trend")
plt.xlabel("Year")
plt.ylabel("Movies Count")

plt.tight_layout()

plt.savefig(
    visuals_path + r"\recent_year_trend.png"
)

plt.show()

# ==================================================
# GRAPH 16
# CORRELATION MATRIX
# ==================================================

plt.figure(figsize=(8,5))

plt.imshow(correlation)

plt.colorbar()

plt.xticks(
    range(len(correlation.columns)),
    correlation.columns
)

plt.yticks(
    range(len(correlation.columns)),
    correlation.columns
)

plt.title("Correlation Matrix")

plt.tight_layout()

plt.savefig(
    visuals_path + r"\correlation_matrix.png"
)

plt.show()

# ==================================================
# GRAPH 17
# VOTE AVERAGE BOXPLOT
# ==================================================

plt.figure(figsize=(8,5))

plt.boxplot(df["Vote_Average"])

plt.title("Vote Average Boxplot")
plt.ylabel("Vote Average")

plt.tight_layout()

plt.savefig(
    visuals_path + r"\vote_average_boxplot.png"
)

plt.show()

# ==================================================
# GRAPH 18
# POPULARITY BOXPLOT
# ==================================================

plt.figure(figsize=(8,5))

plt.boxplot(df["Popularity"])

plt.title("Popularity Boxplot")
plt.ylabel("Popularity")

plt.tight_layout()

plt.savefig(
    visuals_path + r"\popularity_boxplot.png"
)

plt.show()

# ==================================================
# GRAPH 19
# MOVIES BY DECADE
# ==================================================

movies_by_decade.plot(
    kind="bar",
    figsize=(10,5)
)

plt.title("Movies by Decade")
plt.xlabel("Decade")
plt.ylabel("Movies Count")

plt.tight_layout()

plt.savefig(
    visuals_path + r"\movies_by_decade.png"
)

plt.show()

# ==================================================
# GRAPH 20
# TOP LANGUAGES BY RATING
# ==================================================

top_languages_rating.plot(
    kind="bar",
    figsize=(10,5)
)

plt.title("Top Languages by Average Rating")
plt.xlabel("Language")
plt.ylabel("Vote Average")

plt.tight_layout()

plt.savefig(
    visuals_path + r"\top_languages_rating.png"
)

plt.show()

# ==================================================
# GRAPH 21
# ROLLING TREND
# ==================================================

rolling_trend.plot(
    kind="line",
    figsize=(10,5)
)

plt.title("5-Year Rolling Movie Trend")
plt.xlabel("Year")
plt.ylabel("Movies Average")

plt.tight_layout()

plt.savefig(
    visuals_path + r"\rolling_movie_trend.png"
)

plt.show()

# ==================================================
# GRAPH 22
# TOP MOVIES BY VOTE COUNT
# ==================================================

most_voted_movies.head(10).plot(
    x="Title",
    y="Vote_Count",
    kind="line",
    figsize=(10,5),
    marker="o"
)

plt.title("Top Movies by Vote Count")
plt.xlabel("Movie")
plt.ylabel("Vote Count")

plt.tight_layout()

plt.savefig(
    visuals_path + r"\top_movies_vote_line.png"
)

plt.show()

# ==================================================
# GRAPH 23
# YEAR VS AVG RATING
# ==================================================

year_rating.plot(
    kind="line",
    figsize=(10,5)
)

plt.title("Year vs Average Rating")
plt.xlabel("Year")
plt.ylabel("Vote Average")

plt.tight_layout()

plt.savefig(
    visuals_path + r"\year_vs_avg_rating.png"
)

plt.show()

# ==================================================
# GRAPH 24
# TOP GENRES COUNT
# ==================================================

genre_counts.head(10).plot(
    kind="barh",
    figsize=(10,5)
)

plt.title("Top Genres Count")
plt.xlabel("Count")
plt.ylabel("Genre")

plt.tight_layout()

plt.savefig(
    visuals_path + r"\top_genres_count.png"
)

plt.show()

# ==================================================
# GRAPH 25
# YEARLY POPULARITY TREND
# ==================================================

year_popularity.plot(
    kind="line",
    figsize=(10,5)
)

plt.title("Yearly Popularity Trend")
plt.xlabel("Year")
plt.ylabel("Popularity")

plt.tight_layout()

plt.savefig(
    visuals_path + r"\yearly_popularity_trend.png"
)

plt.show()

# ==================================================
# FINAL MESSAGE
# ==================================================

print("\n========== PROJECT COMPLETED ==========")
print("All 25 graphs saved successfully.")
print("Dataset cleaned and analyzed successfully.")