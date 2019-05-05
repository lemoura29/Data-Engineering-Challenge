import pandas as pd
from db import ConnectionClass
from sqlalchemy.types import VARCHAR

class Business(ConnectionClass):
    def __init__(self):
        super().__init__()

    def insert_table(self,table, df):
        self.connect()
        df.to_sql(name=table, con=self.conn, if_exists="replace", index=False)
        self.disconnect()

    def select_table(self, table):
        self.connect()
        return pd.read_sql_query("select * from " + table, self.conn)

    def select_single_table(self):
        self.connect()
        sql = "SELECT c.device_id, lead_id, registered_at, credit_decision, credit_decision_at, signed_at, revenue, a.ad_creative_id, a.campaign_id, cost, clicks, impressions " +\
              "FROM customer_leads_funnel c "+\
              "INNER JOIN (SELECT device_id, ad_creative_id, campaign_id FROM pageviews WHERE campaign_id <> 0 GROUP BY device_id, ad_creative_id, campaign_id) a " + \
              "ON c.device_id = a.device_id " +\
              "INNER JOIN (SELECT campaign_id, ad_creative_id, SUM(cost) as cost, SUM(clicks) as clicks, SUM(impressions) as impressions FROM ads_media_costs " +\
              "GROUP BY campaign_id, ad_creative_id) ad ON a.ad_creative_id = ad.ad_creative_id AND a.campaign_id = ad.campaign_id "

        return pd.read_sql_query(sql, self.conn)

    def select_first_question(self):
        self.connect()
        sql = "SELECT campaign_id, SUM(cost) AS cost "\
              "FROM (SELECT campaign_id, cost FROM single_table GROUP BY campaign_id, cost) AS a "\
              "GROUP BY campaign_id ORDER BY cost DESC LIMIT 1"
        return pd.read_sql_query(sql, self.conn)

    def select_second_question(self):
        self.connect()
        sql = "SELECT campaign_id, SUM(lucro) lucro " \
              "FROM (SELECT campaign_id, (SUM(revenue)-cost) lucro FROM single_table GROUP BY campaign_id, cost) AS a " \
              "GROUP BY campaign_id ORDER BY lucro DESC LIMIT 1"
        return pd.read_sql_query(sql, self.conn)

    def select_third_question(self):
        self.connect()
        sql = "SELECT ad_creative_id, SUM(clicks) clicks " \
              "FROM (SELECT ad_creative_id, clicks FROM single_table WHERE ad_creative_id > 0 GROUP BY ad_creative_id, clicks) a " \
              "GROUP BY ad_creative_id ORDER BY clicks DESC LIMIT 1"
        return pd.read_sql_query(sql, self.conn)

    def select_fourth_question(self):
        self.connect()
        sql = "SELECT ad_creative_id, COUNT(DISTINCT lead_id) leads FROM single_table WHERE ad_creative_id > 0 " \
              "GROUP BY ad_creative_id  ORDER BY leads DESC LIMIT 1"
        return pd.read_sql_query(sql, self.conn)



