# Speedtest Prometheus Exporter

This application runs periodic internet speed tests using [Ookla's Speedtest CLI](https://www.speedtest.net/apps/cli) 
and exposes the results as Prometheus metrics.

---

## Usage

Build and run the Docker container:

```shell
docker build -t speedtest-exporter .
docker run -p 8000:8000 speedtest-exporter
```

You can now access metrics at:
http://localhost:8000/metrics

## Configuration

You can configure the exporter using environment variables:

| Variables          | Description                                | Default |
|--------------------|--------------------------------------------|---------|
| SPEEDTEST_INTERVAL | Interval in seconds between speedtest runs | `600`   |
| TEST_MODE          | Use test mode with mock data               | `false` |

You can set these variables using the -e flag in Docker:

```shell
docker run -e SPEEDTEST_INTERVAL=1000 -p 8000:8000 speedtest-exporter
```

⚠️ Note: Setting SPEEDTEST_INTERVAL too low (e.g., under 5 minutes) may cause Ookla to rate-limit your access
to the Speedtest service. It is recommended to keep the interval at 10 minutes or more unless you're running in TEST_MODE.

## Logging
This application uses structured logging based on `logging_config.yaml` file (loaded at startup). It supports
multiple log levels and formatters

To modify logging behavior:

1. Edit `speedtest/logging_config.yaml`
2. Mount a custom config into the container

Example:

```shell
docker run -v $(pwd)/logging_config.yaml:/app/speedtest/logging_config.yaml -p 8000:8000 speedtest-exporter
```

## Metrics Exposed

### Speedtest Execution

| Metric Name                | Type    | Description                                 |
|----------------------------|---------|---------------------------------------------|
| `speedtest_runs_total`     | Counter | Total number of speedtest executions        |
| `speedtest_failures_total` | Counter | Total number of failed speedtest executions |

### Ping

| Metric Name                 | Type  | Description                                          |
|-----------------------------|-------|------------------------------------------------------|
| ` speedtest_ping_jitter_ms` | Gauge | Jitter of the connection in milliseconds             |
| `speedtest_ping_latency_ms` | Gauge | Latency of the connection in milliseconds            |
| `speedtest_ping_low_ms`     | Gauge | Lowest ping latency during the test in milliseconds  |
| `speedtest_ping_high_ms`    | Gauge | Highest ping latency during the test in milliseconds |

### Download

| Metric Name                            | Type  | Description                                              |
|----------------------------------------|-------|----------------------------------------------------------|
| `speedtest_download_bandwidth_bps`     | Gauge | Download bandwidth in bits per second                    |
| `speedtest_download_bytes_total`       | Gauge | Total bytes downloaded during the test                   |
| `speedtest_download_elapsed_seconds`   | Gauge | Time taken for the download test in seconds              |
| `speedtest_download_latency_iqm_ms`    | Gauge | Interquartile mean of download latency in milliseconds   |
| `speedtest_download_latency_low_ms`    | Gauge | Lowest download latency during the test in milliseconds  |
| `speedtest_download_latency_high_ms`   | Gauge | Highest download latency during the test in milliseconds |
| `speedtest_download_latency_jitter_ms` | Gauge | Jitter of download latency in milliseconds               |

### Upload

| Metric Name                          | Type  | Description                                            |
|--------------------------------------|-------|--------------------------------------------------------|
| `speedtest_upload_bandwidth_bps`     | Gauge | Upload bandwidth in bits per second                    |
| `speedtest_upload_bytes_total`       | Gauge | Total bytes uploaded during the test                   |
| `speedtest_upload_elapsed_seconds`   | Gauge | Time taken for the upload test in seconds              |
| `speedtest_upload_latency_iqm_ms`    | Gauge | Interquartile mean of upload latency in milliseconds   |
| `speedtest_upload_latency_low_ms`    | Gauge | Lowest upload latency during the test in milliseconds  |
| `speedtest_upload_latency_high_ms`   | Gauge | Highest upload latency during the test in milliseconds |
| `speedtest_upload_latency_jitter_ms` | Gauge | Jitter of upload latency in milliseconds               |


### Packet Loss

| Metric Name                     | Type  | Description               |
|---------------------------------|-------|---------------------------|
| `speedtest_packet_loss_percent` | Gauge | Percentage of packet loss |


## Resources
- [Speedtest CLI](https://www.speedtest.net/apps/cli)
- [Prometheus](https://prometheus.io/)
