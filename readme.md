[branches]
 - windy
## Inventário::
```shell
CREATE TABLE temperatura_exporter (
    id int NOT NULL AUTO_INCREMENT,
    data  DATETIME NOT NULL,
    data_from TIMESTAMP DEFAULT 0,,
    temperatura float(10) NOT NULL,
    umidade float(10) NOT NULL,
    localidade varchar(255) NOT NULL,
    PRIMARY KEY (id)
);
```