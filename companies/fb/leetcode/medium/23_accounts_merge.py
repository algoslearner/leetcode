'''
Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

 

Example 1:

Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Explanation:
The first and second John's are the same person as they have the common email "johnsmith@mail.com".
The third John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
Example 2:

Input: accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
Output: [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]
 

Constraints:

1 <= accounts.length <= 1000
2 <= accounts[i].length <= 10
1 <= accounts[i][j] <= 30
accounts[i][0] consists of English letters.
accounts[i][j] (for j > 0) is a valid email.
'''

# DFS
# Time : O(NK log NK)
# Space: O(NK)

class Solution:
    def dfs(self, node, graph, visited, component):
        if visited[node]:
            return
        visited[node] = True
        component.append(node)
        for neighbor in graph[node]:
            if not visited[neighbor]:
                self.dfs(neighbor, graph, visited, component)
    
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = {}
        visited = {}
        email_to_account = {}

        # set up graph, visited 
        for account in accounts:
            emails = account[1:]
            first_email = emails[0] # could've been last or any other
            for email in emails:
                # add undirected edges b/w first node and other nodes
                graph.setdefault(email, set()).add(first_email)
                graph.setdefault(first_email, set()).add(email)
                visited[email] = False
                email_to_account[email] = account[0] # name
        
        output = []
        for email,account in email_to_account.items():
            if visited[email]:
                continue
            # visited dict ensures that DFS gets called for every component
            # and NOT on every node
            nodes = [] # to fill all nodes (emails) in the component
            self.dfs(email, graph, visited, nodes)
            output.append([account] + sorted(nodes))
            
        return output
   
   
   # METHOD 2 - DFS - clearer functions to understand
   class Solution: 
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(list)
        visited = set()
        merged_accounts = []
        
        def buildGraph(accounts):
            for account in accounts:
                first_email = account[1]
                other_emails = account[2:]
                graph[first_email].extend(other_emails)
                for other_email in other_emails:
                    graph[other_email].append(first_email)
                    
        def dfs(merged_account, email):
            visited.add(email)
            merged_account.append(email)
            for neighbour in graph[email]:
                if neighbour not in visited:
                    dfs(merged_account, neighbour)
            
        
        buildGraph(accounts)
        for account in accounts:
            name = account[0]
            first_email = account[1]
            if first_email not in visited:
                merged_account = []
                dfs(merged_account, first_email)
                merged_accounts.append([name] + sorted(merged_account))
        
        return merged_accounts
    
    # https://leetcode.com/problems/accounts-merge/discuss/109161/Python-Simple-DFS-with-explanation!!!    
