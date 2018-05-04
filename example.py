from faktiskt import FaktisktScraper
from faktiskt import FaktisktStatistics

investigation_search = FaktisktScraper.InvestigationSearch()

investigation_data = []
for url in investigation_search.fetch_investigation_url():
    investigation = FaktisktScraper.Investigation(url)
    print("- Claim at: {}".format(investigation.claim_url))
    print("- Claim checked by: {}".format(investigation.claim_checker))
    print("- Claim made by: {}".format(investigation.claim_maker))
    print("- Claim: {}".format(investigation.claim))
    print("- Claim checked date: {}".format(investigation.check_date))
    print("- Claim tagged as: {}".format(investigation.claim_tags))
    print("- Claim concluded as: {}".format(investigation.check_conclusion))

    investigation_data.append({
        'claim_url': investigation.claim_url,
        'claim_checker': investigation.claim_checker,
        'claim_maker': investigation.claim_maker,
        'claim': investigation.claim,
        'check_date': investigation.check_date,
        'claim_tags': investigation.claim_tags,
        'check_conclusion': investigation.check_conclusion
    })

checker_analysis = FaktisktStatistics(investigation_data, "claim_checker")
print(checker_analysis.n_entirely_false)
print(checker_analysis.n_entirely_true)
print(checker_analysis.n_partly_false)
print(checker_analysis.n_partly_true)
print(checker_analysis.n_investigations)

claimer_analysis = FaktisktStatistics(investigation_data, "claim_maker")
print(claimer_analysis.n_entirely_false)
print(claimer_analysis.n_entirely_true)
print(claimer_analysis.n_partly_false)
print(claimer_analysis.n_partly_true)
print(claimer_analysis.n_investigations)