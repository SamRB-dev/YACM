# YACM (Alpha)

Yet Another Clipboard Manager or YACM is a simple tool that aims to be a cli based tool to managing clipboard history written in **Python** and **Rust** for **Linux**.

## Features (ToDo)

1. Copy previous contents from terminal
2. Search contents on from clipboard
3. Export history of a specific date as csv
4. Delete previous content

## Development Goals

### Platform: Linux, WSL (windows)

- [x] Build Daemon (Rust)
- [ ] Systemd Service (for Systemd)
- [ ] Terminal User Interface (Python)

## Current Status
Tested on WSL on windows and with the daemon running on background, it can fetch the contents from windows clipboard buffer directly.

## Build daemon

```shell
cargo build -r --target-dir build
```
