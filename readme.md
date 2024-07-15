[branches]
common

## Inventário::
```shell
CREATE TABLE temperatura (
    id int NOT NULL AUTO_INCREMENT,
    data  DATETIME NOT NULL,
    temperatura float(10) NOT NULL,
    local varchar(255) NOT NULL,
    PRIMARY KEY (id)
);
```