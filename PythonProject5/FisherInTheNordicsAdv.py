# Ex 8: Fisher in the Nordics Adv
# Kevin Key
# 10/16/2025

countries = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
male_fishers = [1822, 2575, 3400, 11291, 1731]
female_fishers = [69, 77, 400, 320, 26]

def guess(gender_of_winner):
    """
    Guesses the nationality of a fisher based on their gender.

    Args:
        gender_of_winner (str): The gender of the fisher ('male' or 'female').

    Returns:
        tuple: A pair containing the country (str) and the probability (float).
    """
    # Select the appropriate list of fisher counts based on the gender
    if gender_of_winner == 'male':
        fishers_list = male_fishers
    else: # Assumes 'female'
        fishers_list = female_fishers

    # Calculate the total number of fishers for the given gender
    total_fishers_by_gender = sum(fishers_list)
    # Find the highest number of fishers in the list
    max_fishers = max(fishers_list)
    # Find the index of that highest number
    max_index = fishers_list.index(max_fishers)

    # Use the index to get the corresponding country
    most_likely_country = countries[max_index]

    # Calculate the probability of that country being the winner's nationality
    # P(Country | Gender) = (Fishers in Country) / (Total Fishers of that Gender)
    probability = (max_fishers / total_fishers_by_gender) * 100

    return (most_likely_country, probability)

def main():
    """
    Main function to run the logic and print the formatted output.
    """
    # Get the guess for a male winner
    country_male, prob_male = guess('male')
    # Print the result using an f-string for precise formatting
    # The format specifier {prob_male:05.2f} ensures two decimal places
    # and a leading zero if the number is less than 10.
    print(f"if the winner is male, my guess is he's from {country_male}; probability {prob_male:05.2f}%")

    # Get the guess for a female winner
    country_female, prob_female = guess('female')
    # Print the result with the same precise formatting
    print(f"if the winner is female, my guess is she's from {country_female}; probability {prob_female:05.2f}%")

# This ensures the main function is called when the script is run
if __name__ == "__main__":
    main()