import hashlib

members = []
posts = []


class Member:
    def __init__(self):
        print('\n회원정보를 입력해주세요.')
        self.name = input('name: ')
        self.username = input('ID: ')
        self.password = input('PW: ')
        m = hashlib.sha256()
        m.update(self.password.encode('utf-8'))
        # print(m.hexdigest()) 헤싱한 암호를 프린트

        members.append(self.name)

    def display(self):
        print({'name': self.name, 'ID': self.username})


class Post(Member):
    def __init__(self):
        super().__init__()
        print('\n게시물을 3개 작성해주세요.')

        num = 0
        while num <= 2:
            self.title = input('title: ')
            self.content = input('content: ')
            self.author = self.username

            posts.append(self.title)
            posts.append(self.content)
            posts.append(self.author)
            # posts:{}에 posts['title']=self.title 로 저장해보려했는데 실패

            num += 1

            continue


m1 = Post()
m1.display()

m2 = Post()
m2.display()

m3 = Post()
m3.display()


for i, member in enumerate(members):
    print(member)

for i, author in enumerate(posts):
    if author == 'alswo9872':
        print(posts[i-2])
# list인 posts가 아니라 반복문으로 뽑아낸 author 값의 순서로 체킹하다가 오류

for i, content in enumerate(posts):
    # print(type(content)) 모두 str class로 출력
    if '했다' in content:
        print(posts[i-1])
