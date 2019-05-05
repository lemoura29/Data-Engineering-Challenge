
# Creditas Data Engineering Challenge

## Instructions

Faça download da solução e abra em alguma IDE. Eu utilizei o PyCharm. 
Execute o arquivo **challenge.py**, nele estão as principais funcionalidades da solução.
Ao executar ele irá ler os arquivos, salvá-los em tabelas, criar uma única tabela e dará as repostas das 4 questões solicitadas.
O banco foi criado e manipulado utilizando SQLite.

## Answers

### 1. What was the most expensive campaign?

``` 
SELECT campaign_id, SUM(cost) AS cost 
FROM 
	(SELECT campaign_id, cost FROM single_table GROUP BY campaign_id, cost) AS a 
GROUP BY campaign_id 
ORDER BY cost DESC LIMIT 1
```

#### `Campaign: 1004 - Cost: 15.626,58`

### 2. What was the most profitable campaign?

```
SELECT campaign_id, SUM(lucro) lucro 
FROM 
  (SELECT campaign_id, (SUM(revenue)-cost) lucro FROM single_table GROUP BY campaign_id, cost) AS a 
GROUP BY campaign_id 
ORDER BY lucro DESC LIMIT 1
```

#### `Campaign: 1003 - Profit: 34.065,47`


### 3. Which ad creative is the most effective in terms of clicks?

```
SELECT ad_creative_id, SUM(clicks) clicks 
FROM 
  (SELECT ad_creative_id, clicks FROM single_table WHERE ad_creative_id > 0 GROUP BY ad_creative_id, clicks) a 
GROUP BY ad_creative_id 
ORDER BY clicks DESC LIMIT 1
```

#### `Ad creative: 20003 - Clicks 27.911.110`

### 4. Which ad creative is the most effective in terms of generating leads?

```
SELECT ad_creative_id, COUNT(DISTINCT lead_id) leads 
FROM single_table 
WHERE ad_creative_id > 0 
GROUP BY ad_creative_id  
ORDER BY leads DESC LIMIT 1
```

#### `Ad creative: 20003 - Leads: 1002`

## Extra questions

#### What would you suggest to process new incoming files several times a day?
  Disponibiliza-los em um diretório pré determinado onde alguma ferramenta consiga identificar e manipula-los automáticamente.
#### What would you suggest to process new incoming data in near real time?
  Talvez um processamento via streaming como a presente no Apache.
#### What would you suggest to process data that is much bigger?
  Utilizar ferramentas análiticas de Big Data como o Hadoop e banco de dados NoSQL.
#### What would you suggest to process data much faster?
  Utilizando processamento nas nuvens.