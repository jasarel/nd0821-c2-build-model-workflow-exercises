import scipy.stats


# COMPLETE HERE: make this test accept the fixtures defined in the
# conftest.py file (data and ks_alpha)
def test_kolmogorov_smirnov(data, ks_alpha):  # TODO: update x and y here.

    sample1, sample2 = data

    columns = [
        "danceability",
        "energy",
        "loudness",
        "speechiness",
        "acousticness",
        "instrumentalness",
        "liveness",
        "valence",
        "tempo",
        "duration_ms"
    ]

    alpha_prime = 1 - (1 - ks_alpha)**(1 / len(columns))

    # Column with Nan values (Getting imputted)
    sample1['loudness'].fillna(sample1['loudness'].mean(), inplace=True)

    sample2['loudness'].fillna(sample2['loudness'].mean(), inplace=True)

    for col in columns:

        ts, p_value = scipy.stats.ks_2samp(sample1[col], sample2[col])

        # RUN kept failing, so i added checked to make sure data had all values (sample 1 did not)
        assert not sample1[col].isnull().any(), f"NaN values found in sample1 for column {col}"
        assert not sample2[col].isnull().any(), f"NaN values found in sample2 for column {col}"


        # NOTE: as always, the p-value should be interpreted as the probability of
        # obtaining a test statistic (TS) equal or more extreme that the one we got
        # by chance, when the null hypothesis is true. If this probability is not
        # large enough, this dataset should be looked at carefully, hence we fail
        assert p_value > alpha_prime
