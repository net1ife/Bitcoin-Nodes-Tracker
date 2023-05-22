import requests
from collections import Counter


def get_node_data():
    url = 'https://bitnodes.io/api/v1/snapshots/latest/'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get('nodes', {})
    else:
        print("Could not get data from the API")
        return {}


def nodes_per_country(node_data):
    # Country is the 8th item in the details.
    countries = [details[7]
                 for details in node_data.values() if len(details) > 7]
    return Counter(countries)


node_data = get_node_data()
node_counts = nodes_per_country(node_data)

# Sort by node count, in descending order
sorted_node_counts = dict(
    sorted(node_counts.items(), key=lambda item: item[1], reverse=True))

total_nodes = sum(sorted_node_counts.values())

print(f"Total nodes: {total_nodes}\n")
print(f"{'Country':<5} {'Nodes':<7}")
for country, count in sorted_node_counts.items():
    country = 'None' if country is None else country
    print(f"{country:5} {count:<7}")
