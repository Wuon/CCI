#
# @lc app=leetcode id=811 lang=python3
#
# [811] Subdomain Visit Count
#

# @lc code=start
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        store = {}
        output = []
        for cpdomain in cpdomains:
            count, url = cpdomain.split(" ")
            splitDomain = url.split(".")
            for i in range(len(splitDomain)):
                cur = '.'.join(splitDomain[i:])
                if cur not in store:
                    store[cur] = 0
                store[cur] += int(count)
        for entry in store:
            output.append(str(store[entry]) + " " + entry)
        return output

# @lc code=end
