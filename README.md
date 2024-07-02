

## requirements

```shell 
pip install scrapy
```

## create project
```shell
 crapy genspider coindesk www.coindesk.com
```

## spider
start to crawl
```shell
scrapy crawl coindesk --nolog 
```

## sql
```sql
USE spider;

CREATE TABLE IF NOT EXISTS users (
	id INT AUTO_INCREMENT PRIMARY KEY,    
	title text, 
    link text,
    date VARCHAR(200),
    create_at timestamp DEFAULT CURRENT_TIMESTAMP,
    update_at timestamp DEFAULT CURRENT_TIMESTAMP
);
```