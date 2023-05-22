## Bitcoin Nodes Tracker

This script connects to the Bitnodes API, gathers data about Bitcoin nodes, and counts the nodes per country.

## Usage

To run the script, you need Python 3 and the `requests` library installed. If `requests` is not installed, you can install it via pip:

```bash
pip install requests
```

Once you have Python 3 and `requests` installed, you can run the script with:

```bash
python3 nodes.py
```

## Output

The script prints out the total count of nodes and a list of ISO country codes along with the count of nodes for each code. The list is sorted in descending order by the count of nodes. 

If the country couldn't be determined for some nodes, these nodes are assigned the country code `None`.

For example, the output might look like this:

```
Total nodes: 17067

Country Nodes  
None  10543  
US    1635   
DE    1369   
FR    471    
...
```

In this example, there are 17067 nodes in total, 10543 of which don't have a determined country. The rest of the nodes are broken down by country, with "US" (United States) having 1635 nodes, "DE" (Germany) having 1369 nodes, "FR" (France) having 471 nodes, and so forth.

## Limitations and improvements

This script uses the Bitnodes API, which may not always be able to determine the country for all nodes. Therefore, the total number of nodes and the counts per country are estimates and may not be completely accurate.
