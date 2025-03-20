# Dimity Jones in Puzzle Castle Solutions

## Introduction

[Dimity Jones in Puzzle Castle](https://obnakwa.itch.io/dimityjones) is a single text file where only the first chapter is readable. Subsequent chapters must be deciphered, using the answers to puzzles.

This repository provides solutions to each chapter and decrypts the file.

## Usage

1. Clone the repo `git clone https://github.com/pf981/dimity-jones-solutions.git`
2. Download the [Dimity Jones text file](https://obnakwa.itch.io/dimityjones) and save it as `data/00.txt`
3. Install requirements `pip install -r requirements.txt`
4. Run with `pytest`

`pytest` will generate the decrypted chapters in `data/01.chp`, `data/02.chp` etc. It will check that the decrypted files match the expected hash.
