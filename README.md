# Deprecated

Sorry, I'm no longer maintaining this project.

## US COVID-19 Predictor

This software project tries to predict US COVID-19 cases and deaths.

Based on top of work by Anaiy Somalwar: https://github.com/anaiy2004/COVID-19-Forecasting

In my tests, the predicted deaths were better than predicted cases.

## Disclaimer

While this software project predicts COVID-19, deaths and especially cases are still random. USE THIS SOFTWARE AND DATA AT YOUR OWN RISK!

## Running

You need Python 3(at least 3.8 is recommended) and pip.

First, let's run pip install:

```bash
pip3 install -r requirements.txt
```

This might take some time.

Now, we need to download US data from JHU CSSE COVID-19 Data and sort the downloaded data by date:

```bash
python3 tools/download_us_data.py
```

```bash
python3 tools/date_sort.py US.csv US.csv
```

*NOTE*: The first argument passed to date_sort.py is the input file, US.csv and the second argument is the output file, again, US.csv

Finally let's predict deaths and cases:

```bash
python3 predict_deaths.py US.csv
```

```bash
python3 predict_cases.py US.csv
```

If you want to generate a data.json file, which contains predicted and current total cases and deaths in JSON, run:

```bash
python3 tools/create_data_json.py US.csv
```

The schema of data.json is in data.schema.json.

Having any issues? Simply open an issue.

### Contributing

Simply send a PR ;)

### License

See LICENSE at the root.

### Prediction data

There's also a [data repo](https://github.com/okyanusoz/covid19-us-predictions-data) that contains prediction data in the form of data.json and dataset.csv files that are updated daily. See [the README](https://github.com/okyanusoz/covid19-us-predictions-data/blob/master/README.md) for more info.
