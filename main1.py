from demographic_data_analyzer import calculate_demographic_data

def main():
    result = calculate_demographic_data()
    
    print("=== Demographic Data Analysis Results ===")
    print(f"Race count:\n{result['race_count']}")
    print(f"\nAverage age of men: {result['average_age_men']}")
    print(f"Percentage with Bachelors degrees: {result['percentage_bachelors']}%")
    print(f"Percentage with higher education that earn >50K: {result['higher_education_rich']}%")
    print(f"Percentage without higher education that earn >50K: {result['lower_education_rich']}%")
    print(f"Min work time: {result['min_work_hours']} hours/week")
    print(f"Percentage of rich among those who work min hours: {result['rich_percentage']}%")
    print(f"Country with highest percentage of rich: {result['highest_earning_country']}")
    print(f"Highest percentage of rich people in country: {result['highest_earning_country_percentage']}%")
    print(f"Top occupations in India for those who earn >50K: {result['top_IN_occupation']}")

if __name__ == "__main__":
    main()