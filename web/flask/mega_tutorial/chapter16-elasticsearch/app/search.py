from flask import current_app


def add_to_index(index, model):
    """
    添加数据
    :param index: 索引，通常对应数据库表名
    :param model: 实体数据
    :return:
    """
    if not current_app.elasticsearch:
        return
    payload = {}
    for field in model.__searchable__:
        payload[field] = getattr(model, field)
    current_app.elasticsearch.index(index=index, doc_type=index, id=model.id, body=payload)


def remove_from_index(index, model):
    """
    删除数据
    :param index:  索引，通常对应数据库表名
    :param model:  实体数据
    :return:
    """
    if not current_app.elasticsearch:
        return
    current_app.elasticsearch.delete(index=index, doc_type=index, id=model.id)


def query_index(index, query, page, per_page):
    """
    查询数据
    :param index:  索引，通常对应数据库表名
    :param query: 要查询的关键词
    :param page: 页数
    :param per_page: 每页的数量
    :return:
    """
    current_app.logger.info('elasticsearch keywords -> ' + query)
    search = current_app.elasticsearch.search(
        index=index,
        body={
            'query': {'multi_match': {'query': query, 'fields': ['*']}},
            'from': (page - 1) * per_page, 'size': per_page
        })

    ids = [int(hit['_id']) for hit in search['hits']['hits']]
    return ids, search['hits']['total']
