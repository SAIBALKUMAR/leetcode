class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result_emails = set()
        for email in emails:
            email_array = email.split("@")
            if len(email_array) != 2:
                continue
            local_name = email_array[0]
            domain_name = email_array[1]
            local_name = local_name.split("+")[0]
            local_name = "".join(local_name.split("."))
            result_email = local_name + "@" + domain_name
            result_emails.add(result_email)
        return len(result_emails)