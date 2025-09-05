# 1330 두 수 비교하기
'''
두 정수 A와 B가 주어졌을 때, A가 B보다 크면 '>'를 출력하고, A가 B보다 작으면 '<'를 출력하며, A와 B가 같으면 '=='를 출력하는 프로그램을 작성하시오.
'''
A, B = map(int, input().split())
print('>' if A > B else '<' if  A < B else '==')
