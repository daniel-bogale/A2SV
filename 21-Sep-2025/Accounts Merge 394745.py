# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailToAccount = dict()

        # Step1: map emails to account and if email belongs to several accounts => merge them
        for accountId, accountData in enumerate(accounts):
            for j in range(1, len(accountData)):
                email = accountData[j]
                if email in emailToAccount:
                    uf.union(accountId, emailToAccount[email])
                else:
                    emailToAccount[email] = accountId

        # Step2: regroup email by the main account
        groupByAccount = defaultdict(list)
        for email, accountId in emailToAccount.items():
            mainAccountId = uf.find(accountId)
            groupByAccount[mainAccountId].append(email)

        # Step3: Prepare response to required format [accountName, ...sorteEmails]
        res = []
        for accountId, emails in groupByAccount.items():
            data = [accounts[accountId][0]]
            data.extend(sorted(emails))
            res.append(data)
        return res

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1