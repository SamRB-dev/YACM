# YACM (Alpha)

Yet Another Clipboard Manager or YACM is a simple tool that aims to be a cli based tool to managing clipboard history written in **Python** and **Rust**.

# Features (ToDo)

1. Copy previous contents from terminal
2. Search contents on from clipboard
3. Export history of a specific date as csv
4. Delete previous content

# Development Stage 1

- [x] Build Daemon
check on the os clipboard and each time new content is available, save the content on json/txt file
- [ ] Systemd Service

## Build daemon

```shell
cargo build -r --target-dir build
```
