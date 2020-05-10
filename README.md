# python-cassandra-docker-compose
## Workflow

__wait for one minute after docker-compose up for cassandra to start__

```
docker-compose up
docker exec -it app python3 create_tables.py
docker exec -it app python3 seed_db.py
docker exec -it app python3 query.py
```


## Reference:
https://github.com/datastax/python-driver/blob/master/example_core.py

https://towardsdatascience.com/getting-started-with-apache-cassandra-and-python-81e00ccf17c9

https://blog.alejandrocelaya.com/2017/04/21/set-specific-ip-addresses-to-docker-containers-created-with-docker-compose/
