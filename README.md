# Dimity Jones in Puzzle Castle – Solution Scripts

This repository contains Python scripts to decrypt the chapters of [Dimity Jones in Puzzle Castle](https://obnakwa.itch.io/dimityjones), a puzzle-based interactive fiction game.

The game provides a single text file where only the first chapter is readable. Each subsequent chapter is encrypted and must be unlocked by solving a puzzle. This repo contains solutions that automate the decryption process.

## 📁 Project Structure

- `data/`: Contains the original encrypted text file (`00.txt`) and the decrypted chapters (`01.chp`, `02.chp`, etc.)
- `solutions/`: Python scripts that implement decryption algorithms for each chapter.
- `tests/`: Pytest-based tests that check the correctness of decrypted chapters.
- `requirements.txt`: Lists Python dependencies required to run the project.

## 🚀 Getting Started

### Prerequisites

- Python `3.12`
- `pip` package manager

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/pf981/dimity-jones-solutions.git
   cd dimity-jones-solutions
   ```

2. **Download the encrypted text file:**

   Visit the [Dimity Jones in Puzzle Castle page](https://obnakwa.itch.io/dimityjones) and download the text file.  
   Save it as `data/00.txt` in the repository.

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## 🧪 Running Tests

Run all test cases with:

```bash
pytest
```

The tests will:

- Decrypt each chapter using the appropriate solution script.
- Verify that the decrypted output matches the expected hashes.
- Save each decrypted chapter to a file like `01.chp`, `02.chp`, etc., in the `data/` directory.
