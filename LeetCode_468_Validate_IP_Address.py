
# https://leetcode.com/problems/validate-ip-address/submissions/
class Solution:
    def validIPAddress(self, IP: str) -> str:
        code = "Neither"
        try:
            ipsplit = IP.split('.')
            if len(ipsplit) == 4:
                    for n in ipsplit:
                        if 0 > int(n) or 255 < int(n) or str(int(n)) != n:
                            return
                    else:
                        code = "IPv4"

            ipsplit = IP.split(':')
            if len(ipsplit) == 8:
                    for n in ipsplit:
                        if len(n) > 4:
                            return
                        
                        int(n, 16) # will throw if not an hexadecimal int
                    else:
                        code = "IPv6"

        finally:
            return 
