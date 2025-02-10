# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count = {}
        for count_pair in cpdomains:
            rep, domain = count_pair.split()
            all_domains = domain.split(".")
            for i in range(len(all_domains)):
                current_domain = (".").join(all_domains[i:])
                count[current_domain] = count.get(current_domain, 0) + int(rep)
        answer = []
        for domain in count:
            answer.append(str(count[domain])+ " "+domain)
        
        return answer