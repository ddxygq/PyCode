broker_url = 'redis://:redis@192.168.199.198:6379'
result_backend = 'redis://:redis@192.168.199.198:6379/1'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'Europe/Oslo'
enable_utc = True
