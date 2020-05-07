class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = []

        def backtrack(track):
            """ track is a list """
            # terminate condition
            ptr = len(track)
            if ptr == len(S):
                res.append("".join(track))
                return

            if S[ptr].isalpha():
                for case in ["lower", "upper"]:
                    if case == "lower":
                        track.append(S[ptr].lower())
                        backtrack(track)
                        track.pop()
                    else:
                        track.append(S[ptr].upper())
                        backtrack(track)
                        track.pop()
            else:
                track.append(S[ptr])  # make choice
                backtrack(track)  # backtrack
                track.pop()  # remove choice

        backtrack([])
        return res