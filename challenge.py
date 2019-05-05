import pandas as pd
from Utils import Utils
from BusinessLogic import Business


def insert_data():
    b = Business()

    df = pd.read_csv("Arquivos/customer_leads_funnel.csv", header=None)
    df.columns = ['device_id', 'lead_id', 'registered_at', 'credit_decision', 'credit_decision_at', 'signed_at','revenue']
    b.insert_table("customer_leads_funnel", df)

    dgoogle = pd.read_json('Arquivos/google_ads_media_costs.jsonl', lines=True)
    dgoogle.columns = ['ad_creative_id', 'ad_creative_name', 'clicks', 'cost', 'date', 'campaign_id', 'campaign_name', 'impressions']

    dfacebook = pd.read_json('Arquivos/facebook_ads_media_costs.jsonl', lines=True)
    dfacebook.columns = ['clicks', 'cost', 'date', 'campaign_id', 'campaign_name', 'impressions']

    dAds = pd.concat([dgoogle,dfacebook], ignore_index=True, sort=False)
    dAds = dAds.fillna(0)

    b.insert_table('ads_media_costs',dAds)


def read_insert_pageviews():
    utils = Utils()
    b = Business()
    ref_arquivo = open('Arquivos/pageview.txt','r')
    data = []
    linha = ref_arquivo.readline()
    while linha:
        valores = linha.split("|")
        device_id = utils.separa_string(valores[1],':',1)
        url = utils.separa_urls_params(valores[0])
        campaign_id = pd.to_numeric(utils.extrai_campos(url, 'campaign_id'))
        creative_id = pd.to_numeric(utils.extrai_campos(url, 'ad_creative_id'))
        data.append({'device_id': device_id,'campaign_id': campaign_id, 'ad_creative_id': creative_id})
        linha = ref_arquivo.readline()

    b.insert_table('pageviews',pd.DataFrame(data))
    ref_arquivo.close()

def create_single_table():
    b = Business()
    insert_data()
    read_insert_pageviews()
    dads = b.select_single_table()
    b.insert_table('single_table',dads)


if __name__ == '__main__':
    b = Business()
    create_single_table()
    print(b.select_first_question())
    print(b.select_second_question())
    print(b.select_third_question())
    print(b.select_fourth_question())
