import requests, re, pymongo, random, time,logging
from lxml import html

# from cookie import cookie
# from header import header
# header = {
#     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
# cookie = {
#     'Cookie': 'acw_tc=AQAAADAcklWo/QEAo/ycy4VyyjbBSrqv; UM_distinctid=15ebd879834881-05709224e69dfb-3976045e-13c680-15ebd87983551c; _uab_collina=150641833753343192906233; PHPSESSID=8vo5en6lgbtiqqk8uk3mqi29l0; _umdata=2FB0BDB3C12E491DBA56D15D2243C7A74D000D6C33FCD16F79C1C9D42333892F7F8B3CB72F680169CD43AD3E795C914CD1735650C982B7CFD9C19118AC57B5DD; zg_did=%7B%22did%22%3A%20%2215ebd87988c698-01b6332be7046b-3976045e-13c680-15ebd87988d407%22%7D; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201506492681105%2C%22updated%22%3A%201506492694774%2C%22info%22%3A%201506418333856%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.qichacha.com%22%2C%22cuid%22%3A%20%22c11b6f0a73cca35a27a8af6db3c88b92%22%7D; CNZZDATA1254842228=713826384-1506416515-%7C1506564195'}

collection = pymongo.MongoClient(host='127.0.0.1', port=27017)['Falonie']['淄烟-24-21-10.20_checklist']
header = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
]
cookie = [
    '_uab_collina=150527284704149589548835; UM_distinctid=15ea3addeae8d3-07742f025e0c8f-3976045e-13c680-15ea3addeafa93; PHPSESSID=58noalcg5ue46bmks5l11g5cl4; _umdata=E2AE90FA4E0E42DE0F446AE0957BCA8A133E0B34391C28947685CA351FCA05F1C03BAF7D07039AA4CD43AD3E795C914C329F984629917D25CAF964CA6594FBB0; acw_tc=AQAAAHKLHU7oVwgAo/ycy9QODOpwsN4y; zg_did=%7B%22did%22%3A%20%2215e7940da0f78f-01ffe099dc343d-3976045e-13c680-15e7940da10ba7%22%7D; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201508482281848%2C%22updated%22%3A%201508482311698%2C%22info%22%3A%201508134371883%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%22dad2b2131a760fad57cbbb67ceea827c%22%7D; CNZZDATA1254842228=1726320973-1505979679-%7C1508478545',
    # 'acw_tc=AQAAACkGPXV8Og0Ao/ycy/5JP413geQN; UM_distinctid=15f2ea41db6b3e-003cb5004328df-3976045e-13c680-15f2ea41db782f; hasShow=1; _uab_collina=150831603022193127647865; _umdata=6AF5B463492A874D59D5F34FAF3E894CA7C03E5352A97ACA7C4D5C3C9F4F34A87A6C14B58E60FDB8CD43AD3E795C914CDE0437EBCF76BAEACE0DF5E624BA9CC0; PHPSESSID=jq77r8gu6i5ctgqo3paap7saq7; zg_did=%7B%22did%22%3A%20%2215f2ea41e27ab-04bf4a8aea9832-3976045e-13c680-15f2ea41e2885f%22%7D; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201508316028459%2C%22updated%22%3A%201508316058061%2C%22info%22%3A%201508316028461%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%228df61d213235daf577fa1bf530ea2748%22%7D; CNZZDATA1254842228=2138888725-1508312600-%7C1508312600',
    # '_uab_collina=150527284704149589548835; UM_distinctid=15ea3addeae8d3-07742f025e0c8f-3976045e-13c680-15ea3addeafa93; acw_tc=AQAAABLs9nqUEwUAo/ycy2+t6j46trKn; hasShow=1; _umdata=E2AE90FA4E0E42DE0F446AE0957BCA8A133E0B34391C28947685CA351FCA05F1C03BAF7D07039AA4CD43AD3E795C914C0740E60E336CD4FCC1938A36DBAF3938; PHPSESSID=58noalcg5ue46bmks5l11g5cl4; zg_did=%7B%22did%22%3A%20%2215e7940da0f78f-01ffe099dc343d-3976045e-13c680-15e7940da10ba7%22%7D; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201508129130788%2C%22updated%22%3A%201508129153785%2C%22info%22%3A%201507529495851%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%22dad2b2131a760fad57cbbb67ceea827c%22%7D; CNZZDATA1254842228=1726320973-1505979679-%7C1508126805',
    # 'acw_tc=AQAAAD8yP3sDXgsAo/ycy3KuNSp6lRPv; UM_distinctid=15f2326491f698-00c0ab4091eb14-3976045e-13c680-15f23264920334; hasShow=1; _uab_collina=150812323530791705371175; _umdata=BA335E4DD2FD504F27B2604E28E497D4C964E255C35FE09CE6D9B0F11D30DF6A8D3574F242EF9303CD43AD3E795C914CB605150709C0BF60F46748991AE50298; PHPSESSID=627g6bi0er6q50k1inulfc79d0; zg_did=%7B%22did%22%3A%20%2215f2326493929e-058db831af14d1-3976045e-13c680-15f2326493a217%22%7D; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201508129029069%2C%22updated%22%3A%201508129369009%2C%22info%22%3A%201508123232585%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%228df61d213235daf577fa1bf530ea2748%22%7D; CNZZDATA1254842228=1002996613-1508118197-%7C1508126805'
]


def check():
    with open('/media/salesmind/Other/Shell/淄烟-24-21-10.20.txt', 'r') as f:
        for i, line in enumerate(f.readlines(), 1):
            print(i, line.strip())
            url = 'http://www.qichacha.com/search?key={}'
            print(url.format(line.strip()))
            # response = requests.get(url=url.format(line.strip()), headers=header,
            #                         cookies=cookie).text
            response = requests.get(url=url.format(line.strip()), headers={'User-Agent': random.choice(header)},
                                    cookies={'Cookie': random.choice(cookie)}).text
            sel = html.fromstring(response)
            company_name = sel.xpath('//*[@id="searchlist"]/table/tbody/tr[1]/td[2]/a/descendant::text()')
            company = ''.join(str(i).strip() for i in company_name)
            # if company.__len__()>1:
            # try:
            print(company)
            # logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S: %p', level=logging.DEBUG)
            # logging.info(msg='{0},{1}'.format(line.strip(),company))
            a = {'company1': line.strip(), 'company2': company}
            collection.insert(a)
            # except Exception as e:
            #     break
            time.sleep(7)


def check2():
    url = 'http://www.qichacha.com/search?key={}'
    response = requests.get(url=url.format('龙口市胜通物流有限公司'), headers=header,
                            cookies=cookie).text
    sel = html.fromstring(response)
    company_name = sel.xpath('//*[@id="searchlist"]/table/tbody/tr[1]/td[2]/a/descendant::text()')
    company = ''.join(str(i).strip() for i in company_name)
    print(company)


if __name__ == '__main__':
    check()