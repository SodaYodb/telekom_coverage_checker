# Telekom Coverage Checker

This script allows you to check the maximum internet connection speed provided by Telekom for a given address. It utilizes the Telekom Coverage Checker API to retrieve the information.
I would recommend to add a small delay to the queries to not stress the telecom server too much.

## Prerequisites

To run this script, make sure you have the following dependencies installed:

- Python 3.x
- requests library

You can install the requests library using pip:

```
pip install requests
```

## Usage

To use the script, provide the following details in the `sample` list:

- Postal code (`IN_PLZ`)
- City (`IN_CITY`)
- Street (`IN_STREET`)
- State (`IN_STATE`)

For addresses in Germany, the state does not have to be specified. For other countries I have not tested this.


For example, to check the coverage for the address "Alter Markt 6, 39104, Magdeburg, Sachsen-Anhalt", use the `sample` list:

```python
sample = ["39104", "Magdeburg", "Alter Markt 6", "Sachsen-Anhalt"]
```

Then, execute the script and it will output the maximum internet connection speed available for the provided address.

```python
print(request_telekom(sample[0], sample[1], sample[2], sample[3]))
```

The result will be displayed in megabits per second (Mbps).

Please note that the availability of data for an address may vary. In some cases, there might be no internet connection available, in which case the script will display "NO DATA".

Feel free to modify the script according to your needs or incorporate it into your own projects.
