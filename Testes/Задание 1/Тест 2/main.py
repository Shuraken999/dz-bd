def max_sales(statist_list):
    m_sales = 0
    for sales in statist_list:
        if m_sales < statist_list[sales]:
            m_sales = statist_list[sales]
            result = sales
    return result


if __name__ == "__main__":
    stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
    maximum = max_sales(stats)
    print(maximum)
