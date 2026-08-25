# Python-PhilSys-Packet-Backup

Command-line Python tools for backing up PhilSys registration packets (and related Reg-client data) from a source machine — either copying all packets at once, or copying only packets/DB/keys within a specific date range.

**Ready-to-use executables are available for each build's `/dist` folder — no Python installation required.**

## Description

The repository contains two builds:

- **Build v1 copy all** — copies every `.zip` and `.html` packet file from a source folder (and its subfolders) to a destination folder in one shot.
- **Build v2 copy date range** — a more targeted backup tool: given a Reg-client `packet-manager` path, a date range, a `db` path, and a `.mosipkeys` path, it creates a new dated folder and copies the `db` folder, `.mosipkeys` folder, and only the `.zip`/`.html` packets created within that date range.

## Features

**Build v1 (copy all):**
- Recursively scans a source folder for `.zip` and `.html` files
- Copies all matching files to a destination folder
- Progress bar via `tqdm`

**Build v2 (copy date range):**
- Prompts for the Reg-client `packet-manager` path, a start/end date, the `db` path, and the `.mosipkeys` path
- Creates a new destination folder named `packets (<startdate>-<enddate>)` on drive `D:`, with a `packet-manager` subfolder
- Copies the `db` and `.mosipkeys` folders in full
- Filters and copies only `.zip`/`.html` packets whose file modification date falls within the specified date range
- Prints which files were included/excluded, and a completion message

## Tech Stack

- **Python 3**
- [`DateTime`](https://pypi.org/project/DateTime/) `5.5`
- [`tqdm`](https://pypi.org/project/tqdm/) `4.66.5` (Build v1 — progress bar)
- `future` (Build v2 — used via `future.backports.datetime`; not currently listed in `requirements.txt`)
- `os`, `shutil`, `time`, `traceback`, `datetime` (Python standard library)

## Prerequisites

- Windows OS (Build v2 writes its output to drive `D:` by default)
- Python 3 (only needed if running from source — the packaged executables require no Python installation)

## Installation

Clone the repository:

```bash
git clone https://github.com/paoradox/Python-PhilSys-Packet-Backup.git
cd Python-PhilSys-Packet-Backup
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Build v2 also imports `future.backports.datetime`, which requires the `future` package — install it if not already present:

```bash
pip install future
```

## Usage

### Build v1 — copy all packets

```bash
cd "Build v1 copy all"
python copyallpackets.py
```

Choose `Y` to start, then enter:
1. The source folder path
2. The destination folder path

All `.zip` and `.html` files found (recursively) in the source are copied to the destination.

### Build v2 — copy packets within a date range

```bash
cd "Build v2 copy date range"
python backuppacketsaccdate.py
```

**Note:** close RegClient before running, and coordinate with your I.S.A. as prompted by the tool.

Choose `Y` to start, then enter:
1. Path to the `packet-manager` folder (e.g. `C:\PhilSys_20210713\Reg-client.1.4.4_012122\packet\packet-manager`)
2. Start date (`yyyy-mm-dd`)
3. End date (`yyyy-mm-dd`)
4. Path to the `db` folder (e.g. `C:\PhilSys_20210713\Reg-client.1.4.4_012122\Reg-client.1.4.4_012122\db`)
5. Path to the `.mosipkeys` folder (e.g. `C:\ProfileUser\PhilSys\.mosipkeys`)

The tool creates `D:\packets (<startdate>-<enddate>)\` containing copies of `db`, `.mosipkeys`, and the matching packets under a `packet-manager` subfolder.

### Running the packaged executables

Pre-built executables are available in each build's own `dist` folder — no Python installation required:

- `Build v1 copy all/dist/copyallpackets.exe`
- `Build v2 copy date range/dist/run-backuppacketsaccdate.exe`

## Project Structure

```
Python-PhilSys-Packet-Backup/
├── Build v1 copy all/
│   ├── dist/
│   │   └── copyallpackets.exe        # Packaged executable
│   ├── copyallpackets.py             # Copies all .zip/.html packets
│   └── ico.ico
├── Build v2 copy date range/
│   ├── dist/
│   │   └── run-backuppacketsaccdate.exe   # Packaged executable
│   ├── backuppacketsaccdate.py       # Copies packets/db/keys within a date range
│   ├── playground.py                 # Scratch/test script (date-math experiment)
│   ├── playground2.py                # Scratch/test script (date-math experiment)
│   └── ico.ico
└── requirements.txt
```

## License

Not specified.
