from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods import posts

wp = Client('http://www.ikeguang.com/xmlrpc.php', 'keguang', '******')


def post_new_article(title, content, terms_names):
    post = WordPressPost()
    post.title = title
    post.content = content
    post.post_status = 'publish'  # 文章状态，不写默认是草稿，private表示私密的，draft表示草稿，publish表示发布
    post.terms_names = terms_names

    post.id = wp.call(posts.NewPost(post))
    return post.id


if __name__ == '__main__':
    post_new_article('python发布wordpress文章测试', 'python发布wordpress文章测试')
