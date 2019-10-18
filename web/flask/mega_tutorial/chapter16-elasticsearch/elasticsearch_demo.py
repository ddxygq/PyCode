from elasticsearch import Elasticsearch


def get_conn():
    return Elasticsearch('http://localhost:9200')


def add():
    """
    如果，id存在，则会替换，即可以实现插入与修改功能
    :return:
    """
    es = get_conn()
    es.index(index='test', doc_type='test', id=1, body={'text': 'this is a test'})
    es.index(index='test', doc_type='test', id=2, body={'text': 'this is a second test'})


def select():
    docs = get_conn().search(index='post', body={'query': {'match': {'body': 'test 0'}}})
    for key, value in docs.items():
        print(key, value)


def delete_index():
    get_conn().indices.delete('test')


if __name__ == '__main__':
    # add()
    select()
    # delete_index()
