# IPL Match Analyzer (Pandas)

# ```python
import pandas as pd
import matplotlib.pyplot as plt

# LOAD DATA

file_path = r'C:\Users\MAINAK\Desktop\SQl\Projects\ipl-matches.csv'
matches = pd.read_csv(file_path)


# FUNCTIONS WITH GRAPHS


def most_successful_team():
    data = matches['WinningTeam'].value_counts().head(10)
    print(data)
    data.plot(kind='bar')
    plt.title('Top Winning Teams')
    plt.show()


def top_players():
    data = matches['Player_of_Match'].value_counts().head(10)
    print(data)
    data.plot(kind='bar')
    plt.title('Top Players')
    plt.show()


def toss_analysis():
    data = matches['TossWinner'].value_counts().head(10)
    print(data)
    data.plot(kind='bar')
    plt.title('Toss Winners')
    plt.show()


def win_percentage():
    total_matches = pd.concat([matches['Team1'], matches['Team2']]).value_counts()
    total_wins = matches['WinningTeam'].value_counts()
    win_percent = (total_wins / total_matches * 100).dropna().sort_values(ascending=False).head(10)

    print(win_percent)
    win_percent.plot(kind='bar')
    plt.title('Win Percentage')
    plt.show()


def season_champion():
    champions = matches.groupby('Season')['WinningTeam'].agg(lambda x: x.value_counts().idxmax())
    print(champions)

    champions.value_counts().plot(kind='bar')
    plt.title('Most Season Wins by Teams')
    plt.show()


def venue_analysis():
    venue = matches['Venue'].value_counts().head(10)
    print(venue)
    venue.plot(kind='bar')
    plt.title('Top Venues')
    plt.show()


def team_vs_team():
    t1 = input("Enter Team 1: ")
    t2 = input("Enter Team 2: ")

    temp = matches[
        ((matches['Team1'] == t1) & (matches['Team2'] == t2)) |
        ((matches['Team1'] == t2) & (matches['Team2'] == t1))
    ]

    print(temp['WinningTeam'].value_counts())
    temp['WinningTeam'].value_counts().plot(kind='bar')
    plt.title(f'{t1} vs {t2}')
    plt.show()


def win_type():
    data = matches['WonBy'].value_counts()
    print(data)
    data.plot(kind='pie', autopct='%1.1f%%')
    plt.title('Win Type')
    plt.show()



# MENU SYSTEM

while True:
    print("\n===== IPL ANALYZER (GRAPH VERSION) =====")
    print("1. Most Successful Team")
    print("2. Top Players")
    print("3. Toss Analysis")
    print("4. Win Percentage")
    print("5. Season Champions")
    print("6. Venue Analysis")
    print("7. Team vs Team")
    print("8. Win Type")
    print("9. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        most_successful_team()

    elif choice == 2:
        top_players()

    elif choice == 3:
        toss_analysis()

    elif choice == 4:
        win_percentage()

    elif choice == 5:
        season_champion()

    elif choice == 6:
        venue_analysis()

    elif choice == 7:
        team_vs_team()

    elif choice == 8:
        win_type()

    elif choice == 9:
        print("Exiting...")
        break

    else:
        print("Invalid choice")

