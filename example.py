from faktiskt import FaktisktScraper

investigation_search = FaktisktScraper.InvestigationSearch()

for url in investigation_search.fetch_investigation_url():
    investigation = FaktisktScraper.Investigation(url)
    print("- Claim at: {}".format(investigation.claim_url))
    print("- Claim checked by: {}".format(investigation.claim_checker))
    print("- Claim made by: {}".format(investigation.claim_maker))
    print("- Claim: {}".format(investigation.claim))
    print("- Claim checked date: {}".format(investigation.check_date))
    print("- Claim tagged as: {}".format(investigation.claim_tags))
    print("- Claim concluded as: {}".format(investigation.check_conclusion))
