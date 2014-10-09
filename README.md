# python-acoustid-api

A lightweight wrapper around the AcoustID API,
meant to facilitate fast and easy submissions and lookups.

Current state: in development.

## Getting Started

Although in development, this wrapper can be installed via Pypi:

```
$ pip install python-acoustid-api
```

## API facilities

Presently covered:

- Track ID lookup
- Fingerprint lookup

## Usage

Look up recordings with a Chromaprint fingerprint

```python
from acoustid_api import AcoustID, Meta

api = AcoustID(<api key>, [format=json|xml])
track_data = api.track('9e1ea2fc-8b0b-40ac-b98a-126a98752002',
                       meta=('recordings', 'sources'))
```

Now, `track_data` now holds the search results:

```json
[{"recordings": [{"sources": 39, "artists": [{"id": "adec1fc3-83c1-48f7-9e49-8347ac6d40b0", "name": "Neu!"}], "duration": 291, "title": "Sonderangebot", "id": "d3f15478-7908-4f68-9daf-96739c6978ca"}], "score": 1.0, "id": "9e1ea2fc-8b0b-40ac-b98a-126a98752002"}]
```

## Testing

If you'd like to run the test suite, first install the requirements:

```shell
$ pip install -r requirements.txt
```

Then set the `ACOUSTID_KEY` environment variable with your API key.

And then run `py.test`:

```shell
$ py.test
```

Warning: this will make call to the live API,
so please do not feel free to go nuts.

## Contributing

Something wrong? Feature missing? Open an issue on this repo
or shoot me a pull request with tests and we'll get it sorted out ASAP.

## Contributing something other than code

If you just want to say thanks, I suggest doing something
donating to the [Ada Initiative](https://adainitiative.org/donate/)
or [fostering an elephant](https://www.sheldrickwildlifetrust.org/asp/fostering.asp).
