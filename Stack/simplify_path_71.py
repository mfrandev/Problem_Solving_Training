class Solution:
    def simplifyPath(self, path: str) -> str:
        split_path = path.split('/')
        stack = []
        for level in split_path:and len(stack) > 0
            if level == "" or level == ".":
                continue
            elif level == "..":
                if len(stack) > 0:
                    stack.pop()
                continue
            stack.append(level)
        ans = ''
        for i in stack:
            ans += f'/{i}'
        return ans if ans != '' else '/'
