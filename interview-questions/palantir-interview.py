# Interview question for Palantir Software Engineering Internship

"""
You are in charge of a display advertising program. Your ads are displayed on websites all over the internet. You have some CSV input data that counts how many times that users have clicked on an ad on each individual domain. Every line consists of a click count and a domain name, like this:

counts = [ "900,google.com",
     "60,mail.yahoo.com",
     "10,mobile.sports.yahoo.com",
     "40,sports.yahoo.com",
     "300,yahoo.com",
     "10,stackoverflow.com",
     "20,overflow.com",
     "5,com.com",
     "2,en.wikipedia.org",
     "1,m.wikipedia.org",
     "1,mobile.sports",
     "1,google.co.uk"]

Write a function that takes this input as a parameter and returns a data structure containing the number of clicks that were recorded on each domain AND each subdomain under it. For example, a click on "mail.yahoo.com" counts toward the totals for "mail.yahoo.com", "yahoo.com", and "com". (Subdomains are added to the left of their parent domain. So "mail" and "mail.yahoo" are not valid domains. Note that "mobile.sports" appears as a separate domain near the bottom of the input.)

Sample output (in any order/format):

calculateClicksByDomain(counts) =>
com:                     1345
google.com:              900
stackoverflow.com:       10
overflow.com:            20
yahoo.com:               410
mail.yahoo.com:          60
mobile.sports.yahoo.com: 10
sports.yahoo.com:        50
com.com:                 5
org:                     3
wikipedia.org:           3
en.wikipedia.org:        2
m.wikipedia.org:         1
mobile.sports:           1
sports:                  1
uk:                      1
co.uk:                   1
google.co.uk:            1

n: number of domains in the input
(individual domains and subdomains have a constant upper length)

"""

counts = [
    "900,google.com",
    "60,mail.yahoo.com",
    "10,mobile.sports.yahoo.com",
    "40,sports.yahoo.com",
    "300,yahoo.com",
    "10,stackoverflow.com",
    "20,overflow.com",
    "5,com.com",
    "2,en.wikipedia.org",
    "1,m.wikipedia.org",
    "1,mobile.sports",
    "1,google.co.uk" 
]

# domain_counts = dict()

def getUniqueDomains(domain_counts):
    return_dict = dict()
    domains = [
        domain_str.split(",")[1] for domain_str in domain_counts
    ]
    
    for domain in domains:
        str_list = domain.split(".")
        for i in range(len(str_list)):
            domain_str = ".".join(str_list[i:])
            if (domain_str.endswith(".com") or domain_str.endswith(".sports") or domain_str.endswith(".uk") or domain_str.endswith(".org")):
                return_dict[domain_str] = 0
    
    return return_dict
    
def countDomains(domain_dict):
    counts_dict = {
        input_str.split(",")[1]: int(input_str.split(",")[0])
        for input_str in counts
    }
    
    for domain in domain_dict:
        count = sum(counts_dict[d] for d in counts_dict if domain in d)
        domain_dict[domain] = count
    
    return domain_dict

def main(counts):
    unique_domains = getUniqueDomains(counts)
    domain_counts = countDomains(unique_domains)
    
    for domain, count in domain_counts.items():
        print(f"{domain}: {count}")
    
    return domain_counts
    

if __name__ == "__main__":
    main(counts)