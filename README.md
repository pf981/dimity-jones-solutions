# Dimity Jones in Puzzle Castle – Solution Scripts

This repository contains Python scripts to decrypt the chapters of [Dimity Jones in Puzzle Castle](https://obnakwa.itch.io/dimityjones), a puzzle-based interactive fiction game.

The game provides a single text file where only the first chapter is readable. Each subsequent chapter is encrypted and must be unlocked by solving a puzzle. This repo contains solutions that automate the decryption process.

## 📁 Project Structure

- `data/`: Contains the original encrypted text file (`00.txt`) and the decrypted chapters (`01.chp`, `02.chp`, etc.).
  - `data/00.txt`: Full text of the [Dimity Jones puzzle book](https://obnakwa.itch.io/dimityjones) (CC BY 4.0).
  - `01.chp`, `02.chp`, etc.: Decrypted chapters, generated after running `uv run pytest`.
- `solutions/`: Python scripts implementing decryption algorithms for each chapter.
- `tests/`: Pytest-based tests that both verify the correctness of decrypted chapters and generate them from the original encrypted text.

## 🚀 Getting Started

### Installation

1. **Install uv:**

   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

1. **Clone the repository:**

   ```bash
   git clone https://github.com/pf981/dimity-jones-solutions.git
   cd dimity-jones-solutions
   ```

## 🧪 Running Tests

Run all test cases with:

```bash
uv run pytest
```

The tests will:

- Decrypt each chapter using the appropriate solution script.
- Verify that the decrypted output matches the expected hashes.
- Save each decrypted chapter to a file like `01.chp`, `02.chp`, etc., in the `data/` directory.

## ✍️ Attribution

This repository includes the puzzle book under its original license:

- **Author:** O.B. Nakwa
- **Original source:** [Dimity Jones on itch.io](https://obnakwa.itch.io/dimityjones)  
- **License:** Creative Commons Attribution 4.0 International (CC BY 4.0): https://creativecommons.org/licenses/by/4.0/  
- **Notes:** This is a verbatim copy in text format. Please see the original site for licensing and updates.

## 💖 Support the Creator

This puzzle book and game were created by **O.B. Nakwa**, not me — this repository only contains my solutions to the puzzles.  

If you enjoyed the original work, consider supporting the creator directly:

- **Official page:** https://obnakwa.itch.io/dimityjones  
- **Donate via PayPal:** https://paypal.me/obnakwa
