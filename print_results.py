def print_results(results_dic, results_stats_dic, model,
                  print_incorrect_dogs=False, print_incorrect_breed=False):
    """
    Prints summary results on the classification and then prints incorrectly
    classified dogs and incorrectly classified dog breeds if the user indicates
    they want those printouts (use non-default values)
    Parameters:
      # ... (unchanged)

    Returns:
        None - simply printing results.
    """
    print(f"\nModel used: {model.upper()}")

    print(f"\nNumber of images: {results_stats_dic['n_images']}")
    print(f"Number of dog images: {results_stats_dic['n_dogs_img']}")
    print(f"Number of non-dog images: {results_stats_dic['n_notdogs_img']}")

    print(f"\nPercentage match: {results_stats_dic['pct_match']:.1f}%")

    print(f"Percentage correctly classified dogs: {results_stats_dic['pct_correct_dogs']:.1f}%")

    print(f"Percentage correctly classified dog breeds: {results_stats_dic['pct_correct_breed']:.1f}%")

    print(f"Percentage correctly classified non-dogs: {results_stats_dic['pct_correct_notdogs']:.1f}%")

    if print_incorrect_dogs and (results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs'] != results_stats_dic['n_images']):
        print("\nIncorrectly classified dogs:")
        for key in results_dic:
            if sum(results_dic[key][3:]) == 1:
                print(f"Real: {results_dic[key][0]}, Classified: {results_dic[key][1]}")

    if print_incorrect_breed and (results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed']):
        print("\nIncorrectly classified dog breeds:")
        for key in results_dic:
            if sum(results_dic[key][3:]) == 2 and results_dic[key][2] == 0:
                print(f"Real: {results_dic[key][0]}, Classified: {results_dic[key][1]}")
