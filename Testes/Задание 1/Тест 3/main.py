def unic_id(list_id):
    id_city = []
    for id_list in list_id.values():
        for id_user in id_list:
          id_city.append(id_user)
    unic_id_set = set(id_city)
    return unic_id_set


if __name__ == "__main__":
    ids = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}
    id_set = unic_id(ids)
    print(id_set)
