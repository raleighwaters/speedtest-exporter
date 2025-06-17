import json
import subprocess
import threading
import logging
from time import sleep

from speedtest.metrics import update_metrics
from speedtest.metrics import speedtest_runs_total, speedtest_failures_total
from speedtest.settings import settings

logger = logging.getLogger(__name__)

def run_speedtest():
    while True:
        try:
            logger.debug("Starting new speedtest run...")
            result = subprocess.run(
                ["speedtest", "--format=json"],
                capture_output=True, text=True, check=True
            )
            speedtest_runs_total.inc()
            data = json.loads(result.stdout)
            update_metrics(data)

        except subprocess.CalledProcessError as err:
            logger.error(f"[Speedtest failed] Command: {err.cmd}")
            logger.error(f"[Speedtest failed] Return code: {err.returncode}")
            process_output = (err.stdout or '') + (err.stderr or '')
            logger.error("[Speedtest failed] Command output:\n%s", process_output.strip())
            speedtest_failures_total.inc()

        except Exception as err:
            logger.exception(f"[Unexpected error running speedtest] {err}")
            speedtest_failures_total.inc()

        sleep(settings.SPEEDTEST_INTERVAL)


def test_run_speedtest():
    while True:
        logger.debug("Running speedtest")
        try:
            with open("example.json", "r") as input_file:
                result = input_file.read()

            speedtest_runs_total.inc()
            data = json.loads(result)
            update_metrics(data)

        except Exception as err:
            logger.error(f"[Speedtest error] {err}")
            logger.error(err)
            speedtest_failures_total.inc()

        sleep(settings.SPEEDTEST_INTERVAL)


def start_background_speedtest():
    if settings.TEST_MODE:
        thread_target = test_run_speedtest
    else:
        thread_target = run_speedtest

    thread = threading.Thread(target=thread_target, daemon=True)
    thread.start()
