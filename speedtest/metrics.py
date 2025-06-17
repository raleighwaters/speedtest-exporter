import logging

from prometheus_client import Gauge, Counter
from typing import Dict

logger = logging.getLogger(__name__)

# Speedtest Exec Information
speedtest_runs_total = Counter("speedtest_runs_total", "Total number of speedtest executions")
speedtest_failures_total = Counter("speedtest_failures_total", "Total number of failed speedtest executions")

# Ping Information (in milliseconds)
speedtest_ping_jitter_ms = Gauge("speedtest_ping_jitter_ms", "Jitter of the connection in milliseconds")
speedtest_ping_latency_ms = Gauge("speedtest_ping_latency_ms", "Latency of the connection in milliseconds")
speedtest_ping_low_ms = Gauge("speedtest_ping_low_ms", "Lowest ping latency during the test in milliseconds")
speedtest_ping_high_ms = Gauge("speedtest_ping_high_ms", "Highest ping latency during the test in milliseconds")

# Download Information (in bits per second)
speedtest_download_bandwidth_bps = Gauge("speedtest_download_bandwidth_bps", "Download bandwidth in bits per second")
speedtest_download_bytes_total = Gauge("speedtest_download_bytes_total", "Total bytes downloaded during the test")
speedtest_download_elapsed_seconds = Gauge("speedtest_download_elapsed_seconds", "Time taken for the download test in seconds")
speedtest_download_latency_iqm_ms = Gauge("speedtest_download_latency_iqm_ms", "Interquartile mean of download latency in milliseconds")
speedtest_download_latency_low_ms = Gauge("speedtest_download_latency_low_ms", "Lowest download latency during the test in milliseconds")
speedtest_download_latency_high_ms = Gauge("speedtest_download_latency_high_ms", "Highest download latency during the test in milliseconds")
speedtest_download_latency_jitter_ms = Gauge("speedtest_download_latency_jitter_ms", "Jitter of download latency in milliseconds")

# Upload Information (in bits per second)
speedtest_upload_bandwidth_bps = Gauge("speedtest_upload_bandwidth_bps", "Upload bandwidth in bits per second")
speedtest_upload_bytes_total = Gauge("speedtest_upload_bytes_total", "Total bytes uploaded during the test")
speedtest_upload_elapsed_seconds = Gauge("speedtest_upload_elapsed_seconds", "Time taken for the upload test in seconds")
speedtest_upload_latency_iqm_ms = Gauge("speedtest_upload_latency_iqm_ms", "Interquartile mean of upload latency in milliseconds")
speedtest_upload_latency_low_ms = Gauge("speedtest_upload_latency_low_ms", "Lowest upload latency during the test in milliseconds")
speedtest_upload_latency_high_ms = Gauge("speedtest_upload_latency_high_ms", "Highest upload latency during the test in milliseconds")
speedtest_upload_latency_jitter_ms = Gauge("speedtest_upload_latency_jitter_ms", "Jitter of upload latency in milliseconds")

# Packet Loss Result Information
speedtest_packet_loss_percent = Gauge("speedtest_packet_loss_percent", "Percentage of packet loss")


def update_metrics(results: Dict):
    """Updates the Prometheus metrics with the latest speedtest results."""

    if not isinstance(results, dict):
        print("[update_metrics] Invalid results type:", type(results))
        return

    if results:
        speedtest_ping_jitter_ms.set(results.get("ping", {}).get("jitter", 0))
        speedtest_ping_latency_ms.set(results.get("ping", {}).get("latency", 0))
        speedtest_ping_low_ms.set(results.get("ping", {}).get("low", 0))
        speedtest_ping_high_ms.set(results.get("ping", {}).get("high", 0))

        speedtest_download_bandwidth_bps.set(results.get("download", {}).get("bandwidth", 0) * 8)
        speedtest_download_bytes_total.set(results.get("download", {}).get("bytes", 0))
        speedtest_download_elapsed_seconds.set(results.get("download", {}).get("elapsed", 0) / 1000)
        speedtest_download_latency_iqm_ms.set(results.get("download", {}).get("latency", {}).get("iqm", 0))
        speedtest_download_latency_low_ms.set(results.get("download", {}).get("latency", {}).get("low", 0))
        speedtest_download_latency_high_ms.set(results.get("download", {}).get("latency", {}).get("high", 0))
        speedtest_download_latency_jitter_ms.set(results.get("download", {}).get("latency", {}).get("jitter", 0))

        speedtest_upload_bandwidth_bps.set(results.get("upload", {}).get("bandwidth", 0) * 8)
        speedtest_upload_bytes_total.set(results.get("upload", {}).get("bytes", 0))
        speedtest_upload_elapsed_seconds.set(results.get("upload", {}).get("elapsed", 0) / 1000)
        speedtest_upload_latency_iqm_ms.set(results.get("upload", {}).get("latency", {}).get("iqm", 0))
        speedtest_upload_latency_low_ms.set(results.get("upload", {}).get("latency", {}).get("low", 0))
        speedtest_upload_latency_high_ms.set(results.get("upload", {}).get("latency", {}).get("high", 0))
        speedtest_upload_latency_jitter_ms.set(results.get("upload", {}).get("latency", {}).get("jitter", 0))

        speedtest_packet_loss_percent.set(results.get("packetLoss", 0))
