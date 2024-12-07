# YACM (Alpha)

Yet Another Clipboard Manager or YACM is a simple tool that aims to be a cli based tool to managing clipboard history written in **Python** and **Rust** for **Linux**.

## Features (ToDo)

1. Copy previous contents from terminal
2. Search contents on from clipboard
3. Export history of a specific date as csv
4. Delete previous content

## Development Goals

### Platform: Linux

- [x] Build Daemon (Rust)
- [ ] Systemd Service (for Systemd)
- [ ] Terminal User Interface

## Build daemon

```shell
cargo build -r --target-dir build
```
