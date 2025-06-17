# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [0.1.0]

### Added
- Initial implementation of Prometheus exporter for internet speed test metrics
- Periodic execution of speed tests with configurable interval (via `SPEEDTEST_INTERVAL`)
- `/metrics` endpoint exposing Prometheus-compatible metrics
- Structured logging via `logging_config.yaml`
- Configuration management via environment variables with defaults
