""" TinyURL是一种URL简化服务， 比如：当你输入一个URL https://leetcode.com/problems/design-tinyurl 时，
它将返回一个简化的URL http://tinyurl.com/4e9iAk.

要求：设计一个 TinyURL 的加密 encode 和解密 decode 的方法。
你的加密和解密算法如何设计和运作是没有限制的，你只需要保证一个URL可以被加密成一个TinyURL，并且这个TinyURL可以用解密方法恢复成原本的URL。

hash map
import random
random.sample(chars, k)
random.randint(s,t)  # int \in [s,t]
"""
import random

class Codec:
    def __init__(self):
        self.chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.urldict = {}

    def get_randstr(self):
        rand_code = random.sample(self.chars, 6)
        return "".join(rand_code)

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        key = self.get_randstr()
        while key in self.urldict:
            key = self.get_randstr()
        self.urldict[key] = longUrl
        return "http://tinyurl.com/" + key        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        key = shortUrl.split('/')[-1]
        return self.urldict[key]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))