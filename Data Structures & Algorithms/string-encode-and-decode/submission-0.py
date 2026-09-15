class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=""
        for w in strs:
            encoded+=str(len(w))+"#"+w
        return encoded


    def decode(self, s: str) -> List[str]:
        decoded=[]
        i=0
        while i<len(s):
            hash_index=s.find("#",i)
            leng=int(s[i:hash_index])
            start = hash_index+1
            end= start+leng

            decoded.append(s[start:end])
            i=end
        return decoded
