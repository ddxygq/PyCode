from elasticsearch import Elasticsearch


def get_conn():
    return Elasticsearch('http://qcloud-test-hadoop01:9200')


def add():
    es = get_conn()
    es.index(index='test', doc_type='test', id=1, body={'text': 'this is a test'})
    es.index(index='test', doc_type='test', id=2, body={'text': 'this is a second test'})


def select():
    docs = get_conn().search(index='test', body={'query': {'match': {'text': 'this test'}}})
    for key, value in docs.items():
        print(key, value)


if __name__ == '__main__':
    # add()
    select()
