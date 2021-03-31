from mercari import Mercari
mercari_api = Mercari()
print('_' * 80)
print(mercari_api.name)
print(mercari_api.fetch_all_items(keyword='CHANEL')[0:1])
print(mercari_api.get_item_info('https://www.mercari.com/jp/items/m11000340298/').name)