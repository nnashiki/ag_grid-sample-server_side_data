# ag_grid-sample-server_side_datasource
ag_grid の server_side_datasource の サンプルを実装


API のビルド

```
docker build -t apimock .
docker run -p 9000:80 --rm -v $(PWD)/app:/app --name apimock apimock
```

フロント・サイドの実装

```
docker run --rm -p 5000:80 -v $PWD/src:/usr/share/nginx/html --name grid -d nginx
```



