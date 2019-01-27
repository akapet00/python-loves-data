import yaml

def yaml_load(filepath):
    """ Loads a yaml file """
    with open(filepath, 'r') as file_descriptor:
        data = yaml.load(file_descriptor)
    return data

def yaml_dump(filepath, data):
    """ Dumps data into a yaml file """
    with open(filepath, 'w') as file_descriptor:
        yaml.dump(data,file_descriptor)

def main():
    # playing around with list in yaml
    filepath = 'sample1.yaml'
    data = yaml_load(filepath)
    print(data)

    # dictionary in yaml
    filepath = 'sample2.yaml'
    data = yaml_load(filepath)
    print(data)
    items = data.get('items')
    for item_key, item_value in items.items():
        print(item_key, ': ', item_value)

    # dumping data in yaml
    filepath = 'sample4.yaml'
    data = {
       'items':{
           'need-to-buy':{
               'sward': 100,
               'axe': 150,
               'boots': 40
               },
           'already-have':{
                'knife',
                'waterbottle'
                }
            }
    }

    yaml_dump(filepath, data)

if(__name__ == '__main__'):
    main()
