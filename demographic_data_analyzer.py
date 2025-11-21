import pandas as pd
import numpy as np

def calculate_demographic_data():
    # Read the data from file
    df = pd.read_csv('adult.data.csv')
    
    # How many people of each race are represented in this dataset?
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df['education'] == 'Bachelors').sum() / len(df) * 100, 1)

    # What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
    advanced_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    rich_advanced_edu = df[advanced_education & (df['salary'] == '>50K')]
    all_advanced_edu = df[advanced_education]
    
    higher_education_rich = round(len(rich_advanced_edu) / len(all_advanced_edu) * 100, 1)

    # What percentage of people without advanced education make more than 50K?
    no_advanced_education = ~advanced_education
    rich_no_advanced_edu = df[no_advanced_education & (df['salary'] == '>50K')]
    all_no_advanced_edu = df[no_advanced_education]
    
    lower_education_rich = round(len(rich_no_advanced_edu) / len(all_no_advanced_edu) * 100, 1)

    # What is the minimum number of hours a person works per week?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_min_workers = min_workers[min_workers['salary'] == '>50K']
    
    rich_percentage = round(len(rich_min_workers) / len(min_workers) * 100, 1) if len(min_workers) > 0 else 0

    # What country has the highest percentage of people that earn >50K and what is that percentage?
    country_stats = df.groupby('native-country')['salary'].apply(
        lambda x: (x == '>50K').sum() / len(x) * 100
    ).round(1)
    
    highest_earning_country = country_stats.idxmax()
    highest_earning_country_percentage = country_stats.max()

    # Identify the most popular occupation for those who earn >50K in India.
    india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_rich['occupation'].value_counts().idxmax()

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

# Test the function
if __name__ == '__main__':
    result = calculate_demographic_data()
    for key, value in result.items():
        print(f"{key}: {value}")