#!/usr/local/bin/python3

# This work is licensed by Zachary J. Szewczyk under the Creative Commons
# Attribution-NonCommercial-ShareAlike 4.0 International License. See
# http://creativecommons.org/licenses/by-nc-sa/4.0/ for more information.

# Method: title_unit_test
# Purpose: Compare the extracted title from the given URL to a string.
# Parameters:
# - url: URL from which to retrieve the page title.
# - title: Title against which to compare the retrieved title.
# Return: 1 (Success), 0 (Failure) (Int)
def title_unit_test(url,title):
    w = Web()
    w.get(url)

    print(f" - {url}", end="", flush=True)
    if (w.get_title() == title):
        print(" + Passed")
        return 1
    print(" - Failed")
    return 0

# If run as a standlone program, run the tests.
if (__name__ == "__main__"):
    total_tests = 0
    passed_tests = 0

    total_tests += 1
    passed_tests += title_unit_test("https://peppe.rs/posts/font_size_fallacies/", "Font Size Fallacies · peppe.rs")

    total_tests += 1
    passed_tests += title_unit_test("https://www.axios.com/dhs-cybersecurity-agency-stress-test-remote-capabilities-coronavirus-cisa-00d94cb9-8826-4271-8cb4-9b380c26a282.html", "DHS' cybersecurity agency to test remote capabilities amid coronavirus - Axios")

    total_tests += 1
    passed_tests += title_unit_test("https://seekingalpha.com/article/4327758-time-to-shield-your-portfolio-message-from-seeking-alphas-founder?source=banner_media_custom&ad_inventory=native&ad_position=single_link", "It's Time To Shield Your Portfolio: A Message From Seeking Alpha's Founder | Seeking Alpha")

    total_tests += 1
    passed_tests += title_unit_test("https://medium.com/@emilefugulin/http-desync-attacks-with-python-and-aws-1ba07d2c860f", "HTTP Desync Attacks with Python and AWS - Emile Fugulin - Medium")

    total_tests += 1
    passed_tests += title_unit_test("https://blog.balthazar-rouberol.com/", "Balthazar")

    total_tests += 1
    passed_tests += title_unit_test("https://lobste.rs/s/bxvg76/home_network_recommendations", "Home network recommendations? | Lobsters")

    total_tests += 1
    passed_tests += title_unit_test("https://www.theguardian.com/fashion/2020/mar/12/i-wear-my-grandads-old-boxers-meet-the-people-who-havent-bought-clothes-for-a-decade", "'I wear my grandad’s old boxers': meet the people who haven't bought clothes for a decade | Fashion | The Guardian")

    total_tests += 1
    passed_tests += title_unit_test("https://github.com/Lissy93/personal-security-checklist/blob/master/README.md", "personal-security-checklist/README.md at master · Lissy93/personal-security-checklist · GitHub")

    total_tests += 1
    passed_tests += title_unit_test("https://cyberdefensereview.army.mil/Portals/6/Nonsimplicity_The_Warriors_Way_West_Arney.pdf?ver=2020-01-17-094932-937", "https://cyberdefensereview.army.mil/Portals/6/Nonsimplicity_The_Warriors_Way_West_Arney.pdf?ver=2020-01-17-094932-937")

    total_tests += 1
    passed_tests += title_unit_test("https://malisper.me/how-to-improve-your-productivity-as-a-working-programmer/", "How to Improve Your Productivity as a Working Programmer - malisper.me")

    total_tests += 1
    passed_tests += title_unit_test("https://www.youtube.com/watch?v=mUpFRDR2Jto", "The MUSEROAMER Project (Part 6) The Ultimate DIY Overlanding Expedition Vehicle!")

    total_tests += 1
    passed_tests += title_unit_test("https://www.youtube.com/watch?v=0Rnyvtan8YQ", "Overland Vehicle Awnings: Expedition Overland 'Proven' Gear & Tactics #9")

    total_tests += 1
    passed_tests += title_unit_test("https://youtu.be/ID1KudXxLfU", "Adventure Hike of Arizona's Devils Chasm: A Hidden Gem in the Desert")

    total_tests += 1
    passed_tests += title_unit_test("https://mobile.twitter.com/jcs/status/1224205573656322048", "https://mobile.twitter.com/jcs/status/1224205573656322048")

    total_tests += 1
    passed_tests += title_unit_test("https://blog.talosintelligence.com/2020/01/mideast-tensions-preparations.html", "Talos Blog || Cisco Talos Intelligence Group - Comprehensive Threat Intelligence: What the continued escalation of tensions in the Middle East means for security")

    total_tests += 1
    passed_tests += title_unit_test("https://utcc.utoronto.ca/~cks/space/blog/web/UBlockOriginAndUMatrix", "Chris's Wiki :: blog/web/UBlockOriginAndUMatrix")

    total_tests += 1
    passed_tests += title_unit_test("https://www.thirtythreeforty.net/posts/2019/08/mastering-embedded-linux-part-1-concepts/", "Mastering Embedded Linux, Part 1: Concepts • &> /dev/null")

    total_tests += 1
    passed_tests += title_unit_test("https://www.thenewatlantis.com/publications/all-activities-monitored", "All Activities Monitored - The New Atlantis")

    total_tests += 1
    passed_tests += title_unit_test("https://gen.medium.com/undercover-in-the-orthodox-underworld-83c61ba3aa83", "Undercover in the Orthodox Underworld - GEN")

    total_tests += 1
    passed_tests += title_unit_test("https://efficiencyiseverything.com/eat-for-1-50-per-day-layoffs-coronavirus-quarantine-food-shortages/", "» Eat for $1.50 per day – Layoffs, Coronavirus Quarantine, Food Shortages")

    print(f"{passed_tests}/{total_tests} passed.")