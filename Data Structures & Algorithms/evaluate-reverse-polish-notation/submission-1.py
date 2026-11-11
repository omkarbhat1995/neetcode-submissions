class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = ('+','-','/','*')
        st = []
        for token in tokens:
            if token in operations:
                b = int(st.pop())
                a = int(st.pop())
                if token == '+':
                    st.append(str(a+b))
                elif token == '-':
                    st.append(str(a-b))
                elif token =='/':
                    st.append(str(a//b))
                else:
                    st.append(str(a*b))
            else:
                st.append(token)
        return int(st.pop())