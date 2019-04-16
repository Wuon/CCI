class Solution:
    def numUniqueEmails(self, emails: 'List[str]') -> 'int':
        s = set()
        for email in emails:
            a = email.split("@")
            b = a[0].replace('.', '').split("+")
            s.add(b[0] + "@" + a[1])
        return len(s)
