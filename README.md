# DCS World Module Price Tracker

Keep track of prices for DCS World flight simulator modules and receive notifications when modules go on sale. This Python-based web scraper gathers pricing information from the DCS World website and alerts you when discounts are available using ntfy.sh.

## Features

- Automatic price tracking for DCS World flight simulator modules.
- Push notifications via [ntfy.sh](ntfy.sh).

## Installation

1. Clone this repository to your local machine using:

    ```bash
    git clone https://github.com/yourusername/DCS-Module-Price-Tracker.git
    ```

1. Navigate to the project directory:

    ```bash
    cd DCS-Module-Price-Tracker
    ```

1. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

Open the DCSModules.csv file in a text / spreadsheet editor.
Modify the MODULES list to include the DCS World modules you're interested in tracking.
Create a file named `.env` on the root of the project and add the folowing variables:
```bash
USERNAME=ntfyuser
PASSWORD=ntfypassword
SERVER_URL=https://ntfy.sh/
TOPIC=your-topic
```

## Usage

Run the scraper script to start tracking module prices:

```bash
python scraper.py
```

The scraper will gather pricing information and notify you when prices change or discounts are available.

## Contributing

Contributions are welcome! If you have ideas for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the GPL-3.0 License.

Happy flying!